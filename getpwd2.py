from subprocess import Popen, PIPE, STDOUT
import os
from pynput.keyboard import Key,Controller
import sys
import msvcrt

p = Popen('python getpwd.py', shell=True, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
keyboard = Controller()
keyboard.press('a')
keyboard.release('a')
keyboard.press('m')
keyboard.release('m')
keyboard.press('i')
keyboard.release('i')
keyboard.press('y')
keyboard.release('y')
keyboard.press('a')
keyboard.release('a')
keyboard.press('m')
keyboard.release('m')
keyboard.press('i')
keyboard.release('i')
keyboard.press('y')
keyboard.release('y')
keyboard.press('\n')
keyboard.release('\n')
print p.communicate(input="some value paased through")[0]

pid = p.pid
print pid

orwr = os.O_RDWR
print 'O_RDWR : ' , orwr
# keyboard = Controller()
# keyboard.press('a')
# keyboard.release('a')
# keyboard.press(''
#                '')
# keyboard.release(''
#                  '')

#noctty = os.O_NOCTTY
#print 'os.O_NOCTTY : ', noctty
# stdin = sys.stdin
# print stdin
# if sys.stdin is not sys.__stdin__:
#     print 'hello'

