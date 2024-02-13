#!/usr/bin/python3

"""

"""
import cmd

class HBNBCommand(cmd.Cmd):
    """

    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
            this command exits the commanmd intepreter
        """
        return True


    def do_EOF(self, arg):
        """
        """
        print()
        return True

    def do_create(self, arg):
        """

        """
        pass

    def empty_line(self):
        """
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
