import os
import cv2
import numpy as np
import faceRecognition as fr
import pyttsx3  # python text to speech
import config
import csv


# Function to Update the NAME dictionary which contains ID NAME pair
def update_name(i, subject):
    config.name.update({i: subject})

# Function called when SCAN FACE Button is pressed and name entered is already a registered user
def scan_image():
    # Text to Speech Commands
    k = pyttsx3.init()
    sound = k.getProperty('voices')
    k.setProperty('voice', sound[0].id)
    k.setProperty('rate', 130)
    k.setProperty('pitch', 200)

    def speak(text):
        k.say(text)
        k.runAndWait()

    # This module captures images via webcam and performs face recognition
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainingData.yml')  # Load saved training data

    cap = cv2.VideoCapture(0)

    Flag = 1
    while True:
        ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
        faces_detected, gray_img = fr.faceDetection(test_img)

        # detecting Face and enclosing the face in BOX
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 0), thickness=7)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('face detection Window', resized_img)
        cv2.waitKey(10)

        # Recognizing the Detected Face
        # Flag Variable to Greet User if Identified only Once
        for face in faces_detected:
            (x, y, w, h) = face
            roi_gray = gray_img[y:y + w, x:x + h]
            label, confidence_value = face_recognizer.predict(roi_gray)  # predicting the label of given image
            print("confidence_value:", confidence_value)
            print("label:", label)
            fr.draw_rect(test_img, face)
            name_dict = config.name
            try:
                predicted_name = name_dict[label]
            except KeyError:
                print("No Username data found!! Reregister your Face")
            if confidence_value < 45:  # If confidence less than 45 then don't print predicted face text on screen
                # fr.put_text(test_img,predicted_name,x,y)
                try:
                    fr.put_text(test_img, predicted_name, x + 6, y + h - 6)
                except Exception:
                    print("No Username data found!! Reregister your Face")
                cv2.putText(test_img, "User Authenticated", (250, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)
                if Flag:
                    try:
                        speak("Hello" + predicted_name)  # Speak function to Speak the Greet the Identified User
                    except UnboundLocalError:
                        print("No Username data found!! Reregister your Face")
                    Flag = 0
            else:
                # speak("Face not found")
                cv2.putText(test_img, "Unknown Face", (250, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('face recognition Window', resized_img)
        if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            break

    cap.release()
    cv2.destroyAllWindows()
