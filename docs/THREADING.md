# Threading

The application uses four worker threads.

---

GUI Thread

Responsible for:

Widgets

Buttons

Table

Progress

Logs

Never blocked.

---

Scanner Thread

Responsible for:

Launching cf-knife

Reading stdout

Stopping process

Nothing else.

---

Reader Thread

Responsible for:

Watching result files

Reading appended lines

Sending lines to Parser

---

Timer Thread

Responsible for:

Elapsed Time

Progress Timer

---

Rules

Never update GUI outside GUI Thread.

Never parse inside Scanner.

Never read files inside GUI.

Never block Controller.

Use callbacks.

Use events.

Keep worker threads independent.

---

Future Threads

Benchmark Thread

Speed Test Thread

Export Thread

Plugin Thread

History Thread