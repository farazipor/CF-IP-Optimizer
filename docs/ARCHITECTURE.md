# Architecture

CF-IP-Optimizer

Version 2.0

---

# Overview

The project follows a layered architecture.

Every layer has exactly one responsibility.

Communication always flows through the Controller.

Nothing bypasses the Controller.

---

# Architecture Diagram

+----------------------+

GUI

+----------+-----------+

|

v

+----------------------+

Controller

+----------+-----------+

|

+--------+---------+

| | |

v v v

Scanner ResultReader Timer

|

v

cf-knife.exe

|

v

Output Files

|

v

Parser

|

v

Controller

|

v

GUI

---

# Layers

Presentation Layer

GUI

Business Layer

Controller

Infrastructure Layer

Scanner

ResultReader

Configuration

Utilities

Parser

---

# GUI Layer

Responsibilities

Display widgets

Collect user input

Display progress

Display logs

Display results

Display errors

Never

Execute scans

Parse output

Read files

Manage threads

---

# Controller Layer

The Controller is the heart of the application.

Everything passes through the Controller.

Responsibilities

Create Scanner

Create ResultReader

Create Parser

Create Threads

Receive Events

Update GUI

Maintain State

Manage Timers

Dispatch Results

---

# Scanner Layer

Scanner is only responsible for executing cf-knife.

Responsibilities

Load configuration

Build command

Launch executable

Read stdout

Terminate process

Nothing else.

Scanner never knows anything about:

GUI

Parser

Tables

Widgets

Themes

---

# Result Reader Layer

Reads generated files continuously.

Responsibilities

Locate newest result file

Watch for changes

Read appended lines

Yield new lines

Nothing else.

---

# Parser Layer

Parser converts text into Python objects.

Input

One text line

Output

One ScanResult object

Parser never reads files.

Parser never updates GUI.

Parser never starts scans.

---

# Data Objects

Every parsed result becomes a ScanResult object.

Example

ScanResult

IP

Port

Latency

Network

Service

Country (future)

ASN (future)

Packet Loss (future)

Score (future)

---

# Event Flow

GUI

↓

Controller.start()

↓

Scanner.start()

↓

cf-knife

↓

ResultReader.follow()

↓

Parser.parse()

↓

Controller.on_result()

↓

GUI.add_row()

---

# Thread Model

Main Thread

GUI

Scanner Thread

Runs cf-knife

Reader Thread

Reads files

Timer Thread

Updates elapsed time

Future

Benchmark Thread

Never access GUI widgets outside Main Thread.

---

# File Structure

app/

controller.py

scanner.py

parser.py

resultreader.py

gui.py

main.py

config/

config.json

tools/

cf-knife.exe

ranges/

quick.txt

normal.txt

deep.txt

results/

Generated Files

cache/

Temporary Files

docs/

Documentation

assets/

Icons

Images

Themes

---

# Dependency Rules

GUI

↓

Controller

↓

Scanner

↓

cf-knife

Allowed

GUI → Controller

Controller → Scanner

Controller → Parser

Controller → Reader

Forbidden

Scanner → GUI

Parser → GUI

Reader → GUI

Scanner → Parser

GUI → Scanner

GUI → Reader

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

Completed

↓

Idle

or

Stopped

↓

Idle

---

# Configuration Flow

config.json

↓

Scanner

↓

Command Builder

↓

cf-knife

Never hardcode values.

Everything comes from config.

---

# Error Flow

Scanner Error

↓

Controller

↓

GUI

Reader Error

↓

Controller

↓

GUI

Parser Error

↓

Controller

↓

GUI

No module except GUI should display message boxes.

---

# Extension Points

Future modules

Benchmark

GeoIP

Packet Loss

Speed Test

Database

Plugin Manager

History Manager

Export Manager

Statistics Engine

These modules will communicate only through Controller.

---

# Design Principles

Single Responsibility

Open / Closed

Composition over Inheritance

Loose Coupling

High Cohesion

Thread Safety

No Circular Dependencies

No Hardcoded Paths

No Business Logic in GUI

No Duplicate Code

---

# Architecture Stability Rules

Never bypass Controller.

Never merge Scanner and Parser.

Never move business logic into GUI.

Never access widgets from worker threads.

Never duplicate parsing code.

Never hardcode configuration.

Never execute cf-knife directly from GUI.

This architecture is considered stable and should remain unchanged unless a major version introduces a new design.