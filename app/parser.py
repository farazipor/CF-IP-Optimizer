<<<<<<< HEAD
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ScanResult:
    ip: str
    port: int
    sni: str
    latency: int
    service: str
    http_status: int
    tcp: bool
    tls: bool
    https: bool
    http2: bool
    http3: bool


class ResultParser:

    def __init__(self):

        self.pattern = re.compile(

            r'^(?P<ip>[\d\.]+)'
            r':(?P<port>\d+)'
            r'\s+\|\s+'
            r'sni=(?P<sni>.*?)'
            r'\s+\|\s+'
            r'latency=(?P<latency>\d+)ms'
            r'.*?'
            r'tcp=(?P<tcp>\w+)'
            r'\s+'
            r'tls=(?P<tls>\w+)'
            r'\s+'
            r'https=(?P<https>\w+)'
            r'\s+'
            r'http2=(?P<http2>\w+)'
            r'\s+'
            r'http3=(?P<http3>\w+)'
            r'.*?'
            r'service=(?P<service>.*?)'
            r'\s+\|\s+'
            r'http_status=(?P<status>\d+)'

        )

    # ------------------------------------------------------------

    def parse(self, line: str) -> Optional[ScanResult]:

        line = line.strip()

        if not line:

            return None

        m = self.pattern.match(line)

        if not m:

            return None

        return ScanResult(

            ip=m.group("ip"),

            port=int(m.group("port")),

            sni=m.group("sni"),

            latency=int(m.group("latency")),

            service=m.group("service"),

            http_status=int(m.group("status")),

            tcp=m.group("tcp") == "ok",

            tls=m.group("tls") == "ok",

            https=m.group("https") == "ok",

            http2=m.group("http2") == "ok",

            http3=m.group("http3") == "ok"

=======
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ScanResult:
    ip: str
    port: int
    sni: str
    latency: int
    service: str
    http_status: int
    tcp: bool
    tls: bool
    https: bool
    http2: bool
    http3: bool


class ResultParser:

    def __init__(self):

        self.pattern = re.compile(

            r'^(?P<ip>[\d\.]+)'
            r':(?P<port>\d+)'
            r'\s+\|\s+'
            r'sni=(?P<sni>.*?)'
            r'\s+\|\s+'
            r'latency=(?P<latency>\d+)ms'
            r'.*?'
            r'tcp=(?P<tcp>\w+)'
            r'\s+'
            r'tls=(?P<tls>\w+)'
            r'\s+'
            r'https=(?P<https>\w+)'
            r'\s+'
            r'http2=(?P<http2>\w+)'
            r'\s+'
            r'http3=(?P<http3>\w+)'
            r'.*?'
            r'service=(?P<service>.*?)'
            r'\s+\|\s+'
            r'http_status=(?P<status>\d+)'

        )

    # ------------------------------------------------------------

    def parse(self, line: str) -> Optional[ScanResult]:

        line = line.strip()

        if not line:

            return None

        m = self.pattern.match(line)

        if not m:

            return None

        return ScanResult(

            ip=m.group("ip"),

            port=int(m.group("port")),

            sni=m.group("sni"),

            latency=int(m.group("latency")),

            service=m.group("service"),

            http_status=int(m.group("status")),

            tcp=m.group("tcp") == "ok",

            tls=m.group("tls") == "ok",

            https=m.group("https") == "ok",

            http2=m.group("http2") == "ok",

            http3=m.group("http3") == "ok"

>>>>>>> 79d58fd8555281da2231e29208dea2e51a5e42a2
        )