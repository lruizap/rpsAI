# Rock-Paper-Scissors AI  

Este proyecto implementa un modelo de inteligencia artificial que utiliza visión por computadora para reconocer gestos de manos y diferenciar entre piedra, papel o tijera. El objetivo es construir una aplicación interactiva que permita a los usuarios jugar al clásico juego contra la IA.  

## Características  

- **Detección de manos:** El modelo utiliza técnicas avanzadas de visión por computadora para identificar la mano en tiempo real.  
- **Clasificación de gestos:** Reconoce los tres gestos principales del juego (piedra, papel y tijera).  
- **Modelo entrenado:** Emplea aprendizaje automático para garantizar un rendimiento preciso y consistente.  
- **Interactividad:** El modelo puede integrarse con una cámara para una experiencia dinámica.  

## Requisitos  

- Python 3.8+  
- Librerías principales:  
  - TensorFlow o PyTorch (según el modelo)  
  - OpenCV  
  - Pandas  
  - Ultralytics
  - PIL
  - Matplotlib
  - Torch

## Instalación  

1. Clona este repositorio:  

   ```bash  
   git clone https://github.com/lruizap/rpsAI.git  
   cd rpsAI  
   ```  

2. Instala las dependencias:  

   ```bash  
   pip install -r requirements.txt  
   ```  

3. Descarga el dataset desde el enlace mencionado en los readme adicionales

  url: https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw/dataset/14

## Uso  

1. Asegúrate de tener una cámara conectada y configurada.  
2. Ejecuta el script principal:  

   ```bash  
   python ./scripts/rpsAI.py  
   ```  

3. Sigue las instrucciones en pantalla para jugar.  

## Estructura del proyecto  

- `datasets/`: Directorio para almacenar los datos utilizados para entrenar el modelo.  
- `models/`: Modelos entrenados y archivos relacionados.  

## Contribuciones  

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, no dudes en abrir un _issue_ o enviar un _pull request_.  
