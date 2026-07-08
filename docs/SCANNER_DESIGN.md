# Scanner Design

Version 2.0

---

# Goal

Scanner is a thin wrapper around cf-knife.exe.

It should never contain business logic.

---

# Responsibilities

Load config

Build command

Launch process

Read stdout

Stop process

Return exit code

---

# Forbidden

Scanner never:

Reads output files

Parses lines

Updates GUI

Calculates progress

Stores results

Ranks IPs

---

# Workflow

Load Config

↓

Build Command

↓

Launch cf-knife

↓

Read stdout

↓

Return Output

---

# Configuration

Loaded from config.json

Threads

Rate

Sample

Timeout

Timing

IPv4

Output File

Ranges

---

# Error Handling

Raise exceptions.

Never show MessageBox.

Never print.

---

# Future

Pause Scan

Resume Scan

Retry

Multiple Scanner Instances

Priority Control

Cancellation Tokens

Benchmark Mode