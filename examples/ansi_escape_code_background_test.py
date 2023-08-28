# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: Unlicense

import random
import time
import ansi_escape_code as terminal

color = [
    terminal.ANSIColors.fg.black,
    terminal.ANSIColors.fg.red,
    terminal.ANSIColors.fg.green,
    terminal.ANSIColors.fg.orange,
    terminal.ANSIColors.fg.blue,
    terminal.ANSIColors.fg.purple,
    terminal.ANSIColors.fg.cyan,
    terminal.ANSIColors.fg.lightgrey,
    terminal.ANSIColors.fg.darkgrey,
    terminal.ANSIColors.fg.lightred,
    terminal.ANSIColors.fg.lightgreen,
    terminal.ANSIColors.fg.yellow,
    terminal.ANSIColors.fg.lightblue,
    terminal.ANSIColors.fg.pink,
    terminal.ANSIColors.fg.lightcyan,
]

background = [
    terminal.ANSIColors.bg.black,
    terminal.ANSIColors.bg.red,
    terminal.ANSIColors.bg.green,
    terminal.ANSIColors.bg.orange,
    terminal.ANSIColors.bg.blue,
    terminal.ANSIColors.bg.purple,
    terminal.ANSIColors.bg.cyan,
    terminal.ANSIColors.bg.lightgrey,
]

while True:
    """Test colors."""
    test_string = (
        random.choice(background)
        + random.choice(color)
        + "Hello "
        + random.choice(color)
        + "World "
        + random.choice(color)
        + ":-)"
        + terminal.ANSIColors.reset
    )
    print(test_string)
    time.sleep(2)
