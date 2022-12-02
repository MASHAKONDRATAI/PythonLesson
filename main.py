 # print('Hello world')
from random import *
class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 50
		self.progress = 0
		self.alive = True
	def say_hello(self):
		print('Hello!')
  def to_own_bissnes(self):
		print('Time to self-development')
		if self.progress < 10:
			self.gladness -= 4
		self.progress += 7
		self.gladness -= 1
	def to_study(self):
		print('Time to study')
		if self.progress < 5:
			self.gladness -= 4
		self.progress += 2
		self.gladness -= 1
    def to_girlfriend(self):
		print('Time for you and your girlfriend')
		if self.progress < 5:
			self.gladness -= 20
		self.progress += 4
		self.gladness -= 0
	def to_sleep(self):
		print('Time to sleep')
		self.gladness += 2
	def to_chill(self):
		print('Rest time')
		self.gladness += 5
		self.progress -= 2
	def statics(self):
		print('Gladness: ', self.gladness, 'Progress: ',self.progress)
	def live(self, day):
		day = "Day " + str(day) + " of " + self.name + " life"
		print(day)
		live_cube = randint(1,4)
		if live_cube == 1:
			self.to_study()
		elif live_cube == 2:
			self.to_sleep()
		elif live_cube == 3:
			self.to_chill()
		elif live_cube == 4:
			self.say_hello()
		self.statics()
		self.is_alive()

sanya = Student('Vanya')
for day in range(365):
	if vanya.alive == False:
		break
	vanya.live(day)

Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
