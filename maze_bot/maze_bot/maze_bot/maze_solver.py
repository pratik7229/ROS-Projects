import rclpy
import cv2
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import os

class Video_get(Node):
    def __init__(self):
        super().__init__('video_subscriber')
        self.subscriber = self.create_subscription(Image, '/upper_camera/image_raw', self.get_video_feed_cb, 10)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.maze_solving)
        self.bridge = CvBridge()

    
    def get_video_feed_cb(self, data):
        frame = self.bridge.imgmsg_to_cv2(data,'bgr8') 
        cv2.imshow('outpur', frame)
        cv2.waitKey(1)
    
    def maze_solving(self):
        msg = Twist()
        msg.linear.x = 0.3
        msg.angular.z = 0.5

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = Video_get()
    rclpy.spin(image_subscriber)
    rclpy.shutdown()


if __name__ == '__main__':
    main()