# PROJECT_CONTEXT.md

# CF-IP-Optimizer

Developer Context Document

Version: 2.0

---

# 1. Purpose

This document explains the entire project.

Every AI assistant or developer MUST read this document before modifying any source code.

Never start coding before understanding this document.

This file is the source of truth for the architecture.

---

# 2. Vision

CF-IP-Optimizer is a professional desktop application built around cf-knife.

The application is NOT just a GUI.

The long-term goal is building a complete Cloudflare optimization suite.

The software should become the easiest and fastest way to discover high-quality Cloudflare IP addresses.

The software should be usable by both beginners and advanced users.

---

# 3. Main Goals

The project must always prioritize:

Fast Scan

Reliable Results

Modern UI

Clean Architecture

Easy Maintenance

Extensibility

Low Memory Usage

Responsiveness

Thread Safety

---

# 4. Design Philosophy

Every source file has exactly one responsibility.

Never combine multiple responsibilities into one class.

The project follows the Single Responsibility Principle.

The GUI must never contain business logic.

The Scanner must never know anything about GUI widgets.

The Parser must never execute scans.

The Controller is the only component allowed to communicate with all modules.

---

# 5. Project Architecture

GUI

↓

Controller

↓

Scanner

↓

cf-knife.exe

↓

ResultReader

↓

Parser

↓

Controller

↓

GUI

This architecture must never be broken.

---

# 6. Component Responsibilities

GUI

Responsible only for:

Drawing widgets

Showing results

Showing progress

Displaying logs

Handling user input

Nothing else.

Controller

Responsible for:

Starting scans

Stopping scans

Thread management

Event dispatching

State management

Progress updates

Scanner

Responsible for:

Loading config

Building command line

Launching cf-knife

Reading stdout

Stopping process

Nothing more.

Parser

Responsible for:

Parsing one line

Returning Python objects

Never reading files.

ResultReader

Responsible for:

Watching output files

Reading new lines

Sending lines to Parser

Nothing else.

---

# 7. Data Flow

User presses Scan

↓

GUI sends request

↓

Controller starts Scanner

↓

Scanner launches cf-knife

↓

cf-knife creates output file

↓

ResultReader follows output

↓

Parser parses lines

↓

Controller receives objects

↓

GUI updates table

---

# 8. Coding Rules

Always use:

Pathlib

Type Hints

Dataclasses

PEP8

Docstrings

Never use:

Global variables

Magic numbers

Hardcoded paths

Duplicated code

Nested responsibilities

---

# 9. Error Handling

Every module must raise meaningful exceptions.

Controller catches exceptions.

GUI displays user-friendly messages.

Scanner never displays MessageBox.

Parser never prints errors.

---

# 10. Threading Rules

GUI Thread

Only GUI.

Scanner Thread

Only cf-knife.

Reader Thread

Only reading files.

Timer Thread

Only elapsed timer.

Never access GUI widgets outside the GUI thread.

---

# 11. Performance

The software should remain responsive.

Scanning should never freeze the interface.

Reading results should happen continuously.

Parsing should be lightweight.

---

# 12. Scan Modes

Quick

Small IP ranges

Fast

Default mode

Normal

Balanced

Deep

Large ranges

Long scan

Custom

User-defined

---

# 13. Configuration

Everything configurable must come from config.json.

Never hardcode values.

Examples:

Threads

Rate

Timeout

Timing

Sample

IPv4

Default Mode

Output Folder

---

# 14. Results

All generated files belong inside

results/

Never create output files elsewhere.

---

# 15. Folder Layout

app/

config/

docs/

assets/

cache/

results/

ranges/

tools/

tests/

---

# 16. Future Features

Latency Ranking

Packet Loss

GeoIP

ASN

Country Detection

DNS Benchmark

TLS Benchmark

HTTP Benchmark

Real Download Speed

Export CSV

Export JSON

Export TXT

Configuration Generator

Plugin System

Automatic Updates

Dark/Light Theme

Multi-language

History Database

Statistics Dashboard

---

# 17. Development Rules

Never rewrite working code without reason.

Prefer refactoring over rewriting.

Small commits.

Meaningful commit messages.

One feature per commit.

Always preserve backward compatibility.

---

# 18. AI Instructions

Before modifying code:

Read README.md

Read PROJECT_CONTEXT.md

Read ARCHITECTURE.md

Understand project structure.

Understand responsibilities.

Never generate partial files.

Never mix responsibilities.

Never change folder structure unless explicitly requested.

Always return complete files.

Always preserve coding style.

---

# 19. Long-Term Goal

The final software should feel like a professional Windows application.

The user should never notice that the backend is based on cf-knife.

Everything should appear as one integrated application.

---

# End of Document