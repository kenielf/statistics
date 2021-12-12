#!/bin/env python
import sys
import platform


if __name__ == '__main__':
    args = sys.argv[1:]
    # Check OS
    if platform.system() == "Linux":
        import interface_lin as ui
    elif platform.system() == "Windows":
        import interface_win as ui
    # Run
    if "-t" in args or "--terminal" in args:
        print("Running as CLI")
        interface = ui.Terminal()
        interface.run()
    elif "-g" in args or "--graphical" in args:
        print("Running as GUI")
        interface = ui.Graphical()
        interface.run()
    elif "-h" in args or "--help" in args:
        ui.help_print()
    elif len(args) == 0:
        print("No interface specified, defaulting to Graphical")
        interface = ui.Graphical()
        interface.run()
    else:
        ui.help_print()
