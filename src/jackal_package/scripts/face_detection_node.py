#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
import cv2
import dlib

#def face_detector():
	#face detection algorithm

	#yes_or_no=1

	#pub.publish(1)


#def callback_received_camera_img():
	#pub.publish()



if __name__=="__main__":
	rospy.init_node("face_detection_node")
	rospy.loginfo("face_detection_started")

	pub=rospy.Publisher("/detectedornot", Int64, queue_size=10)
	

	camera = cv2.VideoCapture(0)
	detector = dlib.get_frontal_face_detector()

	#rate=rospy.Rate(2)
	while not rospy.is_shutdown():
		ret, image =  camera.read()
		if not ret:
			break

		image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
		
		faces =detector(image,1)
		
		if faces:		
			pub.publish(1)
		#sub=rospy.Subscriber("/camera_img", Int64, face_detector)
		else:
			pub.publish(2)

		cv2.imshow("image", image)
		key=cv2.waitKey(1) & 0xFF
		if key==ord("q"):
			break		
		


		#rate.sleep()
	camera.release()
	cv.destroyAllWindows()
	#################################
	#rospy.spin()		
	

	


