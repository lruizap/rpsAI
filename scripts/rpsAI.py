import cv2

from ultralytics import YOLO


def real_time_detection(model_path, confidence_threshold=0.5, source=0):
    """
    Procesa un flujo de video en tiempo real y muestra predicciones de YOLO.

    Args:
        model_path (str): Ruta al modelo YOLO entrenado (.pt).
        confidence_threshold (float): Umbral de confianza para las detecciones.
        source (int or str): Fuente del video (0 para webcam, o ruta a archivo de video).
    """
    # Cargar el modelo YOLO
    model = YOLO(model_path)

    # Inicializar captura de video
    # 0 es la cámara por defecto; también puede ser una ruta a un archivo de video
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("No se pudo abrir la cámara o el archivo de video.")
        return

    # Obtener las dimensiones del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Resolución del video: {width}x{height}")

    # Procesar fotogramas en tiempo real
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el fotograma del video. Finalizando...")
            break

        # Realizar predicciones con YOLO
        results = model.predict(
            frame, conf=confidence_threshold, device=0, stream=False)

        # Dibujar los cuadros delimitadores y etiquetas en el fotograma
        for result in results:
            for box in result.boxes:
                # Obtener coordenadas del cuadro y etiqueta
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                confidence = box.conf[0].item()
                label = result.names[box.cls[0].item()]

                # Dibujar el cuadro delimitador
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Dibujar el texto (etiqueta y confianza)
                text = f"{label} {confidence:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Mostrar el fotograma con las predicciones
        cv2.imshow("YOLO Real-Time Detection", frame)

        # Salir al presionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Saliendo...")
            break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()


real_time_detection("./models/best.pt")
