import time
import speech_recognition as sr

m = sr.Microphone()
r = sr.Recognizer()

with m as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Say something!")
  audio = r.listen(source)

try:
	print("Sphinx thinks you said: "+r.recognize_sphinx(audio))
except sr.UnknownValueError:
	print("Sphinx could not understand audio")
except sr.RequestError as e:
	print("Sphinx error; {0}".format(e))

