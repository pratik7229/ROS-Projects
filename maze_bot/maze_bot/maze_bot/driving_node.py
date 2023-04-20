import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    
    rclpy.spin(minimal_publisher)
    rclpy.shutdown()


if __name__ == '__main__':
    main()