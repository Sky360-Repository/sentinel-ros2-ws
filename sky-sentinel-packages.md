https://index.ros.org/p/usb_cam/ --> https://github.com/ros-drivers/usb_cam
https://index.ros.org/p/vision_opencv/
https://index.ros.org/p/image_geometry/
https://index.ros.org/p/cv_bridge/
https://index.ros.org/p/v4l2_camera/


https://github.com/NVIDIA-ISAAC-ROS

https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection
https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_proximity_segmentation
https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam


https://jeffzzq.medium.com/ros2-image-pipeline-tutorial-3b18903e7329
https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
https://github.com/ros-perception/image_pipeline/tree/humble



ros2 launch usb_cam demo_launch.py
ros2 run usb_cam usb_cam_node_exe

ros2 run image_view image_view --ros-args --remap /image:=/image_raw
ros2 run image_rotate image_rotate --ros-args --remap /image:=/image_raw
ros2 run image_view image_view --ros-args --remap /image:=/rotated/image

ros2 run camera_calibration cameracalibrator --size=8x6 --square=0.063 --approximate=0.3 --no-service-check --ros-args --remap /image:=/image_raw

ros2 pkg executables
ros2 topic list

ros2 topic echo --no-arr /image_raw

