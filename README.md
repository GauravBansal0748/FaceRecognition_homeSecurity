# FaceRecognition_homeSecurity
 Microsoft Engage'22 Project Submission
# Home Security using Face Recognition

To tackle the problem of home theft, a Home security application can be developed using the Face Recognition technology which uses an unique identification factor and allow entry-exit using the same.
## Authors

- [@GauravBansal0748](https://github.com/GauravBansal0748)
## Prerequisites
- Python 3.8
- NumPy
- Pandas
- OpenCV
- Visual Studio
- Face Recognition
## Installation

Install following libraries using pip to run the project.  
- OpenCV
cmd
pip install opencv-python

Note: Please install opencv-contrib-python package instead of opencv-contrib as it contains the main modules and also contrib modules.

- Face Recognition
cmd
pip install dlib
pip install cmake
pip install face-recognition

Note: Make sure you have installed Visual Studio in your system/machine.
    
- Pandas
cmd
pip install pandas


- NumPy
cmd
pip install numpy
# Documentation
## Home Security Using Face Recognition
The Home Security is a desktop application designed to used for Home security via face recognition. This is the Admin panel of the Home security application prototype.
## How to run the App
1.	Just clone the repository and open the Folder Home Security
2.	Install all the dependencies mentioned below
3.	Now, double click the Window.py to run the Desktop Application.
4.	A new window will open (called Home Security), enter your NAME and hit the SUBMIT button.
5.	After Submit, a new window will open (called Home Security Main), this is the Admin Panel, where the Admin has two Features: i) To Add a new Face/Member ii)To Scan already registered Face.
## How to add a Family member/Face
If Admin is registering for the First time, he/she has to register their Face first, Click the ADD MEMBER button, a new window will appear called Face Detection, scan your face for 2-3 minutes, and then press ‘q’ key to quit the process. 

It will then train the Classifier with the newly add data. Once done close the window. (New Face added)
## How to Scan Face
Now, for registered user can directly scan their faces using SCAN FACE button, on Clicking the scan face button a face recognition window will open, which will recognize the user.

If User got matched/verified, it will Display “User Authenticated” and greets user with “Hello”+username of the user, if not recognize it will display User “Unknown User”.

To quit the face recognition window, Long press ‘q’, to stop the program, then close the windows as usual.
## Dependencies
-	Python 3.8
-	Numpy
-	Pandas
-	OpenCV
-	Visual Studio
-	Face Rcognition
- CSV
## What the App looks Like

![Home Security First PageScreenShot](https://user-images.githubusercontent.com/85233894/170864389-6c9201fe-9ba0-4a9c-8880-1189836f2ef5.png)

![Home Security Main ScreenShot](https://user-images.githubusercontent.com/85233894/170864445-b9745870-a7dd-4189-ab33-61a0a7eeb8bd.png)
## Youtube Live Demo
https://youtu.be/zKmwxZ80tcU
## Acknowledgements

- [How to use Tkinter](https://codemy.com/)
- [How to design ui](https://www.youtube.com/watch?v=_lSNIrR1nZU)
- [About opencv and face recognition](https://www.superdatascience.com/blogs/opencv-face-recognition)
- [Object detection with Haar Cascades](https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/)
