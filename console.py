#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel

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
            print(' Input the class name! ')
            return
        elif arg not in HBNBconsole.classnames:
            print(' Class name not exist! ')
            return
        new_inst = eval(arg)()
        storage.save()
        print(new_inst.id)
    
    def help_create(self):
        '''Documentation for create help command'''
        print('[Usage]: create <classname> to create a class')
    


if __name__ == '__main__':
    HBNBconsole().cmdloop()