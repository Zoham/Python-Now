import speech_recognition as sr
import os

def speak(message):
	say = "mshta"
	say = say + " vbscript:Execute(\"CreateObject(\"\"SAPI.SpVoice\"\")"
	say = say + ".Speak(\"\"" + message + "\"\")(window.close)\")"
	os.system(say)

# Set up Engine ---------------------------------------------------
r = sr.Recognizer()

with sr.Microphone() as source:
    # Start Input ---------------------------------------------------
    while (True):
        print "Suppressing Noise"
        r.adjust_for_ambient_noise(source, duration=3)
        
        print "Say Something"
        audio = r.listen(source)

        # Process Audio ---------------------------------------------------
        try:
            out = r.recognize_google(audio)
            os.system(out)
            print "Captured It! - " + out

            speak(out)
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

print "Exiting"
