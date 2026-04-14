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

    # Updated function priority list
    functions = [
        "main_apv",   # ✅ তোমার main function
        "main",
        "run",
        "start",
        "start_checking",
        "menu"
    ]

    for func in functions:
        if hasattr(tool, func):
            print(f"[+] Running: tool.{func}()")
            getattr(tool, func)()
            break
    else:
        print("[!] No runnable function found!")

except ImportError as e:
    print("[-] Module load failed!")
    print(e)

except Exception as e:
    print("[-] Runtime error:")
    print(e)
