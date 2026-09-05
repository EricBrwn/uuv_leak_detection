import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class LeakSensorNode(Node):
	def __init__(self):
		super().__init__('leak_sensor_node')
		#Publicador que enviara el estado en el topico /uuv/leak_status
		self.publisher_ = self.create_publisher(Bool, '/uuv/leak_status', 10)
		# Evalua el estado del sensor cada 1.0 seg
		self.timer = self.create_timer(1.0, self.check_leak_sensor)
		self.get_logger().info('Nodo del Sensor de Fugas inicializado correctamente')

	def check_leak_sensor(self):
		msg = Bool()
		# Simulacion: False = Compartimento seco | True = Fuga detectada
		msg.data = False
		self.publisher_.publish(msg)
		self.get_logger().info(f'Estado publicado en /uuv/leak_status: {"ALERTA DE FUGA" if msg.data else "Seco"}')

def main(args=None):
	rclpy.init(args=args)
	node = LeakSensorNode()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()

