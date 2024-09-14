cmake_minimum_required(VERSION 3.0.2)
project(mycobot_280jn)
add_compile_options(-std=c++11)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  actionlib
  image_transport
  cv_bridge
)

## Find OpenCV for image processing
find_package(OpenCV REQUIRED)

## Declare a catkin package
catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs actionlib image_transport cv_bridge
)

## Include directories
include_directories(include ${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS})

## Install Python scripts
catkin_install_python(PROGRAMS
  scripts/follow_display.py
  scripts/slider_control.py
  scripts/teleop_keyboard.py
  scripts/listen_real.py
  scripts/listen_real_of_topic.py
  scripts/slider_control_gripper.py
  scripts/simple_gui.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Install launch and config directories
install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
