# CF-IP-Optimizer

Professional Cloudflare IP Optimizer

---

## Project Goal

CF-IP-Optimizer is a professional Windows application built around **cf-knife**.

The purpose of this project is finding the fastest and most stable Cloudflare IPs for any domain.

This project is NOT a simple GUI wrapper.

The goal is to become a complete optimization suite for Cloudflare connectivity.

---

## Features

- Modern CustomTkinter GUI
- Fast Cloudflare Scanner
- Real-time Progress
- Live Logs
- Live Result Table
- Quick / Normal / Deep Scan
- Benchmark
- Result Ranking
- Export Results
- Save History
- Top 10 Best IPs
- Config Generator
- Automatic Result Reader
- Resume Scan
- Future Plugin Support

---

## Architecture

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

GUI

---

## Technologies

Python 3.13

CustomTkinter

Pathlib

Threading

Dataclasses

cf-knife

Windows

---

## Directory Structure

app/

config/

docs/

ranges/

results/

cache/

tools/

assets/

tests/

---

## Design Philosophy

Every file has exactly ONE responsibility.

GUI never executes scanner.

Scanner never updates GUI.

Parser never reads files.

Controller controls everything.

---

## Project Status

Version

2.0 Development

---

## Coding Rules

PEP8

Type Hints

No Global Variables

No Duplicate Code

Pathlib Only

Single Responsibility Principle

Thread Safe

---

## Future Versions

2.1

Better GUI

2.2

Benchmark

2.3

Packet Loss

2.4

GeoIP

3.0

Plugin System

---

## License

MIT