#!/usr/bin/env python3
from lib import parse_timetable, read_pings
import argparse

def main():
    parser = argparse.ArgumentParser(description="Train Ping Tracker")
    parser.add_argument("-t", "--timetable", help="Path to the timetable file", default="timetable.txt")
    parser.add_argument("-i", "--input", help="Path to the input file", default="ping_log.csv")
    parser.add_argument("-s", "--segment", help="Length of a segment in seconds", type=int, default=60)
    args = parser.parse_args()

    print(f"Timetable file: {args.timetable}")
    print(f"Input file: {args.input}")

    timetable = parse_timetable(args.timetable)
    if timetable is None:
      print("Error: Failed to parse timetable.")
      return

    try:
      pings = read_pings(args.input, timetable)
    except Exception as e:
      print(f"Error reading pings: {e}")
      return

    if not pings:
      print("Error: No pings found in the input file.")
      return

    ping_sum = 0
    ping_count = 0
    segment_start = pings[0][0]

    segments = []

    for ping in pings:
      if (ping[0] - segment_start).seconds > args.segment:
        # Add segment summary
        if ping_count > 0:
          segments.append([segment_start, ping_sum / ping_count, ping[3]])
        # Reset for new segment
        segment_start = ping[0]
        ping_sum = 0
        ping_count = 0
      ping_sum += ping[1]
      ping_count += 1

    # Add the final segment if there were pings
    if ping_count > 0:
      segments.append([segment_start, ping_sum / ping_count, pings[-1][3]])

    print()
    print("==============================")
    print("TRAIN PING SUMMARY")
    print(f"Segment length: {args.segment} seconds")
    print("==============================")
    print()

    ping_symbols = [ (50, '█'), (80, '▇'), (100, '▆'), (150, '▅'), (300, '▄'), (500, '▃'), (800, '▂'), (float('inf'), '▁') ]

    station = ''
    for index, segment in enumerate(segments):
      if station != segment[2]:
        station = segment[2]
        if index == 0:
          print(f"[{station}] ", end='')
        else:
          print(f" [{station}]\n[{station}] ", end='')
      # Print visual representation of average ping time
      avg_ping = segment[1]
      for threshold, symbol in ping_symbols:
        if avg_ping < threshold:
          print(symbol, end='')
          break

    print("\n")

if __name__ == "__main__":
    main()
