#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import subprocess

# Check 64-bit
if '64' not in os.uname().machine:
    print("[-] Only 64-bit supported!")
    sys.exit(1)

# Auto update (safe)
try:
    subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Run module
try:
    import tool

    if hasattr(tool, "main"):
        tool.main()
    elif hasattr(tool, "run"):
        tool.run()
    elif hasattr(tool, "start_checking"):
        tool.start_checking()
    else:
        print("No valid entry function found!")

except ImportError:
    print("[-] tool module not found!")
    print("Make sure .so file matches Python version")