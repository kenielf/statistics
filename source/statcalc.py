#!/bin/env python
import sys
from interface import *


if __name__ == '__main__':
    args = sys.argv[1:]
    if "-t" in args or "--terminal" in args:
        print("Running as CLI")
        interface = Terminal()
        interface.run()
    elif "-g" in args or "--graphical" in args:
        print("Running as GUI")
        interface = Graphical()
        interface.run()
    elif "-h" in args or "--help" in args:
        help_print()
    elif len(args) == 0:
        print("No interface specified, defaulting to Graphical")
        interface = Graphical()
        interface.run()
    else:
        help_print()
