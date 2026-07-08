# Project Development Rules

CF-IP-Optimizer

Version 2.0

---

# Purpose

This document defines the mandatory rules that every contributor, developer and AI assistant must follow.

These rules are considered part of the project architecture.

Violation of these rules will reduce code quality.

---

# Rule 1

Never change the architecture without a documented reason.

The architecture has already been designed.

Respect it.

---

# Rule 2

Every module has exactly ONE responsibility.

Examples

GUI

Displays information.

Controller

Controls workflow.

Scanner

Runs cf-knife.

Parser

Parses one line.

ResultReader

Reads files.

Nothing more.

---

# Rule 3

GUI must never contain business logic.

Forbidden

Running scanner

Opening files

Parsing output

Sorting results

Benchmark calculations

Building commands

Everything belongs to Controller.

---

# Rule 4

Scanner must never know GUI exists.

Scanner only executes:

cf-knife

Everything else belongs elsewhere.

---

# Rule 5

Never hardcode paths.

Wrong

"C:\\Project"

"./results"

Correct

Pathlib

base_path

config.json

---

# Rule 6

Never duplicate code.

If code exists once

Reuse it.

If copied twice

Refactor it.

---

# Rule 7

Always use Type Hints.

Wrong

def scan(domain):

Correct

def scan(domain: str) -> None:

---

# Rule 8

Always use Pathlib.

Never use

os.path

unless absolutely necessary.

---

# Rule 9

Configuration belongs only inside

config/config.json

Never duplicate values inside source code.

---

# Rule 10

Never block GUI.

Long operations must use

Worker Threads.

Examples

Scanning

Benchmark

Speed Test

Reading Files

Export

---

# Rule 11

Never update GUI from worker threads.

Only Main Thread updates widgets.

Communication uses

Events

Callbacks

Queues

---

# Rule 12

Every file begins with

Module Description

Imports

Classes

Functions

No executable code.

Only

main.py

may execute application startup.

---

# Rule 13

Every public class must have

Docstring

Responsibilities

Usage

---

# Rule 14

Every public function must have

Type Hints

Meaningful names

Short responsibilities

---

# Rule 15

Maximum class size

Preferred

300 lines

Acceptable

500

If larger

Refactor.

---

# Rule 16

Maximum function size

Preferred

40 lines

Maximum

80

If longer

Split it.

---

# Rule 17

Never use magic numbers.

Wrong

threads=37

Correct

config["threads"]

---

# Rule 18

Never silently ignore exceptions.

Wrong

except:

pass

Correct

except Exception as e:

log

raise

or

notify Controller.

---

# Rule 19

Logging

Every important action should be logged.

Examples

Scan Started

Scan Finished

File Opened

File Deleted

Benchmark Finished

Export Completed

---

# Rule 20

Commit Messages

Good

feat(scanner)

fix(gui)

docs(readme)

refactor(controller)

test(parser)

Bad

update

fix

changes

---

# Rule 21

Branch Strategy

main

Always stable.

develop

Future work.

feature/*

Single feature.

bugfix/*

Single bug.

---

# Rule 22

Versioning

Semantic Versioning

Major

Architecture changes.

Minor

New features.

Patch

Bug fixes.

Example

2.0.0

2.1.0

2.1.3

3.0.0

---

# Rule 23

Folder Responsibilities

app/

Application source.

config/

Configuration.

results/

Generated files.

ranges/

IP ranges.

cache/

Temporary data.

assets/

Icons.

docs/

Documentation.

tests/

Unit tests.

tools/

Third-party executables.

---

# Rule 24

Never modify third-party software.

cf-knife.exe

is external.

Do not patch it.

Do not reverse engineer it.

Wrap it.

---

# Rule 25

Scanner Output

Scanner writes logs.

ResultReader reads files.

Parser parses.

Controller distributes.

GUI displays.

Never skip steps.

---

# Rule 26

Future modules

Every future module must integrate through Controller.

Examples

GeoIP

Benchmark

Speed Test

Database

History

Statistics

Plugins

Never communicate directly with GUI.

---

# Rule 27

Code Review Checklist

□ No duplicated code

□ Uses Pathlib

□ Uses Type Hints

□ Thread Safe

□ No GUI logic

□ No hardcoded paths

□ Clear naming

□ Proper exceptions

□ PEP8

□ Documentation updated

---

# Rule 28

AI Rules

Before generating code

Read

README.md

PROJECT_CONTEXT.md

ARCHITECTURE.md

PROJECT_RULES.md

Never generate partial implementations.

Never rewrite unrelated modules.

Always preserve compatibility.

Always output complete files.

---

# Rule 29

Performance Rules

GUI must remain responsive.

Memory usage should stay low.

Reading results must be incremental.

Avoid unnecessary allocations.

Prefer streaming over loading entire files.

---

# Rule 30

Final Principle

Readable code is more important than clever code.

Maintainability is more important than short code.

Stability is more important than adding features.

Professional architecture is more important than quick fixes.

This document is mandatory for every future version of the project.