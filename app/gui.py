<<<<<<< HEAD
from __future__ import annotations

from pathlib import Path
from tkinter import ttk
import queue

import customtkinter as ctk

from controller import Controller


class CFIPOptimizerApp(ctk.CTk):

    """
    Main GUI
    """

    def __init__(self, base_path: Path):

        super().__init__()

        self.base_path = Path(base_path)

        self.controller = Controller(self.base_path)

        self.event_queue = queue.Queue()

        self.controller.set_event_callback(
            self.on_controller_event
        )

        ctk.set_appearance_mode("Dark")

        ctk.set_default_color_theme("blue")

        self.title("CF IP Optimizer v2")

        self.geometry("1220x820")

        self.minsize(1150, 760)

        self.protocol(

            "WM_DELETE_WINDOW",

            self.on_close

        )

        self.create_widgets()
		
	self.initialize()

        self.after(

            100,

            self.process_events

        )

    # -----------------------------------------------------

    def create_widgets(self):

        #
        # Title
        #

        self.title_label = ctk.CTkLabel(

            self,

            text="CF IP Optimizer v2",

            font=(

                "Segoe UI",

                30,

                "bold"

            )

        )

        self.title_label.pack(

            pady=(20, 15)

        )

        # --------------------------------------------

        self.input_frame = ctk.CTkFrame(

            self

        )

        self.input_frame.pack(

            fill="x",

            padx=20,

            pady=10

        )

        # --------------------------------------------

        self.domain_entry = ctk.CTkEntry(

            self.input_frame,

            width=420,

            placeholder_text="Domain (SNI)"

        )

        self.domain_entry.grid(

            row=0,

            column=0,

            padx=15,

            pady=20

        )

        # --------------------------------------------

        self.port_entry = ctk.CTkEntry(

            self.input_frame,

            width=120

        )

        self.port_entry.insert(

            0,

            "443"

        )

        self.port_entry.grid(

            row=0,

            column=1,

            padx=10

        )

        # --------------------------------------------

        self.start_button = ctk.CTkButton(

            self.input_frame,

            text="Start Scan",

            width=180,

            command=self.start_scan

        )

        self.start_button.grid(

            row=0,

            column=2,

            padx=10

        )

        # --------------------------------------------

        self.stop_button = ctk.CTkButton(

            self.input_frame,

            text="Stop",

            width=140,

            fg_color="#C0392B",

            hover_color="#922B21",

            command=self.stop_scan

        )

        self.stop_button.grid(

            row=0,

            column=3,

            padx=10

        )

        # --------------------------------------------

        self.import_button = ctk.CTkButton(

            self.input_frame,

            text="Import Config",

            width=160,
			
    command=self.import_config

        )

        self.import_button.grid(

            row=0,

            column=4,

            padx=10

        )

        # --------------------------------------------

        self.generate_button = ctk.CTkButton(

            self.input_frame,

            text="Generate Configs",

            width=180,
			
    command=self.generate_configs

        )

        self.generate_button.grid(

            row=0,

            column=5,

            padx=10

        )

        # --------------------------------------------

        self.progress = ctk.CTkProgressBar(

            self

        )

        self.progress.pack(

            fill="x",

            padx=20,

            pady=(15, 5)

        )

        self.progress.set(0)

        # --------------------------------------------

        self.progress_label = ctk.CTkLabel(

            self,

            text="0 %"

        )

        self.progress_label.pack()

        # --------------------------------------------

        self.info_frame = ctk.CTkFrame(

            self

        )

        self.info_frame.pack(

            fill="x",

            padx=20,

            pady=15

        )

        self.elapsed_label = ctk.CTkLabel(

            self.info_frame,

            text="Elapsed : 00:00"

        )

        self.elapsed_label.pack(

            side="left",

            padx=20

        )

        self.found_label = ctk.CTkLabel(

            self.info_frame,

            text="Found : 0"

        )

        self.found_label.pack(

            side="left",

            padx=20

        )

        self.status_label = ctk.CTkLabel(

            self.info_frame,

            text="Ready"

        )

        self.status_label.pack(

            side="right",

            padx=20

        )
		        # =====================================================
        # Result Table
        # =====================================================

        self.table_frame = ctk.CTkFrame(
            self
        )

        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure(

            "Treeview",

            rowheight=30,

            font=("Segoe UI", 10)

        )

        style.configure(

            "Treeview.Heading",

            font=("Segoe UI", 10, "bold")

        )

        columns = (

            "IP",

            "Latency",

            "Download",

            "Upload",

            "Jitter"

        )

        self.table = ttk.Treeview(

            self.table_frame,

            columns=columns,

            show="headings",

            height=18

        )

        #
        # Headings
        #

        self.table.heading(

            "IP",

            text="IP Address"

        )

        self.table.heading(

            "Latency",

            text="Latency"

        )

        self.table.heading(

            "Download",

            text="Download"

        )

        self.table.heading(

            "Upload",

            text="Upload"

        )

        self.table.heading(

            "Jitter",

            text="Jitter"

        )

        #
        # Columns
        #

        self.table.column(

            "IP",

            width=330,

            anchor="center"

        )

        self.table.column(

            "Latency",

            width=120,

            anchor="center"

        )

        self.table.column(

            "Download",

            width=140,

            anchor="center"

        )

        self.table.column(

            "Upload",

            width=140,

            anchor="center"

        )

        self.table.column(

            "Jitter",

            width=120,

            anchor="center"

        )

        #
        # Scrollbar
        #

        self.scrollbar = ttk.Scrollbar(

            self.table_frame,

            orient="vertical",

            command=self.table.yview

        )

        self.table.configure(

            yscrollcommand=self.scrollbar.set

        )

        self.table.pack(

            side="left",

            fill="both",

            expand=True

        )

        self.scrollbar.pack(

            side="right",

            fill="y"

        )

        #
        # اولین ردیف
        #
		
    self.configure_table_tags()

        self.table.insert(

            "",

            "end",

            values=(
			
                "Waiting for scan...",

                "-",

                "-",

                "-",

                "-"

            )
			
        )
		

    # =========================================================
    # Scan Buttons
    # =========================================================

    def start_scan(self):

        domain = self.domain_entry.get().strip()

        if not domain:

            self.status_label.configure(

                text="Please enter a domain."

            )

            return

        try:

            port = int(

                self.port_entry.get()

            )

        except ValueError:

            self.status_label.configure(

                text="Invalid port."

            )

            return

        #
        # Reset UI
        #

        self.progress.set(0)

        self.progress_label.configure(

            text="0 %"

        )

        self.found_label.configure(

            text="Found : 0"

        )

        self.elapsed_label.configure(

            text="Elapsed : 00:00"

        )

        self.status_label.configure(

            text="Scanning..."

        )

        #
        # پاک کردن جدول
        #

        for item in self.table.get_children():

            self.table.delete(item)

        #
        # شروع اسکن
        #

    self.controller.prepare_scan()
		
    self.lock_controls()

        self.controller.start_scan(

            domain,

            port

        )

    # -----------------------------------------------------

    def stop_scan(self):

        self.controller.stop_scan()

        self.status_label.configure(

            text="Stopped"

        )
		    # =====================================================
    # Controller Events
    # =====================================================

    def on_controller_event(self, event):

    #
    # دیگر کاری لازم نیست.
    # Event داخل Controller وارد Queue شده است.
    #

    pass

    # -----------------------------------------------------

    def process_events(self):

        while not self.event_queue.empty():

            event = self.event_queue.get()

            name = event.get("event")

            data = event.get("data")

            #
            # Scan Started
            #

            if name == "scan_started":

                self.status_label.configure(

                    text="Scanning..."

                )

            #
            # Scan Finished
            #

            elif name == "scan_finished":

                self.process_finished()

            #
            # Scan Stopped
            #

            elif name == "scan_stopped":

                self.status_label.configure(

                    text="Stopped"

                )
				self.unlock_controls()

            #
            # Found Counter
            #

            elif name == "found":

                self.found_label.configure(

                    text=f"Found : {data}"

                )

            #
            # Elapsed Time
            #

            elif name == "elapsed":

                self.elapsed_label.configure(

                    text=f"Elapsed : {data}"

                )

            #
            # New Result
            #

            elif name == "new_result":

                self.add_result(data)

            #
            # Error
            #

            elif name == "error":

                self.status_label.configure(

                    text=str(data)

                )

            #
            # Log
            #

            elif name == "log":

                #
                # بعداً Progress واقعی را
                # از لاگ استخراج می‌کنیم.
                #

                pass

        #
        # keep polling
        #

        self.after(

            100,

            self.process_events

        )

    # =====================================================
    # Result Table
    # =====================================================

    def add_result(

        self,

        result

    ):

        #
        # فعلاً Download / Upload / Jitter
        # توسط cf-knife خروجی نمی‌شوند.
        # بعداً SpeedTest اضافه می‌شود.
        #
		
		tag = self.latency_tag(result.latency)

        self.table.insert(

            "",

            "end",

            values=(

                result.ip,

                f"{result.latency} ms",

                "-",

                "-",

                "-"

            ),
			
			tags=(tag,)

    )
		
    self.update_progress_from_results()

        #
        # همیشه آخرین آیتم دیده شود
        #

        children = self.table.get_children()

        if children:

            self.table.see(

                children[-1]

            )
			    # =====================================================
    # UI Helpers
    # =====================================================

    def clear_table(self):
        """
        Remove all rows from result table.
        """

        for item in self.table.get_children():
            self.table.delete(item)

    # -----------------------------------------------------

    def reset_ui(self):
        """
        Reset GUI to initial state.
        """

        self.clear_table()

        self.progress.set(0)

        self.progress_label.configure(
            text="0 %"
        )

        self.found_label.configure(
            text="Found : 0"
        )

        self.elapsed_label.configure(
            text="Elapsed : 00:00"
        )

        self.status_label.configure(
            text="Ready"
        )

    # -----------------------------------------------------

    def lock_controls(self):
        """
        Disable controls while scanning.
        """

        self.start_button.configure(
            state="disabled"
        )

        self.domain_entry.configure(
            state="disabled"
        )

        self.port_entry.configure(
            state="disabled"
        )

        self.import_button.configure(
            state="disabled"
        )

        self.generate_button.configure(
            state="disabled"
        )

        self.stop_button.configure(
            state="normal"
        )

    # -----------------------------------------------------

    def unlock_controls(self):
        """
        Enable controls after scan.
        """

        self.start_button.configure(
            state="normal"
        )

        self.domain_entry.configure(
            state="normal"
        )

        self.port_entry.configure(
            state="normal"
        )

        self.import_button.configure(
            state="normal"
        )

        self.generate_button.configure(
            state="normal"
        )

        self.stop_button.configure(
            state="normal"
        )

    # =====================================================
    # Future Buttons
    # =====================================================

    def import_config(self):
        """
        Reserved for config import.
        """

        self.status_label.configure(
            text="Import Config (Coming Soon)"
        )

    # -----------------------------------------------------

    def generate_configs(self):
        """
        Reserved for Config Builder.
        """

        self.status_label.configure(
            text="Generate Configs (Coming Soon)"
        )

    # =====================================================
    # Window Events
    # =====================================================

    def on_close(self):
        """
        Close application safely.
        """

        try:

            self.controller.shutdown()

        except Exception:

            pass

        self.destroy()
		    # =====================================================
    # Progress
    # =====================================================

    def update_progress(self, value: float):
        """
        value : 0.0 -> 1.0
        """

        value = max(0.0, min(1.0, value))

        self.progress.set(value)

        self.progress_label.configure(
            text=f"{int(value*100)} %"
        )

    # -----------------------------------------------------

    def update_progress_from_results(self):
        """
        Temporary progress estimation.

        تا زمانی که cf-knife درصد واقعی را
        اعلام نکند از تعداد IPها استفاده می‌کنیم.
        """

        found = self.controller.get_result_count()

        #
        # فعلاً هر 10 IP = 10%
        #

        progress = min(found / 100, 1.0)

        self.update_progress(progress)

    # =====================================================
    # Table Colors
    # =====================================================

    def configure_table_tags(self):

        self.table.tag_configure(

            "excellent",

            background="#1E8449"

        )

        self.table.tag_configure(

            "good",

            background="#21618C"

        )

        self.table.tag_configure(

            "medium",

            background="#9A7D0A"

        )

        self.table.tag_configure(

            "bad",

            background="#922B21"

        )

    # -----------------------------------------------------

    def latency_tag(self, latency):

        if latency <= 50:

            return "excellent"

        if latency <= 120:

            return "good"

        if latency <= 250:

            return "medium"

        return "bad"

    # =====================================================
    # Sorting
    # =====================================================

    def sort_by_latency(self):

        rows = []

        for item in self.table.get_children():

            values = self.table.item(item)["values"]

            try:

                latency = int(

                    str(values[1]).replace(

                        " ms",

                        ""

                    )

                )

            except Exception:

                latency = 9999

            rows.append(

                (

                    latency,

                    values

                )

            )

        rows.sort(

            key=lambda x: x[0]

        )

        self.clear_table()

        for _, values in rows:

            tag = self.latency_tag(

                int(

                    str(values[1]).replace(

                        " ms",

                        ""

                    )

                )

            )

            self.table.insert(

                "",

                "end",

                values=values,

                tags=(tag,)

            )

    # =====================================================
    # Top 10
    # =====================================================

    def get_top10(self):

        rows = []

        for item in self.table.get_children():

            rows.append(

                self.table.item(item)["values"]

            )

        rows.sort(

            key=lambda row:

            int(

                str(row[1]).replace(

                    " ms",

                    ""

                )

            )

        )

        return rows[:10]
		    # =====================================================
    # Settings
    # =====================================================

    def load_defaults(self):
        """
        Load default values when application starts.
        """

        try:

            if not self.domain_entry.get():

                self.domain_entry.insert(
                    0,
                    "cloudflare.com"
                )

            if not self.port_entry.get():

                self.port_entry.insert(
                    0,
                    "443"
                )

        except Exception:

            pass

    # -----------------------------------------------------

    def save_defaults(self):
        """
        Reserved for future config.json save.
        """

        pass

    # =====================================================
    # Scan Finished
    # =====================================================

    def finish_scan(self):

        #
        # مرتب سازی نتایج
        #

        try:

            self.sort_by_latency()

        except Exception:

            pass

        #
        # نمایش بهترین IP ها
        #

        top10 = self.get_top10()

        self.status_label.configure(

            text=f"Finished - {len(top10)} Best IPs Ready"

        )

        self.update_progress(1.0)

        self.unlock_controls()

    # =====================================================
    # Override Finished Event
    # =====================================================

    def process_finished(self):

        self.finish_scan()

    # =====================================================
    # Application Start
    # =====================================================

    def initialize(self):

        self.load_defaults()

        self.configure_table_tags()

    # =====================================================
    # Debug
    # =====================================================

    def print_top10(self):

        for row in self.get_top10():

            print(row)


#
# End of Class
=======
from __future__ import annotations

from pathlib import Path
from tkinter import ttk
import queue

import customtkinter as ctk

from controller import Controller


class CFIPOptimizerApp(ctk.CTk):

    """
    Main GUI
    """

    def __init__(self, base_path: Path):

        super().__init__()

        self.base_path = Path(base_path)

        self.controller = Controller(self.base_path)

        self.event_queue = queue.Queue()

        self.controller.set_event_callback(
            self.on_controller_event
        )

        ctk.set_appearance_mode("Dark")

        ctk.set_default_color_theme("blue")

        self.title("CF IP Optimizer v2")

        self.geometry("1220x820")

        self.minsize(1150, 760)

        self.protocol(

            "WM_DELETE_WINDOW",

            self.on_close

        )

        self.create_widgets()
		
	self.initialize()

        self.after(

            100,

            self.process_events

        )

    # -----------------------------------------------------

    def create_widgets(self):

        #
        # Title
        #

        self.title_label = ctk.CTkLabel(

            self,

            text="CF IP Optimizer v2",

            font=(

                "Segoe UI",

                30,

                "bold"

            )

        )

        self.title_label.pack(

            pady=(20, 15)

        )

        # --------------------------------------------

        self.input_frame = ctk.CTkFrame(

            self

        )

        self.input_frame.pack(

            fill="x",

            padx=20,

            pady=10

        )

        # --------------------------------------------

        self.domain_entry = ctk.CTkEntry(

            self.input_frame,

            width=420,

            placeholder_text="Domain (SNI)"

        )

        self.domain_entry.grid(

            row=0,

            column=0,

            padx=15,

            pady=20

        )

        # --------------------------------------------

        self.port_entry = ctk.CTkEntry(

            self.input_frame,

            width=120

        )

        self.port_entry.insert(

            0,

            "443"

        )

        self.port_entry.grid(

            row=0,

            column=1,

            padx=10

        )

        # --------------------------------------------

        self.start_button = ctk.CTkButton(

            self.input_frame,

            text="Start Scan",

            width=180,

            command=self.start_scan

        )

        self.start_button.grid(

            row=0,

            column=2,

            padx=10

        )

        # --------------------------------------------

        self.stop_button = ctk.CTkButton(

            self.input_frame,

            text="Stop",

            width=140,

            fg_color="#C0392B",

            hover_color="#922B21",

            command=self.stop_scan

        )

        self.stop_button.grid(

            row=0,

            column=3,

            padx=10

        )

        # --------------------------------------------

        self.import_button = ctk.CTkButton(

            self.input_frame,

            text="Import Config",

            width=160,
			
    command=self.import_config

        )

        self.import_button.grid(

            row=0,

            column=4,

            padx=10

        )

        # --------------------------------------------

        self.generate_button = ctk.CTkButton(

            self.input_frame,

            text="Generate Configs",

            width=180,
			
    command=self.generate_configs

        )

        self.generate_button.grid(

            row=0,

            column=5,

            padx=10

        )

        # --------------------------------------------

        self.progress = ctk.CTkProgressBar(

            self

        )

        self.progress.pack(

            fill="x",

            padx=20,

            pady=(15, 5)

        )

        self.progress.set(0)

        # --------------------------------------------

        self.progress_label = ctk.CTkLabel(

            self,

            text="0 %"

        )

        self.progress_label.pack()

        # --------------------------------------------

        self.info_frame = ctk.CTkFrame(

            self

        )

        self.info_frame.pack(

            fill="x",

            padx=20,

            pady=15

        )

        self.elapsed_label = ctk.CTkLabel(

            self.info_frame,

            text="Elapsed : 00:00"

        )

        self.elapsed_label.pack(

            side="left",

            padx=20

        )

        self.found_label = ctk.CTkLabel(

            self.info_frame,

            text="Found : 0"

        )

        self.found_label.pack(

            side="left",

            padx=20

        )

        self.status_label = ctk.CTkLabel(

            self.info_frame,

            text="Ready"

        )

        self.status_label.pack(

            side="right",

            padx=20

        )
		        # =====================================================
        # Result Table
        # =====================================================

        self.table_frame = ctk.CTkFrame(
            self
        )

        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure(

            "Treeview",

            rowheight=30,

            font=("Segoe UI", 10)

        )

        style.configure(

            "Treeview.Heading",

            font=("Segoe UI", 10, "bold")

        )

        columns = (

            "IP",

            "Latency",

            "Download",

            "Upload",

            "Jitter"

        )

        self.table = ttk.Treeview(

            self.table_frame,

            columns=columns,

            show="headings",

            height=18

        )

        #
        # Headings
        #

        self.table.heading(

            "IP",

            text="IP Address"

        )

        self.table.heading(

            "Latency",

            text="Latency"

        )

        self.table.heading(

            "Download",

            text="Download"

        )

        self.table.heading(

            "Upload",

            text="Upload"

        )

        self.table.heading(

            "Jitter",

            text="Jitter"

        )

        #
        # Columns
        #

        self.table.column(

            "IP",

            width=330,

            anchor="center"

        )

        self.table.column(

            "Latency",

            width=120,

            anchor="center"

        )

        self.table.column(

            "Download",

            width=140,

            anchor="center"

        )

        self.table.column(

            "Upload",

            width=140,

            anchor="center"

        )

        self.table.column(

            "Jitter",

            width=120,

            anchor="center"

        )

        #
        # Scrollbar
        #

        self.scrollbar = ttk.Scrollbar(

            self.table_frame,

            orient="vertical",

            command=self.table.yview

        )

        self.table.configure(

            yscrollcommand=self.scrollbar.set

        )

        self.table.pack(

            side="left",

            fill="both",

            expand=True

        )

        self.scrollbar.pack(

            side="right",

            fill="y"

        )

        #
        # اولین ردیف
        #
		
    self.configure_table_tags()

        self.table.insert(

            "",

            "end",

            values=(
			
                "Waiting for scan...",

                "-",

                "-",

                "-",

                "-"

            )
			
        )
		

    # =========================================================
    # Scan Buttons
    # =========================================================

    def start_scan(self):

        domain = self.domain_entry.get().strip()

        if not domain:

            self.status_label.configure(

                text="Please enter a domain."

            )

            return

        try:

            port = int(

                self.port_entry.get()

            )

        except ValueError:

            self.status_label.configure(

                text="Invalid port."

            )

            return

        #
        # Reset UI
        #

        self.progress.set(0)

        self.progress_label.configure(

            text="0 %"

        )

        self.found_label.configure(

            text="Found : 0"

        )

        self.elapsed_label.configure(

            text="Elapsed : 00:00"

        )

        self.status_label.configure(

            text="Scanning..."

        )

        #
        # پاک کردن جدول
        #

        for item in self.table.get_children():

            self.table.delete(item)

        #
        # شروع اسکن
        #

    self.controller.prepare_scan()
		
    self.lock_controls()

        self.controller.start_scan(

            domain,

            port

        )

    # -----------------------------------------------------

    def stop_scan(self):

        self.controller.stop_scan()

        self.status_label.configure(

            text="Stopped"

        )
		    # =====================================================
    # Controller Events
    # =====================================================

    def on_controller_event(self, event):

    #
    # دیگر کاری لازم نیست.
    # Event داخل Controller وارد Queue شده است.
    #

    pass

    # -----------------------------------------------------

    def process_events(self):

        while not self.event_queue.empty():

            event = self.event_queue.get()

            name = event.get("event")

            data = event.get("data")

            #
            # Scan Started
            #

            if name == "scan_started":

                self.status_label.configure(

                    text="Scanning..."

                )

            #
            # Scan Finished
            #

            elif name == "scan_finished":

                self.process_finished()

            #
            # Scan Stopped
            #

            elif name == "scan_stopped":

                self.status_label.configure(

                    text="Stopped"

                )
				self.unlock_controls()

            #
            # Found Counter
            #

            elif name == "found":

                self.found_label.configure(

                    text=f"Found : {data}"

                )

            #
            # Elapsed Time
            #

            elif name == "elapsed":

                self.elapsed_label.configure(

                    text=f"Elapsed : {data}"

                )

            #
            # New Result
            #

            elif name == "new_result":

                self.add_result(data)

            #
            # Error
            #

            elif name == "error":

                self.status_label.configure(

                    text=str(data)

                )

            #
            # Log
            #

            elif name == "log":

                #
                # بعداً Progress واقعی را
                # از لاگ استخراج می‌کنیم.
                #

                pass

        #
        # keep polling
        #

        self.after(

            100,

            self.process_events

        )

    # =====================================================
    # Result Table
    # =====================================================

    def add_result(

        self,

        result

    ):

        #
        # فعلاً Download / Upload / Jitter
        # توسط cf-knife خروجی نمی‌شوند.
        # بعداً SpeedTest اضافه می‌شود.
        #
		
		tag = self.latency_tag(result.latency)

        self.table.insert(

            "",

            "end",

            values=(

                result.ip,

                f"{result.latency} ms",

                "-",

                "-",

                "-"

            ),
			
			tags=(tag,)

    )
		
    self.update_progress_from_results()

        #
        # همیشه آخرین آیتم دیده شود
        #

        children = self.table.get_children()

        if children:

            self.table.see(

                children[-1]

            )
			    # =====================================================
    # UI Helpers
    # =====================================================

    def clear_table(self):
        """
        Remove all rows from result table.
        """

        for item in self.table.get_children():
            self.table.delete(item)

    # -----------------------------------------------------

    def reset_ui(self):
        """
        Reset GUI to initial state.
        """

        self.clear_table()

        self.progress.set(0)

        self.progress_label.configure(
            text="0 %"
        )

        self.found_label.configure(
            text="Found : 0"
        )

        self.elapsed_label.configure(
            text="Elapsed : 00:00"
        )

        self.status_label.configure(
            text="Ready"
        )

    # -----------------------------------------------------

    def lock_controls(self):
        """
        Disable controls while scanning.
        """

        self.start_button.configure(
            state="disabled"
        )

        self.domain_entry.configure(
            state="disabled"
        )

        self.port_entry.configure(
            state="disabled"
        )

        self.import_button.configure(
            state="disabled"
        )

        self.generate_button.configure(
            state="disabled"
        )

        self.stop_button.configure(
            state="normal"
        )

    # -----------------------------------------------------

    def unlock_controls(self):
        """
        Enable controls after scan.
        """

        self.start_button.configure(
            state="normal"
        )

        self.domain_entry.configure(
            state="normal"
        )

        self.port_entry.configure(
            state="normal"
        )

        self.import_button.configure(
            state="normal"
        )

        self.generate_button.configure(
            state="normal"
        )

        self.stop_button.configure(
            state="normal"
        )

    # =====================================================
    # Future Buttons
    # =====================================================

    def import_config(self):
        """
        Reserved for config import.
        """

        self.status_label.configure(
            text="Import Config (Coming Soon)"
        )

    # -----------------------------------------------------

    def generate_configs(self):
        """
        Reserved for Config Builder.
        """

        self.status_label.configure(
            text="Generate Configs (Coming Soon)"
        )

    # =====================================================
    # Window Events
    # =====================================================

    def on_close(self):
        """
        Close application safely.
        """

        try:

            self.controller.shutdown()

        except Exception:

            pass

        self.destroy()
		    # =====================================================
    # Progress
    # =====================================================

    def update_progress(self, value: float):
        """
        value : 0.0 -> 1.0
        """

        value = max(0.0, min(1.0, value))

        self.progress.set(value)

        self.progress_label.configure(
            text=f"{int(value*100)} %"
        )

    # -----------------------------------------------------

    def update_progress_from_results(self):
        """
        Temporary progress estimation.

        تا زمانی که cf-knife درصد واقعی را
        اعلام نکند از تعداد IPها استفاده می‌کنیم.
        """

        found = self.controller.get_result_count()

        #
        # فعلاً هر 10 IP = 10%
        #

        progress = min(found / 100, 1.0)

        self.update_progress(progress)

    # =====================================================
    # Table Colors
    # =====================================================

    def configure_table_tags(self):

        self.table.tag_configure(

            "excellent",

            background="#1E8449"

        )

        self.table.tag_configure(

            "good",

            background="#21618C"

        )

        self.table.tag_configure(

            "medium",

            background="#9A7D0A"

        )

        self.table.tag_configure(

            "bad",

            background="#922B21"

        )

    # -----------------------------------------------------

    def latency_tag(self, latency):

        if latency <= 50:

            return "excellent"

        if latency <= 120:

            return "good"

        if latency <= 250:

            return "medium"

        return "bad"

    # =====================================================
    # Sorting
    # =====================================================

    def sort_by_latency(self):

        rows = []

        for item in self.table.get_children():

            values = self.table.item(item)["values"]

            try:

                latency = int(

                    str(values[1]).replace(

                        " ms",

                        ""

                    )

                )

            except Exception:

                latency = 9999

            rows.append(

                (

                    latency,

                    values

                )

            )

        rows.sort(

            key=lambda x: x[0]

        )

        self.clear_table()

        for _, values in rows:

            tag = self.latency_tag(

                int(

                    str(values[1]).replace(

                        " ms",

                        ""

                    )

                )

            )

            self.table.insert(

                "",

                "end",

                values=values,

                tags=(tag,)

            )

    # =====================================================
    # Top 10
    # =====================================================

    def get_top10(self):

        rows = []

        for item in self.table.get_children():

            rows.append(

                self.table.item(item)["values"]

            )

        rows.sort(

            key=lambda row:

            int(

                str(row[1]).replace(

                    " ms",

                    ""

                )

            )

        )

        return rows[:10]
		    # =====================================================
    # Settings
    # =====================================================

    def load_defaults(self):
        """
        Load default values when application starts.
        """

        try:

            if not self.domain_entry.get():

                self.domain_entry.insert(
                    0,
                    "cloudflare.com"
                )

            if not self.port_entry.get():

                self.port_entry.insert(
                    0,
                    "443"
                )

        except Exception:

            pass

    # -----------------------------------------------------

    def save_defaults(self):
        """
        Reserved for future config.json save.
        """

        pass

    # =====================================================
    # Scan Finished
    # =====================================================

    def finish_scan(self):

        #
        # مرتب سازی نتایج
        #

        try:

            self.sort_by_latency()

        except Exception:

            pass

        #
        # نمایش بهترین IP ها
        #

        top10 = self.get_top10()

        self.status_label.configure(

            text=f"Finished - {len(top10)} Best IPs Ready"

        )

        self.update_progress(1.0)

        self.unlock_controls()

    # =====================================================
    # Override Finished Event
    # =====================================================

    def process_finished(self):

        self.finish_scan()

    # =====================================================
    # Application Start
    # =====================================================

    def initialize(self):

        self.load_defaults()

        self.configure_table_tags()

    # =====================================================
    # Debug
    # =====================================================

    def print_top10(self):

        for row in self.get_top10():

            print(row)


#
# End of Class
>>>>>>> 79d58fd8555281da2231e29208dea2e51a5e42a2
#