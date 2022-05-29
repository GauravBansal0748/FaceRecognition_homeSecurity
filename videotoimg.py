import cv2
import os
import random
import faceRecognition as fr
import videoTester
import config
import csv

subject = ""  # creating a String variable to Store the new member name
global i
i = random.randint(4, 1000)  # Randomizing the ID to prevent the same id clashes


# functionality of the ADD MEMBER Button
def add_member():
    # function to make new directory for the new MEMBER
    def make_directory():
        j = str(i)
        parent_path = "D:\GitHub\FaceRecognition_homeSecurity/trainingImages/"
        new_path = os.path.join(parent_path, j)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            return new_path
        else:
            make_directory()
            print("directory already there!!")

    cap = cv2.VideoCapture(0)
    count = 0
    new_dir = make_directory()
    if new_dir:
        os.chdir(new_dir)
    # To update the New User Name and Id in the dictionary
    config.name.update({i: subject})
    # Writing the ID name pair to a CSV file
    name_dict = config.name
    name_list = []
    for p in name_dict.keys():
        name_list.append({"Id": p, "Name": name_dict[p]})
    field_names = ["Id", "Name"]
    with open('D:\GitHub\FaceRecognition_homeSecurity/mycsvfile.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(name_list)


    # Creating Image Frames from the LIVE VIDEO
    while True:
        ret, test_img = cap.read()
        if not ret:
            continue
        cv2.imwrite("frame%d.jpg" % count, test_img)  # save frame as JPG file
        count += 1
        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('face detection Window', resized_img)
        if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            break


    cap.release()
    cv2.destroyAllWindows()


def train_model():
    # Comment belows lines when running this program second time.Since it saves training.yml file in directory
    faces, faceID = fr.labels_for_training_data('D:\GitHub\FaceRecognition_homeSecurity/trainingImages')
    face_recognizer = fr.train_classifier(faces, faceID)
    face_recognizer.save('trainingData.yml')

