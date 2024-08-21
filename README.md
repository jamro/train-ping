# Train-Ping

Train-Ping is a Python app designed to help train travelers monitor internet connection quality during their journeys. Unreliable connectivity can be a challenge on trains, especially when you need to stay productive. Train-Ping measures and logs the quality of your internet connection and maps it to your train timetable, helping you identify when and where you can expect stable internet access. **Train-Ping** helps you manage your expectations for internet connectivity on train journeys, ensuring you can plan your work or activities with confidence.

## Features

- **Track Internet Quality**: Measures and logs the quality of your internet connection at regular intervals.
- **Integrate with Timetable**: Maps connectivity data against a train timetable to identify connectivity patterns.
- **Visualize Connectivity**: Provides a visual summary of connectivity quality over time.

## Requirements

- Python 3.x

## Installation

**Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/train-ping.git
   cd train-ping
   ```

## Usage

### 1. Tracking Internet Quality

Use the `train-ping-tracker.py` script to track and log your internet connection quality.

```bash
./train-ping-tracker.py -t <timetable_file> -o <output_file>
```

**Arguments:**
- `-t`, `--timetable`: Path to the timetable file (default: `timetable.txt`).
- `-o`, `--output`: Path to the output CSV file where ping logs will be saved (default: `ping_log.csv`).

**Example:**
```bash
./train-ping-tracker.py -t timetable.txt -o ping_log.csv
```

### 2. Viewing Ping Summary

Use the `train-ping-viewer.py` script to view a summary of the collected ping data.

```bash
./train-ping-viewer.py -t <timetable_file> -i <input_file> -s <segment_length>
```

**Arguments:**
- `-t`, `--timetable`: Path to the timetable file (default: `timetable.txt`).
- `-i`, `--input`: Path to the input CSV file containing ping logs (default: `ping_log.csv`).
- `-s`, `--segment`: Length of a segment in seconds for summarizing ping data (default: `60`).

**Example:**

```bash
./train-ping-viewer.py -t timetable.txt -i ping_log.csv -s 60
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
