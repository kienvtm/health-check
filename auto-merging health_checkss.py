#!/usr/bin/env python3
import os
import sys
import shutil
import socket

''' This line is for making conflict test '''

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists(r"/run/reboot-required")

def check_disk_full(disk, min_gb, min_pct):
     """Returns True if there isn't enough disk space, False otherwise."""
     du = shutil.disk_usage(disk)
     # Calculate the percentage of free space
     percent_free = 100 * du.free / du.total
     # # Calculate how many free gigabytes
     gigabytes_free = du.free / 2**30
     if percent_free < min_pct or gigabytes_free < min_gb:
         return True
     return False

def check_no_network():
    ''' Returns True if it fails to resolve Google's URL, False otherwise'''
    try:
        socket.gethostname('www.google.com')
        return False
    except:
        return True

def check_root_full():
    '''Returns True if the root partition is full, False otherwise.'''
    return check_disk_full(disk='/', min_gb=2, min_pct=10)

def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
        (check_no_network, "No network"),
    ]
    everything_ok = True
    for check, msg in checks:  
        if check():
            print(msg)
            everything_ok=False
            
    if not everything_ok:
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()



