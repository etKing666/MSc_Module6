"""
The command prompt for the application.

Imports:
    from cmd: Cmd

Classes:
    Prompt

Functions:
    do_basic()
    do_intermediate()
    do_exit()
    main()
"""

from cmd import Cmd
from cocomo import calc_cocomo
from fpoints import calc_fpoints

class Prompt(Cmd):
    """A class for command prompt.

    Functions
    _________
    do_function (self, inp): Function that corresponds to a CLI command, which is
    "function" in this case.
    'help' is a  built-in function of Prompt() class which displays the documentation of a function.

    Note
    ____
    The CLI continues to run until a function returns True.

    """
    def do_cocomo(self,inp):
        """Makes the basic COCOMO calculation."""
        calc_cocomo()
        return

    def do_fpoint(self, inp):
        """Makes the Function Points calculation."""
        calc_fpoints()
        return

    def do_exit(self, inp):
        """Exists the shell"""
        print("Thanks for using the Project Cost Calculator. Bye!")
        return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.


def main():
    """Provides a CLI menu explaining the available commands"""
    print("\n" + 94 * "=" + "\n" + 41 * " " + "PROJECT COST CALCULATOR\n" + 94 * "=")
    print("""Commands:
cocomo - Makes a basic COCOMO calculation
fpoint - Makes a Function Points calculation
help - Get help and review the documentation of a command (usage: help command)
exit - Exits the application
""")

main()
Prompt().cmdloop()