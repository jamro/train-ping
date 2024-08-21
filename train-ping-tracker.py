#!/usr/bin/env python3
import time
from datetime import datetime
from lib import parse_timetable
from lib import ping_google
from lib import get_last_station
from lib import log_to_csv
from lib import update_quality_history
import argparse

def main():
  
  parser = argparse.ArgumentParser(description="Train Ping Tracker")
  parser.add_argument("-t", "--timetable", help="timetable file", default="timetable.txt")
  parser.add_argument("-o", "--output", help="output file", default="ping_log.csv")
  args = parser.parse_args()

  print(f"Timeline file: {args.timetable}")
  print(f"Output file: {args.output}")

  timetable = parse_timetable(args.timetable)
  if timetable is None:
    print("Error: Failed to parse timetable.")
    return

  ping_filename = args.output
  quality_history = []
  
  while True:
    start_time = time.time()

    # Get the current timestamp
    timestamp = datetime.now()
    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    # Ping google.com 3 times and calculate the average ping time
    avg_ping_time = ping_google()

    # Calculate quality of connection
    quality = max(0, 950 - max(0, avg_ping_time - 50)) / 950 
    quality_history = update_quality_history(quality_history, timestamp, quality)

    last_station = get_last_station(timetable, datetime.now())

    print(f'{timestamp_str} - Average Ping Time: {avg_ping_time} ms - Quality: {quality:.2f} | {last_station}')
    
    # Log the average ping time and timestamp to the ping log CSV
    log_to_csv(ping_filename, {'Timestamp': timestamp_str, 'Average Ping Time (ms)': avg_ping_time, 'Quality': quality, 'Last Station': last_station}, 
                ['Timestamp', 'Average Ping Time (ms)', 'Quality', 'Last Station'])

    # Calculate elapsed time and sleep for the remainder of the 3-second interval
    elapsed_time = time.time() - start_time
    time.sleep(max(0, 3 - elapsed_time))

if __name__ == "__main__":
  main()
