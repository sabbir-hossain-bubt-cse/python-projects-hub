# Multi-Threaded TCP Port Scanner

A fast and lightweight multi-threaded TCP port scanner built with Python. This script scans standard network ports ($1-1024$) on a target host concurrently using worker threads and a thread-safe queue.

# Features
  *Multi-threading:** Leverages 100 concurrent threads to speed up the scanning process.
  *Thread-Safe Output:** Utilizes threading locks to prevent overlapping or jumbled text in the terminal.
  *Socket Timeouts:** Configured with a 1-second timeout to handle non-responsive or closed ports efficiently.
  *Queue Management:** Uses Python's built-in `queue.Queue` for seamless task assignment across threads.


# Requirements
- Python 3.x


# Usage

1. Clone or copy the project into your local directory.
2. Navigate to the project folder:
   ```bash
   cd port_scanner_project

# How to run:

python <file_name>.py