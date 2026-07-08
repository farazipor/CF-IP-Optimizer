# Result Reader Design

Version 2.0

---

# Goal

ResultReader continuously watches scan result files.

It reads only newly appended lines.

It never loads the entire file into memory.

---

# Responsibilities

Locate newest result file

Watch file changes

Read appended lines

Yield new lines

Detect file rotation

Handle missing files

---

# Forbidden

ResultReader never:

Parses lines

Updates GUI

Runs Scanner

Starts Threads

Deletes files

Calculates statistics

---

# Workflow

Wait for Result File

↓

Open File

↓

Seek End

↓

Read New Line

↓

Yield Line

↓

Repeat

---

# Input

clean_ips.txt

clean_list.txt

Future

benchmark.json

statistics.json

---

# Output

One raw text line.

Nothing else.

---

# Error Handling

Retry on missing file.

Ignore temporary file locks.

Raise unexpected exceptions.

---

# Performance

Streaming

Minimal Memory

Non-blocking

Incremental Reading

---

# Future

Multiple Output Files

JSON Support

CSV Support

Compressed Results

Live Database Reader