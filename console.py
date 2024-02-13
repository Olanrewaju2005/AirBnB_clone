#!/usr/bin/python3

"""
Imports the cmd module to handle command line
arguments
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of he command intepreter
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name = eval(args[0])
            new_inst = class_name()
            new_inst.save()
            print(new_inst.id)

    def emptyline(self):
        """
        Does nothing if no command is entered and goes to the next line
        """
        pass

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        objects = storage.all()
	args = shlex.split(arg)

        if len(args) == 0:
            for key, value in objects.items():
                print(str(value))
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(".")[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
	args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objects[key]

                attr_name = args[0]
                attr_value = args[1]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass

                setattr(obj, attr_name, attr_value)

                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
