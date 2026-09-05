import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, String

class WaterLeakDetector(Node):
	def __init__(self):
		super().__init__('water_leak_detector')

		#Suscribirse al topico del sensor que ya existe
		self.subscription = self.create_subscription(
			Bool, 
			'/uuv/leak_status',
			self.sensor_callback,
			10)

		#Creacion de Nuevo topico para publicar el resultado procesado
		self.publisher_ = self.create_publisher(String, '/uuv/enclosure_alarm', 10)
		self.get_logger().info('Detector central activado. Monitoreando el enclosure...')

	def sensor_callback(self, msg):

		# Recibe la medicion, determina el estado y lo publica
		resultado = String()

		if msg.data == True:
			resultado.data = "ALERTA CRITICA, INUNDACION EN EL ENCLOSURE"
			self.get_logger().error('FUGA CONFIRMADA, ACTIVANDO ALARMA')
		else:
			resultado.data = "Enclosure seguro y presurizado"
			self.get_logger().info('Sistemas nominales')

		self.publisher_.publish(resultado)

def main(args=None):
	rclpy.init(args=args)
	node = WaterLeakDetector()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()

