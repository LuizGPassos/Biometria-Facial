from concurrent.futures import process
import face_recognition as fr
import cv2
import numpy as np


def biometria():
    camera = cv2.VideoCapture(0)

    fotoLuiz = fr.load_image_file("Images/Luiz.png")
    encLuiz = fr.face_encodings(fotoLuiz)[0]
    fotoObama = fr.load_image_file("Images/Barack_Obama.jpg")
    encObama = fr.face_encodings(fotoObama)[0]
    fotoPedro = fr.load_image_file("Images/Pedro_Henrique.png")
    encPedro = fr.face_encodings(fotoPedro)[0]

    encRostosAprendidos = [encLuiz, encObama, encPedro]
    nomeRostosAprendidos = ["Luiz", "Obama", "Pedro"]

    locRostos = []
    encRostos = []
    nomeRostos = []
    processar = True

    while True:
        ret, frame = camera.read()
        if processar:
            rgbFrame = frame[:, :, ::-1]
            locRostos = fr.face_locations(rgbFrame)
            encRostos = fr.face_encodings(rgbFrame, locRostos)

            for encRosto in encRostos:
                compara = fr.compare_faces(encRostosAprendidos, encRosto)
                nome = "Desconhecido"

                disRostos = fr.face_distance(encRostosAprendidos, encRosto)
                melhorIndice = np.argmin(disRostos)
                if compara[melhorIndice]:
                    nome = nomeRostosAprendidos[melhorIndice]

                nomeRostos.append(nome)
            
            
            

        for (top, right, bottom, left), nome in zip(locRostos, nomeRostos):
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        cv2.imshow("Video", frame)

        if nome == "Luiz":
            print('Acesso Admin Permitido')
        elif nome == "Obama":
            print('Acesso Editor Permitido')
        elif nome == "Pedro":
            print('Acesso Usuario Permitido')
        else:
            print('Acesso Negado')

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        

    camera.release()
    cv2.destroyAllWindows()

biometria()