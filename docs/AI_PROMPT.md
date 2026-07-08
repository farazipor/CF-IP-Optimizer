# AI Instructions

You are contributing to CF-IP-Optimizer.

Before writing any code you MUST read:

README.md

PROJECT_CONTEXT.md

ARCHITECTURE.md

PROJECT_RULES.md

CODING_STYLE.md

DIRECTORY_STRUCTURE.md

Never skip this step.

---

# Project Goal

Develop a professional Windows application around cf-knife.

This project is NOT a GUI wrapper.

The final application should feel like a native professional desktop application.

---

# Technology

Python 3.13

CustomTkinter

Windows

Pathlib

Threading

Dataclasses

cf-knife

---

# Architecture

GUI

↓

Controller

↓

Scanner

↓

cf-knife

↓

ResultReader

↓

Parser

↓

Controller

↓

GUI

Never break this architecture.

---

# Development Rules

Always return COMPLETE files.

Never return partial code.

Never use placeholders.

Never generate pseudo-code.

Always preserve compatibility.

Never rewrite unrelated modules.

Prefer refactoring over rewriting.

Never move business logic into GUI.

Never access widgets outside GUI thread.

Always use pathlib.

Always use Type Hints.

Always use dataclasses when appropriate.

Always use config.json.

Never hardcode values.

---

# Scanner Rules

Scanner only launches cf-knife.

Scanner never parses output.

Scanner never updates GUI.

Scanner never reads result files.

---

# Controller Rules

Controller owns the application state.

Controller manages all threads.

Controller dispatches all events.

Controller updates GUI.

---

# Parser Rules

Parser receives one line.

Parser returns one object.

Parser never opens files.

---

# GUI Rules

GUI draws widgets.

GUI receives events.

GUI displays results.

GUI never contains business logic.

---

# Code Style

PEP8

Pathlib

Type Hints

Meaningful Names

Small Functions

Small Classes

Docstrings

Single Responsibility

---

# Commit Style

feat(scanner)

fix(gui)

refactor(parser)

docs(readme)

test(scanner)

---

# Folder Structure

app/

config/

docs/

tools/

ranges/

results/

cache/

assets/

tests/

---

# Future Modules

Benchmark

Packet Loss

GeoIP

ASN

Speed Test

History

Statistics

Plugin Manager

Export

Auto Update

---

# AI Workflow

1 Read Documentation

2 Understand Architecture

3 Identify affected modules

4 Keep compatibility

5 Write complete code

6 Update documentation if needed

7 Never leave TODO inside source code

---

# Final Rule

Readable code is better than clever code.

Stable code is better than fast code.

Maintainable code is better than short code.

Professional architecture is more important than quick implementation.