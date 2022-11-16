{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Everything ok\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "0",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 0\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python3\n",
    "\n",
    "import shutil\n",
    "import sys\n",
    "\n",
    "def check_disk_usage(disk, min_absolute, min_percent):\n",
    "    #Returns True if there is enough free disk space, false otherwise.\"**\n",
    "    du = shutil.disk_usage(disk)\n",
    "    # Calculate the percentage of free space\n",
    "    percent_free = 100 * du.free / du.total\n",
    "    # Calculate how many free gigabytes\n",
    "    gigabytes_free = du.free / 2**30\n",
    "    if percent_free < min_percent or gigabytes_free < min_absolute:\n",
    "        return False\n",
    "    return True\n",
    "# Check for at least 2 GB and 10% free\n",
    "if not check_disk_usage(\"/\", 2, 10):\n",
    "    print(\"ERROR: Not enough disk space.\")\n",
    "    sys.exit(1)\n",
    "\n",
    "print(\"Everything ok\")\n",
    "sys.exit(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.4 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "c21bf4946d8129f87ef48fa30684c756d196c26a47730ca6e4cf7f2ef4ff0328"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
