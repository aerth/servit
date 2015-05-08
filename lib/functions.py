from os import system
import curses
#global get_param
#global get_params
#global launch_cmd
#global execute_cmd

def get_param(prompt_string):
     screen = curses.initscr()
     screen.clear()
     screen.border(0)
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     screen.addstr(1,2, "EARTHBOT SERVIT", curses.A_STANDOUT)
     input = screen.getstr(10, 10, 600)
     return input


def get_params(prompt_string,second_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 10, prompt_string)
     screen.addstr(4, 10, second_string)
     screen.refresh()
     screen.addstr(1,2, "EARTHBOT SERVIT", curses.A_STANDOUT)
     input = screen.getstr(10, 10, 60)
     return input


def execute_cmd(cmd_string):
     system("reset")
     a = system( cmd_string )
     
     if a == 0:
          print "Command executed correctly"
          
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     #system("reset") 
def launch_cmd(cmd_string):
     system("reset")
     a = system( cmd_string )
     print ""
     if a == 0:
          print "Command executed correctly"
          
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     #x = ord('q')
     #print ""
     #system("reset") 