<<<<<<< HEAD
"""
CF IP Optimizer v2
main.py

Application entry point.

Responsibilities:
- Initialize the application.
- Load configuration.
- Create the main window.
- Start the GUI event loop.

This file intentionally contains no business logic.
"""

from pathlib import Path
import sys

from gui import CFIPOptimizerApp


def get_base_path() -> Path:
    """
    Returns the application base path.

    Compatible with:
        - Python execution
        - PyInstaller (--onefile)
    """
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS"))

    return Path(__file__).resolve().parent


def main() -> None:
    """
    Application entry point.
    """
    base_path = get_base_path()

    app = CFIPOptimizerApp(
        base_path=base_path
    )

    app.mainloop()


if __name__ == "__main__":
=======
"""
CF IP Optimizer v2
main.py

Application entry point.

Responsibilities:
- Initialize the application.
- Load configuration.
- Create the main window.
- Start the GUI event loop.

This file intentionally contains no business logic.
"""

from pathlib import Path
import sys

from gui import CFIPOptimizerApp


def get_base_path() -> Path:
    """
    Returns the application base path.

    Compatible with:
        - Python execution
        - PyInstaller (--onefile)
    """
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS"))

    return Path(__file__).resolve().parent


def main() -> None:
    """
    Application entry point.
    """
    base_path = get_base_path()

    app = CFIPOptimizerApp(
        base_path=base_path
    )

    app.mainloop()


if __name__ == "__main__":
>>>>>>> 79d58fd8555281da2231e29208dea2e51a5e42a2
    main()