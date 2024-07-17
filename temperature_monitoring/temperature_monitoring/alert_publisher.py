import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertPublisher(Node):
    def __init__(self):
        super().__init__('alert_publisher')
        self.subscription = self.create_subscription(String, 'alert_trigger', self.alert_callback, 10)
        self.alert_publisher = self.create_publisher(String, 'alert', 10)

    def alert_callback(self, msg):
        self.alert_publisher.publish(msg)
        self.get_logger().info(f'Alert message published: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = AlertPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
