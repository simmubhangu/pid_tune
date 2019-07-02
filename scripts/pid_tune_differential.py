#!/usr/bin/env python
import rospy
import time
from pid_lib import *

if __name__ == '__main__':

	rospy.init_node('Tune_pid_differential')
	lwheel_ui = rospy.get_param('~lpid_ui_enable',True) #set it as True if you need left_wheel ui
	rwheel_ui = rospy.get_param('~rpid_ui_enable',True)

	if lwheel_ui and rwheel_ui:
		lpid = Pid_dim("Left_wheel","lpid_params",1000) #Title of the ui, topic name of the publisher, queue size
		rpid = Pid_dim("Right_wheel","rpid_params",1000)
		lpid.root.mainloop()
	elif lwheel_ui:
		lpid = Pid_dim("Left_wheel","lpid_params",1000)
		lpid.root.mainloop()
	elif rwheel_ui:
		rpid = Pid_dim("Right_wheel","rpid_params",1000)
		rpid.root.mainloop()
	else:
		rospy.loginfo("UI DISABLED")