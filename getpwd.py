import time
import os
import sys
import msvcrt
orwr = os.O_RDWR
print 'O_RDWR : ' , orwr
#noctty = os.O_NOCTTY
#print 'os.O_NOCTTY : ', noctty
# stdin = sys.stdin
# print stdin
# if sys.stdin is not sys.__stdin__:
#     print 'hello'
def win_getpass(prompt='Password: ', stream=None):
    """Prompt for password with echo off, using Windows getch()."""
    if sys.stdin is not sys.__stdin__:
        print 'hei'

    for c in prompt:
        msvcrt.putch(c)
    pw = ""
    while 1:
        c = msvcrt.getwch()
        # print c
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            pw = pw[:-1]
            # print pw
        else:
            pw = pw + c
            # print pw
    msvcrt.putch('\r')
    msvcrt.putch('\n')
    return pw

pwd = win_getpass(prompt='Password3  : \n',stream=None)
time.sleep(40)
print 'You entered:', pwd

