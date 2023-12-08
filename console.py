#!/usr/bin/python3
import cmd

class HBNBconsole(cmd.Cmd):
    prompt = "(hbnb) "
    
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
        """empty input line"""
        pass


if __name__ == "__main__":
    HBNBconsole().cmdloop()