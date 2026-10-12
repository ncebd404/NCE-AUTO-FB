#!/data/data/com.termux/files/usr/bin/python3
#_________|NCE AUTO FACEBOOK CREATOR — LAUNCHER|_________#

import os
import sys
import subprocess

# ── Architecture check (64-bit only) ──
if '64' not in os.uname().machine:
    sys.exit("[-] Only 64-bit devices supported!")

# ── Silent auto-update from GitHub ──
try:
    subprocess.run(
        ["git", "pull"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=15
    )
except Exception:
    pass  # no internet or not a git repo → skip silently

# ── Load the tool module (.so first, then .py fallback) ──
try:
    import tool

    # Preferred public entry point
    if hasattr(tool, "start_tool"):
        tool.start_tool()

    # Fallback for older versions
    elif hasattr(tool, "main_apv") and hasattr(tool, "poco"):
        tool.main_apv()
        tool.poco()

    else:
        print("[!] No runnable entry point found in 'tool' module.")
        print("    Available:", [f for f in dir(tool) if not f.startswith("_")])
        sys.exit(1)

except ModuleNotFoundError:
    print("[-] 'tool' module not found!")
    print("    → Make sure tool.py or tool.*.so is in the same folder.")
    print("    → Try: git pull")
    sys.exit(1)

except ImportError as e:
    print(f"[-] Import error: {e}")
    print("    → Python version may not match the .so file.")
    print("    → Delete tool.*.so and re-run to use tool.py instead.")
    sys.exit(1)

except KeyboardInterrupt:
    print("\n\n  ✦ Goodbye!\n")
    sys.exit(0)

except Exception as e:
    print(f"[-] Unexpected error: {e}")
    sys.exit(1)
