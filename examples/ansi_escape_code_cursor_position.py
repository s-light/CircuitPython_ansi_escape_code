#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: Copyright (c) 2022 Stefan Krüger for s-light
#
# SPDX-License-Identifier: Unlicense

"""Test Cursor Movement."""

import time
import sys
import board
import usb_cdc
import ansi_escape_code as terminal

##########################################
# globals


def run_example():
    serial = usb_cdc.console
    print("get_terminal_size:")
    row, col = terminal.get_terminal_size(serial=serial)
    print("row: {}; col: {}".format(row, col))
    print("wait 2s")
    time.sleep(2)


##########################################
# main


def main():
    """Main."""
    # wait some time untill the computer / terminal is ready
    for _i in range(10):
        # print(".", end="")
        print(".", end="")
        time.sleep(0.5 / 10)
    print("")
    print(42 * "*")
    print("ansi_escape_code__cursor_position_test.py")
    print("Python Version: " + sys.version)
    print("board: " + board.board_id)
    print(42 * "*")
    print("run")

    running = True
    while running:
        try:
            serial = usb_cdc.console
            if serial.connected:
                run_example()
        except KeyboardInterrupt as e:
            print("KeyboardInterrupt - Stop Program.", e)
            running = False
        else:
            pass


##########################################
if __name__ == "__main__":
    main()

##########################################
