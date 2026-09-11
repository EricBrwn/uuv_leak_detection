import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class WaterLeakDetector(Node):
	def __init__(self):
		super().__init__('water_leak_detector')

		#Variable de memoria
		self.fugaDetectada = False
		self.contadorPeligro = 0
		self.lecturasCriticas = 3

		#Suscribirse al topico del sensor que ya existe
		self.subscription = self.create_subscription(
			Float32, 
			'/uuv/leak_status',
			self.sensor_callback,
			10)

		#Creacion de Nuevo topico para publicar el resultado procesado
		self.publisher_ = self.create_publisher(String, '/uuv/enclosure_alarm', 10)
		self.get_logger().info('Detector activado. Histeresis con Filtro. Monitoreando el enclosure...')

	def sensor_callback(self, msg):
		humedad = msg.data
		resultado = String()

		if humedad >= 60.0:
			self.contadorPeligro += 1
		elif humedad <= 40.0:
			self.contadorPeligro = 0

		
		if not self.fugaDetectada and self.contadorPeligro >= self.lecturasCriticas:
			#Supero el limite superior, activa alarma
			self.fugaDetectada = True
			self.get_logger().error(f"FUGA CONFIRMADA - Humedad: {humedad}% - Activando alarma")

		elif self.fugaDetectada and humedad <= 40.0:
			#Bajo del limite inferior, desactiva alarma
			self.fugaDetectada = False
			self.get_logger().info(f"Nivel seguro. Humedad: {humedad}% - Sistemas nominales")

		#Publicar el estado
		if self.fugaDetectada:
			resultado.data = f"ALERTA CRITICA, INUNDACION EN ENCLOSURE! Humedad: {humedad}%"
		else:
			resultado.data = f"Enclosure seguro y presurizado - Humedad: {humedad}%"

		self.publisher_.publish(resultado)

def main(args=None):
	rclpy.init(args=args)
	node = WaterLeakDetector()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()

