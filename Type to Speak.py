#! /usr/bin/python

import pyttsx3

class App:
	def __init__(self):
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices')	# get voices
		rate = self.engine.getProperty('rate')
		self.SpeakingSpeed = rate-35
		self.engine.setProperty('rate', self.SpeakingSpeed)		# change speach rate
		self.RunApp = True
		print("""
- Enter text below.  Type Quit or Q to end.  Type Male or Female to switch voice. - 
          - Type 'Speed +5' or 'Speed -5' to change the Speaking speed. -""")
		self.Run()
	
	def Run(self):
		while self.RunApp is True:
			ReadMe = input(" ---> ")
			if ReadMe.lower().strip() in ('quit', "q"):
				self.RunApp = False
				return
			elif ReadMe.lower().strip() in ('male', 'guy', 'man'):
				print("Changed voice to Male.")
				self.engine.setProperty('voice', self.voices[0].id)
			elif ReadMe.lower().strip() in ('female', 'girl', 'woman'):
				print("Changed voice to Female.")
				self.engine.setProperty('voice', self.voices[1].id)
			elif ReadMe.lower().strip() in ('speed+ 5','speed+5','speed +5', 'speed + 5'):
				print("Increasing Speaking Speed.")
				self.SpeakingSpeed = self.SpeakingSpeed+5
				self.engine.setProperty('rate', self.SpeakingSpeed)
			elif ReadMe.lower().strip() in ('speed- 5','speed-5','speed -5', 'speed - 5'):
				print("Decreasing Speaking Speed.")
				self.SpeakingSpeed = self.SpeakingSpeed-5
				self.engine.setProperty('rate', self.SpeakingSpeed)
			else:
				self.engine.say(ReadMe)
				self.engine.runAndWait()

if __name__ == '__main__':
	try:
		a = App()
	except Exception:
		logging.critical('Error')
	finally:
		quit()