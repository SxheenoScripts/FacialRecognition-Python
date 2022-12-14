import cv2
import face_recognition as fr
import os
import numpy as np

faces_path = r"C:\Users\khali\Desktop\Javascripts\imgs"

def get_faces_encoding():

    face_names = os.listdir(f"{faces_path}")
    face_encodings = []


    for i, name in enumerate(face_names):
        face = fr.load_image_file(f"{faces_path}\\{name}")
        face_encodings.append(fr.face_encodings(face)[0])




        face_names[i] = name.split(".")[0]

    return face_encodings, face_names



face_encodings, face_names = get_faces_encoding()                                


video = cv2.VideoCapture(0)

sc1 = 2

while True:
    success, image =  video.read()

    resized_image = cv2.resize(image, (int(image.shape[1]/sc1), int(image.shape[0]/sc1)))


    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)


    face_locations = fr.face_locations(rgb_image)
    unknown_encodings= fr.face_encodings(rgb_image, face_locations)

    for face_encoding, face_locations in zip(unknown_encodings, face_locations):

        result = fr.compare_faces(face_encodings, face_encoding, 0.6)

        if True in result:
            name = face_names[result.index(True)]


            top, right , bottom, left = face_locations

            cv2.rectangle(image, (left * sc1, top * sc1), (right * sc1, bottom*sc1), (0,0,255), 2)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2. putText(image, name, (left*sc1, bottom*sc1 + 20), font, 0.8, (255,255,255), 1)


    cv2.imshow("frame", image)
    cv2.waitKey(1)




