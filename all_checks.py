#!/usr/bin/env python3
import os
import sys
import pandas as pd

''' This line is for making conflict test ''''

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists(r"/run/reboot-required")


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Evertying ok.")
    sys.exit(0)



main()
