import subprocess
import os
import sys
import time

def run_in_background(script_name):
    script_path = os.path.abspath(script_name)
    subprocess.Popen(['python3', script_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)

def delete_self():
    script_path = os.path.abspath(__file__)
    time.sleep(2)
    if os.path.exists(script_path):
        os.remove(script_path)
        print(f"Deleted self: {script_path}")
if __name__ == "__main__":
    run_in_background('wander2.py')
    delete_self()
