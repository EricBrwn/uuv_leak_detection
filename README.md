# UUV Water Leak Detection System

#Descripcion
Este paquete de ROS 2 Humble implementa un sistema de deteccion de intrusion de agua para un UUV.
Consta de un nodo emisor que simula las lecturas del sensor y un nodo receptor que procesa la informacion y emite alertas de seguridad.

## Requisitos
* Ubuntu 22.04 LTS
*ROS 2 Humble
* Python 3.10

## Compilacion
Desde la raiz de workspace:

cd ~/ros2_ws
colcon build --packages-select uuv_leak_detection
source install/setup.bash


## Ejecucion
Se requieren dos terminales con el entrono activado

Terminal 1 (Sensor):
'ros2 run uuv_leak_detection leak_sensor_node'

Terminal 2 (Detector):
'ros2 run uuv_leak_detection water_leak_detector'


