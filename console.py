#!/usr/bin/python3
import cmd
import sys
from models.base_model  import BaseModel
from models import storage


class HBNBconsole(cmd.Cmd):
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    
    classnames = ['BaseModel', 'User', 'State', 'City', 'Place', 'Review', 'Amenity']

    def do_quit(self, arg):
        '''This command to exit from program'''
        return True
    #alias do_quit
    do_exit = do_quit

    def help_quit(self):
        '''Documentation for quit help command'''
        print('This command to to exit from the app\n')

    def do_EOF(self, arg):
        '''Handle EOF to End program'''
        print() # emtpy line before exit
        return True
    
    def help_EOF(self, arg):
        '''Documentation for EOF help command'''
        print('Exit program when type CTRL+D')
    
    def emptyline(self):
        '''empty input line'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of classes, saves it, and prints the id'''
        if not arg:
            print('** class name missing **')
            return
        elif arg not in HBNBconsole.classnames:
            print("** class doesn't exist **")
            return
        new_inst = eval(arg)()
        storage.save()
        print(new_inst.id)
    
    def help_create(self):
        '''Documentation for create help command'''
        print('[Usage]: create <classname> to create a class')

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name"""
        if not arg:
            print("** class name missing **")
            return
        
        str_rep = arg.split()
        if len(str_rep) < 2:  # missing id
            print("** instance id missing **")
            return
        elif str_rep[0] not in HBNBconsole.classnames:
            print("** class doesn't exist **")
            return
        key = str_rep[0] + "." + str_rep[1]
        if key in storage.all():
            obj = storage.all()[key]
            print(obj)
        else:
            print("** no instance found **")
    
    def help_show(self):
        '''Documentation for show help command'''
        print('[Usage]: show <classname> <id>\n')
    
    def do_destroy(self, arg):
        '''Delete instance by classname and id'''
        if not arg:
            print('** class name missing **')
            return
        str_rep = arg.split()
        if len(str_rep) < 2:  # missing id
            print("** instance id missing **")
            return
        elif str_rep[0] not in HBNBconsole.classnames:
            print("** class doesn't exist **")
            return

        key = str_rep[0] + "." + str_rep[1]
        if key in storage.all():
            obj = storage.all()[key]
            del obj
            storage.save()
        else:
            print("** no instance found **")
        
    def help_destroy(self):
        '''Documentation for destroy help command'''
        print('[Usage]: destroy <classname> <id>\n')
    
    def do_all(self, arg):
        ''''''
        pass
    
    def help_all(self):
        pass

    def do_update(self, arg):
        pass

    def help_update(self):
        pass

if __name__ == '__main__':
    HBNBconsole().cmdloop()

