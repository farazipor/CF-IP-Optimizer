from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(slots=True)
class ScanResult:

    ip: str

    port: int

    latency: int

    network: str

    service: str


class ResultParser:
    """
    Parses CF-Knife output lines.

    Example:

    104.24.41.222 443 cloudflare.com 142ms 104.24.0.0/14 ok ok ok ok fail cloudflare
    """

    RESULT_PATTERN = re.compile(

        r"^(?P<ip>\d+\.\d+\.\d+\.\d+)\s+"

        r"(?P<port>\d+)\s+"

        r"\S+\s+"

        r"(?P<latency>\d+)ms\s+"

        r"(?P<range>\S+)\s+"

        r".*?"

        r"(?P<service>cloudflare|-)$"

    )

    def parse(

        self,

        line: str

    ) -> ScanResult | None:

        line = line.strip()

        match = self.RESULT_PATTERN.match(line)

        if not match:

            return None

        return ScanResult(

            ip=match.group("ip"),

            port=int(

                match.group("port")

            ),

            latency=int(

                match.group("latency")

            ),

            network=match.group("range"),

            service=match.group("service")

        )