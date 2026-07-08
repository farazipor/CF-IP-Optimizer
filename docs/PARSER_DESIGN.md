# Parser Design

Version 2.0

---

# Goal

Convert one text line into one Python object.

Nothing more.

---

# Input

Single line.

Example

198.41.215.101 443 cloudflare.com 104ms

---

# Output

ScanResult

ip

port

latency

range

service

status

Future

country

asn

packet_loss

score

---

# Responsibilities

Validate line

Split values

Convert types

Return object

Ignore invalid lines

---

# Forbidden

Parser never:

Reads files

Writes files

Starts scans

Updates GUI

Shows dialogs

Deletes files

---

# Error Handling

Return None for invalid lines.

Raise only unexpected exceptions.

---

# Performance

Stateless

Lightweight

Fast

No caching

No I/O

---

# Future

JSON Parser

CSV Parser

Benchmark Parser

GeoIP Parser

Packet Loss Parser

Speed Test Parser