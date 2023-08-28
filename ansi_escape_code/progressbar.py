#!/usr/bin/env python3
# coding=utf-8

# SPDX-FileCopyrightText: Copyright (c) 2022 Stefan Krüger s-light.eu
#
# SPDX-License-Identifier: MIT
"""
`ansi_escape_code`
================================================================================

simple helper library for common ANSI escape codes

inspired / based on information from
    - https://en.wikipedia.org/wiki/ANSI_escape_code
    - https://www.geeksforgeeks.org/print-colors-python-terminal/


* Author(s): Stefan Krüger

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware
    `>= 7.0.0 for the supported boards. <https://github.com/adafruit/circuitpython/releases>`_
* Python3
* terminal with support for escape codes / sequences
    (tested with `GTKTerm <https://github.com/Jeija/gtkterm>`_)
"""

# pylint: disable=invalid-name, too-few-public-methods

# how to document on class attributes:
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute


import time
import usb_cdc
import ansi_escape_code as terminal


class ProgressBar:
    """
    Show ProgressBar on bottom of screen.

    please make sure your terminal supports control sequences.
    tested with `GTKTerm:
    <https://github.com/Jeija/gtkterm>`_

    and `picocom:
    <https://github.com/npat-efault/picocom>`_


    usage:

    .. code-block:: python

        my_progress = ProgressBar()
        my_progress.update(0.5)
        my_progress.clear()


    range is 0.0 - 1.0

    """

    def __init__(self, *, serial):
        self.serial = serial
        self.terminal_size = (0, 0)
        self.line1 = "progress: {:> 3}%".format(0)
        self.last_abs_pos = 0
        if self.serial.connected:
            self.terminal_size = terminal.get_terminal_size(serial=usb_cdc.console)
            print(self.line1)
            print("_")

    def update(self, progress):
        """update progress bar on bottom of screen."""
        if self.serial.connected:
            print(
                terminal.ANSIControl.cursor.previous_line(2)
                # + terminal.ANSIControl.erase_line()
                + terminal.ANSIControl.cursor.horizontal_absolute(len(self.line1) - 1)
                + "{:> 3}%".format(int(progress * 100))
                + terminal.ANSIControl.cursor.next_line(2),
                end="",
            )
            progress_abs_pos = int(progress * self.terminal_size[1])
            char_repeate = progress_abs_pos - self.last_abs_pos
            print(
                terminal.ANSIControl.cursor.previous_line(1)
                + terminal.ANSIControl.cursor.horizontal_absolute(self.last_abs_pos + 1)
                + "#" * char_repeate
                # + terminal.ANSIControl.erase_line()
                # + "{}".format(progress_char_count * "#")
                + terminal.ANSIControl.cursor.next_line(1),
                end="",
            )
            self.last_abs_pos = progress_abs_pos

    def clear(self):
        """clear progress bar lines."""
        if self.serial.connected:
            print(
                terminal.ANSIControl.cursor.previous_line(2)
                + terminal.ANSIControl.erase_line()
                + terminal.ANSIControl.cursor.next_line(1)
                + terminal.ANSIControl.erase_line(),
                end="",
            )


##########################################
# tests


def map_to_01(x, in_min, in_max):
    """Map value to 0..1 range."""
    return (x - in_min) / (in_max - in_min)


def simulate_progress():
    """draw progress bar to bottom of screen."""
    duration = 20
    my_progress = ProgressBar()

    steps = my_progress.terminal_size[1]
    sleep_duration = duration / steps
    step_size = 1.0 / steps

    for progress_int in range(0, steps):
        progress = map_to_01(progress_int, 0, steps)
        my_progress.update(progress)
        time.sleep(sleep_duration)
    time.sleep(2)
    # my_progress.clear()
    print(2 * "\n")


def run_tests():
    for _i in range(10):
        # print(".", end="")
        print(".", end="")
        time.sleep(0.5 / 10)
    print("")
    print(42 * "*")
    print("progressbar.py")

    running = True
    while running:
        try:
            serial = usb_cdc.console
            if serial.connected:
                simulate_progress()
                time.sleep(2)
                # test_control()
                # time.sleep(2)
        except KeyboardInterrupt as e:
            print("KeyboardInterrupt - Stop Program.", e)
            running = False
        else:
            pass


if __name__ == "__main__":
    import usb_cdc

    run_tests()
