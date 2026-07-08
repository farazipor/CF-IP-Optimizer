# Controller Design

Version 2.0

---

# Goal

Controller is the heart of the application.

Every module communicates through Controller.

---

# Responsibilities

Create Scanner

Create Parser

Create ResultReader

Manage Threads

Dispatch Events

Maintain State

Update GUI

Handle Errors

---

# State Machine

Idle

↓

Preparing

↓

Scanning

↓

Reading

↓

Finished

↓

Idle

---

# Threads

Scanner Thread

Reader Thread

Timer Thread

Future Benchmark Thread

---

# Events

scan_started

scan_finished

scan_stopped

elapsed

progress

new_result

found

error

log

---

# Internal State

running

results_count

elapsed_time

current_mode

current_range

scan_start_time

---

# Rules

Never parse inside Controller.

Never read files.

Never execute cf-knife directly.

Never access GUI widgets.

Only communicate using callbacks.

---

# Future

Plugin Manager

History Manager

Benchmark Manager

Statistics Engine

Auto Update