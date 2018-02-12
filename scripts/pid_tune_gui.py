#!/usr/bin/env python
from Tkinter import *
from pid_tune.msg import PidTune
import rospy

rospy.init_node('tune_pid')
send_pid = rospy.Publisher('/pid_tuning', PidTune, queue_size=10)
pid_value = PidTune()
def set_value():
  pid_value.Kp = scale.get()
  pid_value.Ki = scale1.get()
  pid_value.Kd = scale2.get()
  # pid_value.Kp_z = scale3.get()
  send_pid.publish(pid_value)
  # print scale.get(), scale1.get(), scale2.get()

root = Tk()

scale = Scale(root, orient='horizontal', from_=0, to=300, label= 'Kp',width = "50", length = "500",troughcolor="red")
scale1 =Scale(root, orient='horizontal', from_=0, to=1000, label= 'Ki',width = "50", length = "500",troughcolor="green")
scale2 =Scale(root, orient='horizontal', from_=0, to=100, label= 'Kd',width = "50", length = "500", troughcolor="blue")
# scale3 =Scale(root, orient='horizontal', from_=0, to=300, label= 'Kp_z',width = "50", length = "500", troughcolor="gray")
scale.pack()
scale1.pack()
scale2.pack()
# scale3.pack()

Button(root, text='set_value', command=set_value).pack()

root.mainloop()