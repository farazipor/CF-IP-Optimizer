<<<<<<< HEAD
from __future__ import annotations

import json
import subprocess
from pathlib import Path


class CFKnifeCommandBuilder:
    """
    Build cf-knife command.
    """

    def __init__(self, base_path: Path):

        self.base_path = Path(base_path)

        self.config_path = self.base_path / "config.json"

        self.cfknife = self.base_path / "cf-knife.exe"

        self.config = self._load_config()

    # ----------------------------------------------------------

    def _load_config(self):

        with open(
            self.config_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    # ----------------------------------------------------------

    def _get_ranges_file(self, mode: str) -> Path:

        mode = mode.lower()

        if mode == "quick":
            return self.base_path / "ranges" / "quick.txt"

        elif mode == "normal":
            return self.base_path / "ranges" / "normal.txt"

        elif mode == "deep":
            return self.base_path / "ranges" / "deep.txt"

        return self.base_path / "ranges" / "quick.txt"

    # ----------------------------------------------------------

    def build(
        self,
        domain: str,
        port: int,
        mode: str = "quick"
    ):

        benchmark = self.config["benchmark"]

        ranges_file = self._get_ranges_file(mode)

        cmd = [

            str(self.cfknife),

            "scan",

            "--input-file",
            str(ranges_file),

            "--sni",
            domain,

            "--port",
            str(port),

            "--sample",
            str(benchmark.get("sample", 20)),

            "--threads",
            str(benchmark.get("threads", 40)),

            "--rate",
            str(benchmark.get("rate", 300)),

            "--timeout",
            benchmark.get("timeout", "2s"),

            "--timing",
            str(benchmark.get("timing", 2)),

            "--ipv4-only",

            "--output",
            "clean_ips.txt",

            "--verbose"

        ]

        return cmd


# =====================================================================


class Scanner:

    def __init__(self, base_path: Path):

        self.base_path = Path(base_path)

        self.builder = CFKnifeCommandBuilder(base_path)

        self.process = None

    # ----------------------------------------------------------

    def running(self):

        return (

            self.process is not None

            and

            self.process.poll() is None

        )

    # ----------------------------------------------------------

    def stop(self):

        if self.running():

            self.process.terminate()

    # ----------------------------------------------------------

    def start(

        self,

        domain,

        port,

        log_callback=None,

        mode="quick"

    ):

        cmd = self.builder.build(

            domain,

            port,

            mode

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

        try:

            for line in self.process.stdout:

                line = line.rstrip()

                if log_callback:

                    log_callback(line)

        finally:

            self.process.wait()

=======
from __future__ import annotations

import json
import subprocess
from pathlib import Path


class CFKnifeCommandBuilder:
    """
    Build cf-knife command.
    """

    def __init__(self, base_path: Path):

        self.base_path = Path(base_path)

        self.config_path = self.base_path / "config.json"

        self.cfknife = self.base_path / "cf-knife.exe"

        self.config = self._load_config()

    # ----------------------------------------------------------

    def _load_config(self):

        with open(
            self.config_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    # ----------------------------------------------------------

    def _get_ranges_file(self, mode: str) -> Path:

        mode = mode.lower()

        if mode == "quick":
            return self.base_path / "ranges" / "quick.txt"

        elif mode == "normal":
            return self.base_path / "ranges" / "normal.txt"

        elif mode == "deep":
            return self.base_path / "ranges" / "deep.txt"

        return self.base_path / "ranges" / "quick.txt"

    # ----------------------------------------------------------

    def build(
        self,
        domain: str,
        port: int,
        mode: str = "quick"
    ):

        benchmark = self.config["benchmark"]

        ranges_file = self._get_ranges_file(mode)

        cmd = [

            str(self.cfknife),

            "scan",

            "--input-file",
            str(ranges_file),

            "--sni",
            domain,

            "--port",
            str(port),

            "--sample",
            str(benchmark.get("sample", 20)),

            "--threads",
            str(benchmark.get("threads", 40)),

            "--rate",
            str(benchmark.get("rate", 300)),

            "--timeout",
            benchmark.get("timeout", "2s"),

            "--timing",
            str(benchmark.get("timing", 2)),

            "--ipv4-only",

            "--output",
            "clean_ips.txt",

            "--verbose"

        ]

        return cmd


# =====================================================================


class Scanner:

    def __init__(self, base_path: Path):

        self.base_path = Path(base_path)

        self.builder = CFKnifeCommandBuilder(base_path)

        self.process = None

    # ----------------------------------------------------------

    def running(self):

        return (

            self.process is not None

            and

            self.process.poll() is None

        )

    # ----------------------------------------------------------

    def stop(self):

        if self.running():

            self.process.terminate()

    # ----------------------------------------------------------

    def start(

        self,

        domain,

        port,

        log_callback=None,

        mode="quick"

    ):

        cmd = self.builder.build(

            domain,

            port,

            mode

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

        try:

            for line in self.process.stdout:

                line = line.rstrip()

                if log_callback:

                    log_callback(line)

        finally:

            self.process.wait()

>>>>>>> 79d58fd8555281da2231e29208dea2e51a5e42a2
        return self.process.returncode