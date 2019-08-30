
### Requirement for this package
1. tkinter python library. 

    ```python
    sudo apt-get install python python-tk
    ```
[For more information visit here](http://www.greenteapress.com/thinkpython/swampy/install.html)

### How to use This package
1. Import the msg in your script. 
    ```python
    from pid_tune.msg import PidTune
    ```
2. Write the subscriber in the code. 
  ```python
   rospy.Subscriber('/pid_tuning', PidTune, self.set_pid_value )
  ```
3. Get the Value and change the Gain values.
  ```python
   def set_pid_value(self,data):
		self.kp_x = data.Kp 
		self.kp_y = data.Kp 
		self.kp_z = data.Kp
		
		self.kd_x =  data.Kd
		self.kd_y =  data.Kd
		self.kd_z = data.Kd
		
		self.ki_x = data.Ki
		self.ki_y = data.Ki
		self.ki_z = data.Ki
  ```

### Package information for tuning drone

#### Publications:
**/$pid_params** *(pid_tune/PidTune)* <br />

$ denotes corresponding letter for the pid. eg: ppid_params for pitch pid parameters

### launch the ros node by the following command
+ For differential drive robot, you can run the following node
  ```
   roslaunch pid_tune pid_tune_diff.launch
  ```
+ For drone, you can run the following node

  ```
   roslaunch pid_tune pid_tune_drone.launch
  ```
### Run the ros node by the following command
+ For differential drive robot, you can run the following node
  ```
   rosrun pid_tune pid_tune_differential.py
  ```
+ For drone, you can run the following node

  ```
   rosrun pid_tune pid_tune_drone.py
  ```

