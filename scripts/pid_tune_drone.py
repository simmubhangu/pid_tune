#!/usr/bin/env python
import rospy
import time
from pid_lib import *

if __name__ == '__main__':

	rospy.init_node('Tune_pid_drone')
	pitch_ui = rospy.get_param('~ppid_ui_enable',True) #set it as True if you need pitch pid ui
	roll_ui = rospy.get_param('~rpid_ui_enable',True)
	yaw_ui = rospy.get_param('~ypid_ui_enable',True)
	throttle_ui = rospy.get_param('~tpid_ui_enable',True)

	if pitch_ui and roll_ui and yaw_ui and throttle_ui :
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		ppid.root.mainloop()

	elif pitch_ui and roll_ui and yaw_ui:
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		ppid.root.mainloop()

	elif pitch_ui and roll_ui and throttle_ui:
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		ppid.root.mainloop()

	elif pitch_ui and yaw_ui and throttle_ui:
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		ppid.root.mainloop()

	elif roll_ui and yaw_ui and throttle_ui:
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)#Title of the ui, topic name of the publisher, queue size
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		rpid.root.mainloop()

	elif pitch_ui and roll_ui:
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)
		ppid.root.mainloop()

	elif pitch_ui and yaw_ui:
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		ppid.root.mainloop()

	elif pitch_ui and yaw_ui:
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		ppid.root.mainloop()

	elif roll_ui and yaw_ui:
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		rpid.root.mainloop()

	elif roll_ui and throttle_ui:
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		rpid.root.mainloop()

	elif yaw_ui and throttle_ui:
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		ypid.root.mainloop()

	elif pitch_ui:
		ppid = Pid_dim("Pitch","pid_tuning_pitch",1000) #Title of the ui, topic name of the publisher, queue size
		ppid.root.mainloop()

	elif roll_ui:
		rpid = Pid_dim("Roll","pid_tuning_roll",1000)
		rpid.root.mainloop()

	elif yaw_ui:
		ypid = Pid_dim("Yaw","pid_tuning_yaw",1000)
		ypid.root.mainloop()

	elif throttle_ui:
		tpid = Pid_dim("Throttle","pid_tuning_altitude",1000)
		tpid.root.mainloop()

	else:
		rospy.loginfo("UI DISABLED")

