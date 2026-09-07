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


## Ejecución
Se requieren dos terminales. En CADA UNA debes cargar el entorno antes de ejecutar:

**Terminal 1 (Sensor):**
```
cd ~/ros2_ws
source install/setup.bash
ros2 run uuv_leak_detection leak_sensor_node
```

**Terminal 2 (Detector):**
```
cd ~/ros2_ws
source install/setup.bash
ros2 run uuv_leak_detection water_leak_detector
```

## Verificación de Tópicos (Debugging)
Para inspeccionar la información que viaja entre los nodos en tiempo real, puedes abrir una tercera terminal y sintonizar los tópicos:

Para ver los datos crudos del sensor (True/False):
`ros2 topic echo /uuv/leak_status`

Para ver las alertas procesadas por el detector (String):
`ros2 topic echo /uuv/enclosure_alarm`
