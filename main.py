#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun mini bounty entry.

Writes the one-line roast to /output/entry.txt.
Bounty: https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda
"""

import os

ROAST = "I asked my agent for one short answer; it gave me a project plan, a cron job, and a todo list."

def main():
    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)

if __name__ == "__main__":
    main()
