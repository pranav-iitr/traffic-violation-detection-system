# Inter IIT Tech Meet 12.0 Engineering Conclave 

## Problem Statement

#### To create a deep-learning-based system to detect and store information on traffic violators in a database hosted on a website to collect proof and number plates of the criminals simultaneously.

## Mentors

### [Pranjal Mangal](https://github.com/mangalpranjal)
### [Maanas Verma](https://github.com/Maanas-Verma)

## Contributors 


### [Riya Jindal](https://github.com/riyaaaa123)
### [Ishika Arya](https://github.com/I-shika)
### [Rishika Pilania](https://github.com/rishu-3619)
### [Pranav Arya](https://github.com/pranav-iitr)
<br/>

## Technology used

<img align="left" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" style="padding-right:10px;" />
<img align="left"  width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original-wordmark.svg" style="padding-right:10px;" />
<img align="left"  width="35px" src="https://cdn.analyticsvidhya.com/wp-content/uploads/2018/12/yologo_2-850x451.png"  />
<br/>
<br/>

###

# Approach

#### 1) Learn different Computer Vision and Deep Learning models

#### 2) As Yolo was chosen for the project, do an in-depth study of its working and custom training 

#### 3) Collect images using Google and Kaggle

#### 4) Labeling of images was implemented using [labelImg](https://github.com/tzutalin/labelImg)

#### 5) Train the model on the collected Data set 

#### 6) Made a Django-based web interface to host the model

<br/>

# Solution

#### 1) The initial dataset consisted of 100 images which were expanded using image processing techniques using OpenCV

#### 2) We used  [labelImg](https://github.com/tzutalin/labelImg) to gentrate labled .txt file

#### 3) Searching for proper training parameters was the toughest part, after multiple experiments and advice from mentors we were able to fix parameters like learning rate, no of steps for training, and much more

#### 4) Model training was done using Google Collab and data was accessed via Google Drive 

#### 5) Initial problems in the model were resolved using better data sets, changing parameters

#### 6) After training the model with sufficient accuracy it had to be hosted on a website

#### 7) It was deployed on Django because it is written in Python, OpenCV can be used with Django and it has many inbuilt features to aid the process of integration and building the website




# Working

## Get API access

#### Go to https://platerecognizer.com/ and get your credentials

#### Put them in webcam\views.py and add credentials in line 23
## Run the following commands


```
pip install -r requirements.txt

python manage.py create superuser (create a super user to access the admin page)   

python manage.py runserver
```
## After starting the server

#### Go to localhost:8000/admin 
#### in two-wheeler upload image to be tested 

#### Go to localhost:8000/index/camera2 to run the test and see the object detection output

#### Go to localhost:8000/admin/webcam/crime2/ to view the crime result

<br/>



# Result

### A platform was successfully presented to detect people on a two-wheeler and not wear helmets present in a given frame, storing proof of the violation and the number plate of the vehicle, leading to 30 points(max possible) in the Engineering conclave of Inter IIT Tech Meet 10 helping Institute to Bag GOLD Medal for the same   
