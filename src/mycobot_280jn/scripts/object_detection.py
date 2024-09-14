#!/usr/bin/env python

import rospy
import cv2
import moveit_commander
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class ObjectDetection:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('object_detection_node', anonymous=True)

        # Initialize CvBridge for converting ROS Image messages to OpenCV
        self.bridge = CvBridge()

        # Subscribe to the camera feed
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)

        # Initialize MoveIt commander
        self.move_group = moveit_commander.MoveGroupCommander("arm")

        # Load your object detection model (example with OpenCV or deep learning model)
        # self.model = load_your_model()  # You would load your pre-trained model here

    def image_callback(self, data):
        try:
            # Convert ROS Image message to OpenCV format
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

            # Perform object detection on the image
            # detected_objects = self.model.detect(cv_image)  # Example: Detect objects using your model
            detected_objects = self.simulate_detection(cv_image)  # Simulate detection for testing

            # Process detected objects
            if detected_objects:
                for obj in detected_objects:
                    # Get the object's position (x, y, z)
                    x, y, z = obj["position"]

                    # Move the robot to the detected object
                    self.move_to_object([x, y, z])

            # Optionally, display the camera feed
            cv2.imshow("Object Detection", cv_image)
            cv2.waitKey(1)

        except Exception as e:
            rospy.logerr("Error processing image: %s", str(e))

    def simulate_detection(self, image):
        # Simulate detection by returning a hardcoded position
        detected_object = {
            "position": [0.5, 0.0, 0.2]  # Simulated position
        }
        return [detected_object]

    def move_to_object(self, target_position):
        # Move the robot's arm to the detected object's position using MoveIt
        self.move_group.set_pose_target(target_position)
        success = self.move_group.go(wait=True)

        if success:
            rospy.loginfo("Moved to object successfully!")
        else:
            rospy.logwarn("Failed to move to the object!")

if __name__ == "__main__":
    try:
        # Initialize the object detection node
        obj_det = ObjectDetection()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
