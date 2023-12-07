#!/usr/bin/python3
import cmd

class HBNBconsole(cmd.Cmd):
    prompt = "HBNB$ "
    
    def do_quit(self, arg):
        '''This command to exit from program'''
        return True
    #alias do_quit
    do_exit = do_quit

    def do_EOF(self, arg):
        '''When type CTRL+D to End program'''
        return True


if __name__ == "__main__":
    HBNBconsole().cmdloop()