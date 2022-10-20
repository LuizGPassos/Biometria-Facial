import cv2
import face_recognition as fr

imgLuiz = fr.load_image_file('Images/Luiz.png')
imgLuiz = cv2.cvtColor(imgLuiz, cv2.COLOR_BGR2RGB)
imgObama = fr.load_image_file('Images/Barack_Obama.jpg')
imgObama = cv2.cvtColor(imgObama, cv2.COLOR_BGR2RGB)
imgPedro = fr.load_image_file('Images/Pedro_Henrique.png')
imgPedro = cv2.cvtColor(imgPedro, cv2.COLOR_BGR2RGB)

imgTest = fr.load_image_file('Images/testeLuiz.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

rostoObama = fr.face_locations(imgObama)[0]
rostoPedro = fr.face_locations(imgPedro)[0]
rostoLuiz = fr.face_locations(imgLuiz)[0]
rostoTeste = fr.face_locations(imgTest)[0]

encodeLuiz = fr.face_encodings(imgLuiz)[0]
encodeTeste = fr.face_encodings(imgTest)[0]
encodePedro = fr.face_encodings(imgPedro)[0]
encodeObama = fr.face_encodings(imgObama)[0]

compararLuiz = fr.compare_faces([encodeObama], encodeTeste)
print(compararLuiz)

cv2.rectangle(imgLuiz, (rostoLuiz[3], rostoLuiz[0]), (rostoLuiz[1], rostoLuiz[2]), (255, 0, 255), 2)
cv2.imshow('Luiz', imgLuiz)
cv2.rectangle(imgTest, (rostoTeste[3], rostoTeste[0]), (rostoTeste[1], rostoTeste[2]), (255, 0, 255), 2)
cv2.imshow('Teste', imgTest)
cv2.waitKey(0)
