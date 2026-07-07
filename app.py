from tkinter import ttk
from resultreader import ResultReader

import customtkinter as ctk
import threading
import time

from scanner import Scanner
from parser import Parser

scanner = Scanner()
parser = Parser()
reader = ResultReader()


def run():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.geometry("950x700")

    app.title("CF IP Optimizer")

    title = ctk.CTkLabel(

        app,

        text="CF IP Optimizer",

        font=("Segoe UI",28,"bold")

    )

    title.pack(pady=20)

    domain = ctk.CTkEntry(

        app,

        width=500,

        placeholder_text="Domain"

    )

    domain.insert(

        0,

        "cloudflare.com"

    )

    domain.pack(pady=8)

    port = ctk.CTkEntry(

        app,

        width=120

    )

    port.insert(

        0,

        "443"

    )

    port.pack()

    status = ctk.CTkLabel(

        app,

        text="Ready"

    )

    status.pack(pady=10)

    progress = ctk.CTkProgressBar(

        app,

        width=700

    )

    progress.pack()

    progress.set(0)

    percent = ctk.CTkLabel(

        app,

        text="0 %"

    )

    percent.pack()

    info = ctk.CTkFrame(app)

    info.pack(pady=15)

    scanned = ctk.CTkLabel(

        info,

        text="Scanned : 0"

    )

    scanned.grid(row=0,column=0,padx=20)

    found = ctk.CTkLabel(

        info,

        text="Found : 0"

    )

    found.grid(row=0,column=1,padx=20)

    elapsed = ctk.CTkLabel(

        info,

        text="Elapsed : 00:00"

    )

    elapsed.grid(row=0,column=2,padx=20)
        # ---------- Result Table ----------

    table = ttk.Treeview(
        app,
        columns=("IP","Ping","Download","Upload","Jitter"),
        show="headings",
        height=12
    )

    table.heading("IP", text="IP")
    table.heading("Ping", text="Ping")
    table.heading("Download", text="Download")
    table.heading("Upload", text="Upload")
    table.heading("Jitter", text="Jitter")

    table.column("IP", width=260, anchor="center")
    table.column("Ping", width=80, anchor="center")
    table.column("Download", width=100, anchor="center")
    table.column("Upload", width=100, anchor="center")
    table.column("Jitter", width=80, anchor="center")

    table.pack(fill="both", expand=True, padx=20, pady=15)

    start_time=0

    running=False

    def timer():

        if running:

            s=int(time.time()-start_time)

            m=s//60

            s=s%60

            elapsed.configure(

                text=f"Elapsed : {m:02}:{s:02}"

            )

            app.after(

                1000,

                timer

            )

    def callback(line):

        data=parser.parse(line)

        if data["total"]:

            progress.set(

                data["scanned"]/data["total"]

            )

            percent.configure(

                text=f'{int(data["scanned"]/data["total"]*100)} %'

            )

        scanned.configure(

            text=f'Scanned : {data["scanned"]}'

        )

        found.configure(

            text=f'Found : {data["found"]}'

        )

        def start():

        nonlocal running, start_time

        running = True

        start_time = time.time()

        timer()

        status.configure(text="Scanning...")

        progress.set(0)

        percent.configure(text="0 %")

        table.delete(*table.get_children())

        def worker():

            scanner.start(
                domain.get(),
                port.get(),
                callback
            )

            rows = reader.load()

            def update():

                nonlocal running

                running = False

                status.configure(text="Finished")

                table.delete(*table.get_children())

                for row in rows[:10]:

                    table.insert(
                        "",
                        "end",
                        values=(
                            row["ip"],
                            row["latency"],
                            row["download"],
                            row["upload"],
                            row["jitter"]
                        )
                    )

            app.after(0, update)

        threading.Thread(
            target=worker,
            daemon=True
        ).start()
        
        button = ctk.CTkButton(
    app,
    text="Start Scan",
    command=start,
    width=220,
    height=40
)

button.pack(pady=20)

app.mainloop()