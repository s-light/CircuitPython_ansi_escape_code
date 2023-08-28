#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: Copyright (c) 2022 Stefan Krüger for s-light
#
# SPDX-License-Identifier: Unlicense

import sys
import time
import usb_cdc
from ansi_escape_code.progressbar import ProgressBar


##########################################
# help


def map_to_01(x, in_min, in_max):
    """Map value to 0..1 range."""
    return (x - in_min) / (in_max - in_min)


##########################################
#


def simulate_progress():
    """draw progress bar to bottom of screen."""
    duration = 20
    my_progress = ProgressBar()

    steps = my_progress.terminal_size[1]
    sleep_duration = duration / steps

    for progress_int in range(0, steps):
        progress = map_to_01(progress_int, 0, steps)
        my_progress.update(progress)
        time.sleep(sleep_duration)
    time.sleep(2)
    # my_progress.clear()
    print(2 * "\n")


##########################################
# main


def main():
    """Main."""
    print("")
    print(42 * "*")
    print("ansi_escape_code__progress.py")
    print("Python Version: " + sys.version)
    print(42 * "*")
    print("run")

    running = True
    while running:
        try:
            serial = usb_cdc.console
            if serial.connected:
                simulate_progress()
                time.sleep(2)
        except KeyboardInterrupt as e:
            print("KeyboardInterrupt - Stop Program.", e)
            running = False
        else:
            pass


##########################################
if __name__ == "__main__":
    main()

##########################################
