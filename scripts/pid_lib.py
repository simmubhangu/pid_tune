#!/usr/bin/env python
from Tkinter import *
from pid_tune.msg import PidTune
import rospy


class Pid_dim():
	def __init__(self,title,topic_name,queue_size):
		self.pub_pid = rospy.Publisher(topic_name,PidTune,queue_size=queue_size)
		self.pid_params = PidTune()

		self.root = Tk()
		self.root.title(title)
		self.root.attributes("-topmost", True)
		self.root.geometry('250x210') 

		self.scale = Scale(self.root, orient='horizontal', from_=0, to=5000, command = self.set_value, label= 'Kp',width = "20", length = "300",troughcolor="red",sliderlength="15")
		self.scale1 =Scale(self.root, orient='horizontal', from_=0, to=1000, command = self.set_value, label= 'Ki',width = "20", length = "300",troughcolor="green",sliderlength="15")
		self.scale2 =Scale(self.root, orient='horizontal', from_=0, to=5000, command = self.set_value, label= 'Kd',width = "20", length = "300", troughcolor="blue",sliderlength="15")

		self.scale.pack()
		self.scale1.pack()
		self.scale2.pack()
	def set_value(self, event):

		self.pid_params.Kp = self.scale.get()
		self.pid_params.Ki = self.scale1.get()
		self.pid_params.Kd = self.scale2.get()
		self.pub_pid.publish(self.pid_params)

		
