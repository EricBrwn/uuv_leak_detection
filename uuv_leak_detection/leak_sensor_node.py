import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class LeakSensorNode(Node):
	def __init__(self):
		super().__init__('leak_sensor_node')
		self.publisher_ = self.create_publisher(Float32, '/uuv/leak_status', 10)
		self.timer = self.create_timer(1.0, self.check_leak_sensor)
		self.get_logger().info('Nodo del Sensor de Fugas inicializado correctamente')

	def check_leak_sensor(self):
		msg = Float32()
		#Valor por defecto, se sobreescribira en las pruebas
		msg.data = 20.0
		self.publisher_.publish(msg)

def main(args=None):
	rclpy.init(args=args)
	node = LeakSensorNode()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()

