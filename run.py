#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import subprocess

# 64-bit check
if '64' not in os.uname().machine:
    sys.exit("[-] Only 64-bit device supported!")

# Auto update
try:
    subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Load module
try:
    import tool
    print("[+] tool loaded!")

    functions = [
        "main_apv",
        "start_account_creation",
        "main",
        "run",
        "start"
    ]

    for func in functions:
        if hasattr(tool, func):
            print(f"[+] Running: tool.{func}()")
            getattr(tool, func)()
            break
    else:
        print("[!] No runnable function found!")
        print("Available:", [f for f in dir(tool) if not f.startswith("_")])

except Exception as e:
    print("[-] Error:", e)
