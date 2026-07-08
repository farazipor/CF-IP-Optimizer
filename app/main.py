from pathlib import Path
import sys

from gui import CFIPOptimizerApp


def get_base_path() -> Path:
    """
    Returns project root.

    Works for:

    - Python
    - PyInstaller
    """

    if getattr(sys, "frozen", False):

        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parent.parent


def main():

    base_path = get_base_path()

    app = CFIPOptimizerApp(
        base_path=base_path
    )

    app.mainloop()


if __name__ == "__main__":

    main()