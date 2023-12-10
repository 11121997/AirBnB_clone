#!/usr/bin/python3
"""modules for console"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class for Console Commands"""
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ''

    classnames = {
        "User": User,
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_EOF(self, arg):
        """Handle EOF to End program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty input line\n"""
        return False

    def do_create(self, arg):
        """Creates a new instance of classes, saves it, and prints the id\n"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classnames:
            print("** class doesn't exist **")
            return
        new_inst = eval(arg)()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name\n"""
        if not arg:
            print("** class name missing **")
            return

        str_rep = arg.split()
        if len(str_rep) < 2:  # missing id
            print("** instance id missing **")
            return
        elif str_rep[0] not in HBNBCommand.classnames:
            print("** class doesn't exist **")
            return
        dic = storage.all()
        key = f"{str_rep[0]}.{str_rep[1]}"
        if key in dic:
            print(dic[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete instance by classname and id\n"""
        if not arg:
            print("** class name missing **")
            return
        str_rep = arg.split()
        if len(str_rep) < 2:  # missing id
            print("** instance id missing **")
            return
        elif str_rep[0] not in HBNBCommand.classnames:
            print("** class doesn't exist **")
            return

        key = str_rep[0] + "." + str_rep[1]
        if key in storage.all():
            obj = storage.all()[key]
            del obj
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the class name\n"""
        N_dict = storage.all()
        A_list = []
        for k in N_dict.values():
            A_list.append(str(k))
        if arg:
            if arg not in HBNBCommand.classnames:
                print("** class doesn't exist **")
            else:
                B_list = []
                for key, val in N_dict.items():
                    if arg in key:
                        B_list.append(str(val))
                print(B_list)
        else:
            print(A_list)

    def do_update(self, arg):
        """Updates an instance by class name and id.\n"""
        str_rep = arg.split()
        if not str_rep:
            print("** class name missing **")
            return
        cls_name = str_rep[0]

        if cls_name not in HBNBCommand.classnames:
            print("** class doesn't exist **")
            return

        if len(str_rep) < 2:
            print("** instance id missing **")
            return
        cls_id = str_rep[1]

        key = "{}.{}".format(cls_name, cls_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(str_rep) < 3:
            print("** attribute name missing **")
            return
        attr_name = str_rep[2]

        if len(str_rep) < 4:
            print("** value missing **")
            return
        attr_val = str_rep[3]

        inst = storage.all()[key]
        setattr(inst, attr_name, eval(attr_val))
        # saves after updates
        inst.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
