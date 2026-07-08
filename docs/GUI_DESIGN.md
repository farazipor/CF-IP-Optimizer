# GUI Design

CF-IP-Optimizer

Version 2.0

---

# Goal

The GUI should feel like a professional native Windows application.

It should remain responsive during long scans.

Users should never interact directly with backend modules.

---

# Responsibilities

GUI is responsible only for:

Drawing widgets

Collecting user input

Displaying progress

Displaying logs

Displaying results

Showing dialogs

Displaying statistics

Nothing else.

---

# Forbidden

GUI must never:

Launch cf-knife

Parse files

Read result files

Manage threads

Calculate rankings

Delete files

Open databases

Generate exports

Everything above belongs to Controller.

---

# Main Window

Top Toolbar

↓

Scan Settings

↓

Statistics

↓

Progress

↓

Result Table

↓

Live Log

↓

Status Bar

---

# Widgets

Domain Entry

Port Entry

Scan Mode

Start Button

Stop Button

Export Button

Open Results

Benchmark Button

Settings Button

Theme Switch

---

# Statistics

Elapsed Time

Found IPs

Scan Speed

Current State

Current Range

Current Threads

Current Sample

---

# Result Table

Columns

IP

Port

Latency

Range

Service

Status

Future

Country

ASN

Packet Loss

Score

---

# Progress

Progress Bar

Elapsed Timer

Current Range

Current File

Messages

---

# Log Window

Auto Scroll

Read Only

Timestamp

Colored Levels

INFO

WARNING

ERROR

SUCCESS

---

# Themes

Dark

Light

System

---

# Events

GUI receives events only from Controller.

Events

scan_started

scan_finished

scan_stopped

progress

new_result

log

error

benchmark_finished

---

# Future

History Window

Statistics Dashboard

Charts

Map

GeoIP View

Plugin Manager

Settings Window