cmake_minimum_required(VERSION 3.0.2)
project(yolo_object_detection)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  cv_bridge
)

## Declare a catkin package
catkin_package()

## Specify additional locations of header files
include_directories(${catkin_INCLUDE_DIRS})

## Install Python scripts (like detect_objects.py)
catkin_install_python(PROGRAMS
  scripts/detect_objects.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
