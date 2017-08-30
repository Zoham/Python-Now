import win32com.client as wincl
import sys
import os
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Happy Birthday To You")
