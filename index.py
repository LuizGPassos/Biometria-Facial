import cv2
import numpy as np
import mediapipe as mp

#Cria camera virtual
camera = cv2.VideoCapture(0)
#Cria reconhecedor de rosto
reconhecedor = mp.solutions.face_detection.FaceDetection()
#Desenha os pontos no rosto
desenhador = mp.solutions.drawing_utils

while True:
    #Lê a imagem da camera e processa
    frame, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = reconhecedor.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    #Mostra o resultado
    if resultados.detections:
        for deteccao in resultados.detections:
            desenhador.draw_detection(frame, deteccao)

    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break