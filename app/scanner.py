from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Callable, Optional


class Scanner:
    """
    Executes CF-Knife.

    Responsibilities
    ----------------
    - Load config
    - Build command
    - Start process
    - Read stdout
    - Stop process
    """

    def __init__(self, base_path: Path):

        self.base_path = Path(base_path)

        self.config_path = (
            self.base_path /
            "config" /
            "config.json"
        )

        self.cfknife = (
            self.base_path /
            "tools" /
            "cf-knife.exe"
        )

        self.process: subprocess.Popen | None = None

        self.config = self._load_config()

    # --------------------------------------------------

    def _load_config(self) -> dict:

        with open(
            self.config_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    # --------------------------------------------------

    def is_running(self) -> bool:

        return (

            self.process is not None

            and

            self.process.poll() is None

        )

    # --------------------------------------------------

    def stop(self):

        if self.is_running():

            self.process.terminate()

    # --------------------------------------------------

    def build_command(

        self,

        domain: str,

        scan_mode: str = "quick"

    ) -> list[str]:

        benchmark = self.config["benchmark"]

        input_file = (

            self.base_path /

            "ranges" /

            f"{scan_mode}.txt"

        )

        cmd = [

            str(self.cfknife),

            "scan",

            "--input-file",

            str(input_file),

            "--sni",

            domain,

            "--port",

            str(self.config["port"]),

            "--threads",

            str(benchmark["threads"]),

            "--sample",

            str(benchmark["sample"]),

            "--rate",

            str(benchmark["rate"]),

            "--timeout",

            benchmark["timeout"],

            "--timing",

            str(benchmark["timing"]),

            "--verbose"

        ]

        if self.config.get(

            "ipv4_only",

            True

        ):

            cmd.append(

                "--ipv4-only"

            )

        return cmd

    # --------------------------------------------------

    def start(

        self,

        domain: str,

        scan_mode: str = "quick",

        callback: Optional[Callable[[str], None]] = None

    ) -> int:

        cmd = self.build_command(

            domain,

            scan_mode

        )

        flags = 0

        if hasattr(

            subprocess,

            "CREATE_NO_WINDOW"

        ):

            flags = subprocess.CREATE_NO_WINDOW

        self.process = subprocess.Popen(

            cmd,

            cwd=self.base_path,

            stdout=subprocess.PIPE,

            stderr=subprocess.STDOUT,

            text=True,

            bufsize=1,

            creationflags=flags

        )

        assert self.process.stdout is not None

        for line in self.process.stdout:

            line = line.rstrip()

            if callback:

                callback(line)

        self.process.wait()

        return self.process.returncode