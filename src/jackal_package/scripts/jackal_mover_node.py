#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int64


#####################################################################
def move(yes_or_no):
	vel_msg = Twist()
        
	#speed = 1
        #distance = 6
        #isForward = 1

	######################################################
        #while not rospy.is_shutdown():
	if (yes_or_no.data ==1):
		vel_msg.linear.x = 1	#Since we are moving just in x-axis
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0

	   
		#Setting the current time for distance calculus
		#t0 = rospy.Time.now().to_sec()
		#current_distance = 0

	  	#Loop to move the turtle in an specified distance
		pub.publish(vel_msg)
		
		###############################################
		#while(current_distance < distance):
		        ##Publish the velocity

		        #pub.publish(vel_msg)

		        ##Takes actual time to velocity calculus

		        #t1=rospy.Time.now().to_sec()

		        ##Calculates distancePoseStamped

		        #current_distance= speed*(t1-t0)
		##############################################



	else:
		vel_msg.linear.x = 0
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0

		pub.publish(vel_msg)


################################################################
if __name__=="__main__":
	rospy.init_node("jackal_mover_node")
	#pub=rospy.Publisher("/jackal_velocity_controller/cmd_vel", Twist, queue_size=10)
	pub=rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
	#while not rospy.is_shutdown():
	sub=rospy.Subscriber("/detectedornot", Int64, move)
	
	rospy.spin()	
