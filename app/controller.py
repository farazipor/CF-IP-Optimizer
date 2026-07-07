<<<<<<< HEAD
from __future__ import annotations

import threading
import time
import traceback
from queue import Queue
from pathlib import Path
from typing import Callable, Optional

from scanner import Scanner
from resultreader import ResultReader
from parser import ResultParser


class Controller:
    """
    Main application controller.

    GUI
        │
        ▼
    Controller
        │
        ├── Scanner
        ├── ResultReader
        └── ResultParser
    """

    def __init__(
        self,
        base_path: Path,
        callback: Optional[Callable] = None
    ):

        self.base_path = Path(base_path)

        self.scanner = Scanner(self.base_path)

        self.reader = ResultReader(self.base_path)

        self.parser = ResultParser()

        #
        # State
        #

        self.running = False

        self.start_time = None

        self.results_count = 0

        #
        # Threads
        #

        self.scan_thread = None

        self.reader_thread = None

        self.timer_thread = None

        #
        # GUI callback
        #

        self.event_callback = callback   
        #
        # Thread Safe Event Queue
        #

        self.event_queue = Queue()
        
    # ---------------------------------------------------------
    # Events
    # ---------------------------------------------------------

    def emit(self, event, data=None):

    message = {

        "event": event,

        "data": data

    }

    #
    # Thread Safe Queue
    #

    self.event_queue.put(message)

    #
    # Optional Callback
    #

    if self.event_callback:

        self.event_callback(message)

    # ---------------------------------------------------------

    def is_running(self):

        return self.running

    # ---------------------------------------------------------
    # Reset
    # ---------------------------------------------------------

    def reset(self):

        self.running = False

        self.results_count = 0

        self.start_time = None

    # ---------------------------------------------------------
    # Cleanup
    # ---------------------------------------------------------

    def cleanup_old_results(self):

        patterns = (

            "clean_ips-*.txt",

            "clean_list.txt",

            "cf-knife.db",

            "domain-cache.txt"

        )

        for pattern in patterns:

            for file in self.base_path.glob(pattern):

                try:

                    file.unlink()

                except Exception:

                    pass

    # ---------------------------------------------------------
    # Prepare
    # ---------------------------------------------------------

    def prepare_scan(self):

        self.cleanup_old_results()

        self.reset()

    # ---------------------------------------------------------
    # Start
    # ---------------------------------------------------------

    def start_scan(

        self,

        domain,

        port

    ):

        if self.running:

            return

        self.running = True

        self.results_count = 0

        self.start_time = time.time()

        self.emit(

            "scan_started"

        )

        #
        # Scanner Thread
        #

        self.scan_thread = threading.Thread(

            target=self._scanner_worker,

            args=(

                domain,

                port

            ),

            daemon=True

        )

        self.scan_thread.start()

        #
        # Reader Thread
        #

        self.reader_thread = threading.Thread(

            target=self._reader_worker,

            daemon=True

        )

        self.reader_thread.start()

        #
        # Timer Thread
        #

        self.timer_thread = threading.Thread(

            target=self._timer_worker,

            daemon=True

        )

        self.timer_thread.start()
    # ---------------------------------------------------------
    # Scanner Worker
    # ---------------------------------------------------------

    def _scanner_worker(

        self,

        domain,

        port

    ):

        try:

            self.scanner.start(

                domain=domain,

                port=port,

                log_callback=self._scanner_log

            )

        except Exception:

            self.emit(

                "error",

                traceback.format_exc()

            )

        finally:

            #
            # اجازه بده Reader
            # آخرین خطوط فایل را بخواند
            #

            time.sleep(0.5)

            self.running = False

            self.emit(

                "scan_finished"

            )

    # ---------------------------------------------------------
    # Scanner Log
    # ---------------------------------------------------------

    def _scanner_log(

        self,

        line

    ):

        self.emit(

            "log",

            line

        )

    # ---------------------------------------------------------
    # Reader Worker
    # ---------------------------------------------------------

    def _reader_worker(self):

        try:

            for line in self.reader.follow():

                if not self.running:

                    break

                result = self.parser.parse(line)

                if result is None:

                    continue

                self.results_count += 1

                self.emit(

                    "new_result",

                    result

                )

                self.emit(

                    "found",

                    self.results_count

                )

        except Exception:

            self.emit(

                "error",

                traceback.format_exc()

            )

    # ---------------------------------------------------------
    # Timer Worker
    # ---------------------------------------------------------

    def _timer_worker(self):

        while self.running:

            elapsed = int(

                time.time() -

                self.start_time

            )

            minutes = elapsed // 60

            seconds = elapsed % 60

            self.emit(

                "elapsed",

                f"{minutes:02}:{seconds:02}"

            )

            time.sleep(1)
    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    def get_result_count(self):

        return self.results_count

    # ---------------------------------------------------------

    def get_elapsed_seconds(self):

        if self.start_time is None:

            return 0

        return int(

            time.time() -

            self.start_time

        )

    # ---------------------------------------------------------
    # Wait
    # ---------------------------------------------------------

    def wait_until_finished(self):

        if self.scan_thread:

            self.scan_thread.join(timeout=3)

        if self.reader_thread:

            self.reader_thread.join(timeout=3)

        if self.timer_thread:

            self.timer_thread.join(timeout=3)

    # ---------------------------------------------------------
    # Shutdown
    # ---------------------------------------------------------

    def shutdown(self):

        self.stop_scan()

=======
from __future__ import annotations

import threading
import time
import traceback
from queue import Queue
from pathlib import Path
from typing import Callable, Optional

from scanner import Scanner
from resultreader import ResultReader
from parser import ResultParser


class Controller:
    """
    Main application controller.

    GUI
        │
        ▼
    Controller
        │
        ├── Scanner
        ├── ResultReader
        └── ResultParser
    """

    def __init__(
        self,
        base_path: Path,
        callback: Optional[Callable] = None
    ):

        self.base_path = Path(base_path)

        self.scanner = Scanner(self.base_path)

        self.reader = ResultReader(self.base_path)

        self.parser = ResultParser()

        #
        # State
        #

        self.running = False

        self.start_time = None

        self.results_count = 0

        #
        # Threads
        #

        self.scan_thread = None

        self.reader_thread = None

        self.timer_thread = None

        #
        # GUI callback
        #

        self.event_callback = callback   
        #
        # Thread Safe Event Queue
        #

        self.event_queue = Queue()
        
    # ---------------------------------------------------------
    # Events
    # ---------------------------------------------------------

    def emit(self, event, data=None):

    message = {

        "event": event,

        "data": data

    }

    #
    # Thread Safe Queue
    #

    self.event_queue.put(message)

    #
    # Optional Callback
    #

    if self.event_callback:

        self.event_callback(message)

    # ---------------------------------------------------------

    def is_running(self):

        return self.running

    # ---------------------------------------------------------
    # Reset
    # ---------------------------------------------------------

    def reset(self):

        self.running = False

        self.results_count = 0

        self.start_time = None

    # ---------------------------------------------------------
    # Cleanup
    # ---------------------------------------------------------

    def cleanup_old_results(self):

        patterns = (

            "clean_ips-*.txt",

            "clean_list.txt",

            "cf-knife.db",

            "domain-cache.txt"

        )

        for pattern in patterns:

            for file in self.base_path.glob(pattern):

                try:

                    file.unlink()

                except Exception:

                    pass

    # ---------------------------------------------------------
    # Prepare
    # ---------------------------------------------------------

    def prepare_scan(self):

        self.cleanup_old_results()

        self.reset()

    # ---------------------------------------------------------
    # Start
    # ---------------------------------------------------------

    def start_scan(

        self,

        domain,

        port

    ):

        if self.running:

            return

        self.running = True

        self.results_count = 0

        self.start_time = time.time()

        self.emit(

            "scan_started"

        )

        #
        # Scanner Thread
        #

        self.scan_thread = threading.Thread(

            target=self._scanner_worker,

            args=(

                domain,

                port

            ),

            daemon=True

        )

        self.scan_thread.start()

        #
        # Reader Thread
        #

        self.reader_thread = threading.Thread(

            target=self._reader_worker,

            daemon=True

        )

        self.reader_thread.start()

        #
        # Timer Thread
        #

        self.timer_thread = threading.Thread(

            target=self._timer_worker,

            daemon=True

        )

        self.timer_thread.start()
    # ---------------------------------------------------------
    # Scanner Worker
    # ---------------------------------------------------------

    def _scanner_worker(

        self,

        domain,

        port

    ):

        try:

            self.scanner.start(

                domain=domain,

                port=port,

                log_callback=self._scanner_log

            )

        except Exception:

            self.emit(

                "error",

                traceback.format_exc()

            )

        finally:

            #
            # اجازه بده Reader
            # آخرین خطوط فایل را بخواند
            #

            time.sleep(0.5)

            self.running = False

            self.emit(

                "scan_finished"

            )

    # ---------------------------------------------------------
    # Scanner Log
    # ---------------------------------------------------------

    def _scanner_log(

        self,

        line

    ):

        self.emit(

            "log",

            line

        )

    # ---------------------------------------------------------
    # Reader Worker
    # ---------------------------------------------------------

    def _reader_worker(self):

        try:

            for line in self.reader.follow():

                if not self.running:

                    break

                result = self.parser.parse(line)

                if result is None:

                    continue

                self.results_count += 1

                self.emit(

                    "new_result",

                    result

                )

                self.emit(

                    "found",

                    self.results_count

                )

        except Exception:

            self.emit(

                "error",

                traceback.format_exc()

            )

    # ---------------------------------------------------------
    # Timer Worker
    # ---------------------------------------------------------

    def _timer_worker(self):

        while self.running:

            elapsed = int(

                time.time() -

                self.start_time

            )

            minutes = elapsed // 60

            seconds = elapsed % 60

            self.emit(

                "elapsed",

                f"{minutes:02}:{seconds:02}"

            )

            time.sleep(1)
    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    def get_result_count(self):

        return self.results_count

    # ---------------------------------------------------------

    def get_elapsed_seconds(self):

        if self.start_time is None:

            return 0

        return int(

            time.time() -

            self.start_time

        )

    # ---------------------------------------------------------
    # Wait
    # ---------------------------------------------------------

    def wait_until_finished(self):

        if self.scan_thread:

            self.scan_thread.join(timeout=3)

        if self.reader_thread:

            self.reader_thread.join(timeout=3)

        if self.timer_thread:

            self.timer_thread.join(timeout=3)

    # ---------------------------------------------------------
    # Shutdown
    # ---------------------------------------------------------

    def shutdown(self):

        self.stop_scan()

>>>>>>> 79d58fd8555281da2231e29208dea2e51a5e42a2
        self.wait_until_finished()