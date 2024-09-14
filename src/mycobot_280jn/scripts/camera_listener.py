#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraListener:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('camera_listener', anonymous=True)

        # Initialize CvBridge for converting ROS Image messages to OpenCV
        self.bridge = CvBridge()

        # Subscribe to the camera's image topic
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)

    def image_callback(self, data):
        try:
            # Convert the ROS Image message to OpenCV format
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

            # Display the camera feed
            cv2.imshow("Camera Feed", cv_image)
            cv2.waitKey(1)

        except Exception as e:
            rospy.logerr("Error processing image: %s", str(e))

if __name__ == '__main__':
    try:
        listener = CameraListener()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
