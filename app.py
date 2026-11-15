"""Startup used by the S2I run script.

The Python builder executes this with `python app.py`, so the file does not
need the executable bit. A shell script uploaded from Windows loses that bit
and fails with "Permission denied".
"""

import os
import subprocess
import sys


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.check_call([sys.executable, "manage.py", "migrate", "--noinput"])
    subprocess.check_call([sys.executable, "manage.py", "collectstatic", "--noinput"])
    subprocess.check_call([sys.executable, "manage.py", "ensure_admin"])

    port = os.environ.get("PORT", "8000")
    workers = os.environ.get("WEB_CONCURRENCY", "2")
    timeout = os.environ.get("GUNICORN_TIMEOUT", "120")
    os.execvp(
        "gunicorn",
        [
            "gunicorn",
            "config.wsgi:application",
            "--bind", f"0.0.0.0:{port}",
            "--workers", workers,
            "--timeout", timeout,
            "--access-logfile", "-",
            "--error-logfile", "-",
        ],
    )


if __name__ == "__main__":
    main()
