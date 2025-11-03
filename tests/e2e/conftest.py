# tests/e2e/conftest.py
import os
import subprocess
import time
import requests
import pytest

def _wait_for(url="http://127.0.0.1:8000", timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url)
            if r.status_code in (200, 404):
                return
        except Exception:
            pass
        time.sleep(0.2)
    raise RuntimeError("Server did not start")

@pytest.fixture(scope="session")
def fastapi_server():
    # make sure coverage picks up code in the server process
    # requires a .coveragerc at repo root with [run] parallel = True, source = app
    env = os.environ.copy()
    env["COVERAGE_FILE"] = ".coverage.e2e"   # keep data separate
    cmd = [
        "python", "-m", "coverage", "run", "-p", "-m",
        "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"
    ]
    proc = subprocess.Popen(cmd, env=env)
    try:
        _wait_for()
        yield
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
