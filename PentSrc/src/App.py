
#!/usr/bin/env python

#imports
import eel
from function import *

# Useful when packaging Penty into an exe, since --noconsole in pyinstaller returns an error for some reason.
def hideConsole():
  whnd = ctypes.windll.kernel32.GetConsoleWindow()
  if whnd != 0:
     ctypes.windll.user32.ShowWindow(whnd, 0)
hideConsole()


eel.init('web') # Initialize the 'web' folder where frontend and js is stored.

# The logic that connects it with the user io.
@eel.expose
def mainBackend(userinput):
  global userinputglobal
  userinputglobal = userinput.lower()
  #functions
  try:
    if "download speed" in userinputglobal[0:14] or "download" in userinputglobal[0:8]:
      return downloadcheck()
    elif "joke" in userinputglobal[0:4] or "say joke" in userinputglobal[0:8] or "say a joke" in userinputglobal[0:10]:
      return sayJoke()
    elif 'eval' in userinputglobal[0:4] or 'evaluate' in userinputglobal[0:8]:
      return complexMath(userinputglobal)
    elif "about" in userinputglobal[0:6] or "abt" in userinputglobal[0:4]:
      return about()
    elif "upload speed" in userinputglobal[0:13] or "upload" in userinputglobal[0:6]:
      return uploadcheck()
    elif "restart" in userinputglobal[0:7] or "restrt" in userinputglobal[0:6]:
      return restrt()
    elif "remind" in userinputglobal[0:6] or "set reminder" in userinputglobal[0:12] or "reminder" in userinputglobal[0:8]:
      return reminder()
    elif "ip" in userinputglobal[0:2] or "ip address" in userinputglobal[0:10]:
      return ipaddress()
    elif "mac" in userinputglobal[0:3] or "mac address" in userinputglobal[0:11]:
      return macaddress()
    elif 'system' in userinputglobal:
      return platforminfo()
    else:
        try:
          return wlfrm(userinputglobal)
        except:
          return wikiped(userinputglobal)
  except:
    return "Something went wrong.."

eel.start('main.html', size = (471, 220))
