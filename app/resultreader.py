<<<<<<< HEAD
from __future__ import annotations

import time
from pathlib import Path


class ResultReader:
    """
    Live reader for cf-knife output files.
    Monitors clean_ips-*.txt and returns only newly added lines.
    """

    def __init__(self, base_path: Path):

        self.base_path = Path(base_path)

        self.current_file = None

        self.file_position = 0

    # ----------------------------------------------------------

    def _find_latest_file(self):

        files = sorted(

            self.base_path.glob("clean_ips-*.txt"),

            key=lambda f: f.stat().st_mtime,

            reverse=True

        )

        if not files:

            return None

        return files[0]

    # ----------------------------------------------------------

    def start(self):

        """
        Wait until cf-knife creates the first output file.
        """

        while True:

            latest = self._find_latest_file()

            if latest is not None:

                self.current_file = latest

                self.file_position = 0

                return

            time.sleep(0.2)

    # ----------------------------------------------------------

    def read_new_lines(self):

        """
        Reads only newly appended lines.
        """

        if self.current_file is None:

            return []

        if not self.current_file.exists():

            return []

        lines = []

        with open(

            self.current_file,

            "r",

            encoding="utf-8",

            errors="ignore"

        ) as f:

            f.seek(self.file_position)

            for line in f:

                line = line.strip()

                if line:

                    lines.append(line)

            self.file_position = f.tell()

        return lines

    # ----------------------------------------------------------

    def follow(self):

        """
        Generator.
        """

        self.start()

        while True:

            lines = self.read_new_lines()

            for line in lines:

                yield line

=======
from __future__ import annotations

import time
from pathlib import Path


class ResultReader:
    """
    Live reader for cf-knife output files.
    Monitors clean_ips-*.txt and returns only newly added lines.
    """

    def __init__(self, base_path: Path):

        self.base_path = Path(base_path)

        self.current_file = None

        self.file_position = 0

    # ----------------------------------------------------------

    def _find_latest_file(self):

        files = sorted(

            self.base_path.glob("clean_ips-*.txt"),

            key=lambda f: f.stat().st_mtime,

            reverse=True

        )

        if not files:

            return None

        return files[0]

    # ----------------------------------------------------------

    def start(self):

        """
        Wait until cf-knife creates the first output file.
        """

        while True:

            latest = self._find_latest_file()

            if latest is not None:

                self.current_file = latest

                self.file_position = 0

                return

            time.sleep(0.2)

    # ----------------------------------------------------------

    def read_new_lines(self):

        """
        Reads only newly appended lines.
        """

        if self.current_file is None:

            return []

        if not self.current_file.exists():

            return []

        lines = []

        with open(

            self.current_file,

            "r",

            encoding="utf-8",

            errors="ignore"

        ) as f:

            f.seek(self.file_position)

            for line in f:

                line = line.strip()

                if line:

                    lines.append(line)

            self.file_position = f.tell()

        return lines

    # ----------------------------------------------------------

    def follow(self):

        """
        Generator.
        """

        self.start()

        while True:

            lines = self.read_new_lines()

            for line in lines:

                yield line

>>>>>>> 79d58fd8555281da2231e29208dea2e51a5e42a2
            time.sleep(0.25)