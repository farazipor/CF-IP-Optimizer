# Coding Style

## Python Version

Python 3.13+

---

## Formatting

PEP8

4 Spaces

UTF-8

LF

---

## Naming

Classes

PascalCase

Example

ResultReader

Controller

Scanner

---

Functions

snake_case

Example

start_scan()

load_config()

parse_result()

---

Variables

snake_case

Example

result_count

scan_thread

elapsed_time

---

Constants

UPPER_CASE

Example

DEFAULT_TIMEOUT

DEFAULT_PORT

---

## Type Hints

Mandatory.

Example

def start_scan(domain: str, port: int) -> None

---

## Imports

Standard Library

↓

Third Party

↓

Project Imports

---

## Path Handling

Always pathlib.

Never os.path.

---

## Exceptions

Never

except:

Always

except Exception as e

---

## Docstrings

Every public class.

Every public method.

---

## Comments

Explain WHY.

Not WHAT.

---

## Maximum Length

Function

50 Lines

Preferred

Class

400 Lines

Preferred

Module

800 Lines

Preferred

---

Readable code wins.