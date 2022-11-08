# Original work Copyright (c) 2022 Sky360
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import os
import yaml
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('sentinel_launch'),
        'config',
        'params.yaml'
    )

    #with open(config, 'r') as f:
    #    configuration = yaml.safe_load(f)
    #    print(f'Loaded configuration: {configuration}')

    #ros2 launch sentinel_launch sentinel_launch.py

    return LaunchDescription([
        #Node(
        #    package='camera_simulator',
        #    ##namespace='sky360',
        #    executable='camera_simulator',
        #    #parameters = [config],
        #    name='camera_simulator',
        #    arguments={
        #        '--type ':'video',
        #        '--path ':'"/workspaces/sentinel-ros2-ws/src/sentinel_launch/videos/brad_drone_1.mp4"',
        #        '--loop ':''
        #    }.items()
        #),
        Node(
            package='usb_cam',
            ##namespace='sky360',
            executable='usb_cam_node_exe',
            parameters = [config],
            name='usb_cam',
        ),
        Node(
            package='usb_cam',
            ##namespace='sky360',
            executable='show_image.py',
            name='usb_cam_show_image',
        ),           
    ])
