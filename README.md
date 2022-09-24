# Inter IIT Tech Meet 10.0 Engineering Conclave , Recived a Gold Medal fro the same

## Problem Statement

#### To create a deep-learning based system to detect and store information of traffic violators in a database hosted on a website to collect proof and number plates of the criminals simultaneously.

## Mentors

### [Pranjal Mangal](https://github.com/mangalpranjal)
### [Maanas Verma](https://github.com/Maanas-Verma)

## Contributors 

### [Harshit Gupta](https://github.com/Daredevil5053728)
### [Pranav Arya](https://github.com/pranav-iitr)
### [Madhumita](https://github.com/madhu7988)
### [Ananya Sharma](https://github.com/sharmaananya-14)
<br/>

## Technolegy used

<img align="left" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" style="padding-right:10px;" />
<img align="left"  width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original-wordmark.svg" style="padding-right:10px;" />
<img align="left"  width="35px" src="https://cdn.analyticsvidhya.com/wp-content/uploads/2018/12/yologo_2-850x451.png"  />
<br/>
<br/>

###

# Approach

#### 1) Learn Differnt Computer Vission and Deep Learning models

#### 2) As yolo was chosen for the project, do an in depth study of it's working and custom training 

#### 3) Collect images using Google and Kaggle

#### 4) Labling of images was implemented using [labelImg](https://github.com/tzutalin/labelImg)

#### 5) Train the model on the collected Data set 

#### 6) Made a Django based web interface to host the model

<br/>

# Solution

#### 1)Intial dataset consisted of 100 images which were expanded using image processing tecniques using OpenCV

#### 2) We used  [labelImg](https://github.com/tzutalin/labelImg) to gentrate labled .txt file

#### 3) Seraching for proper training parameters was toughest part, after multiple experiments and advice for mentors we were able to fix parameters like learning rate,no of steps for training and much more

#### 4) Model training was done using google collab and data was acessed via google drive 

#### 5) Intial problems in the model were resoloved using better data sets, changing parameters

#### 6) After training of model with sufficent accurecy it had to host it on a website

#### 7) it was deployed on Django because it is written in python,OpenCv can used with Django and it has many inbuilt fetures to aid the process of integration and built the website




# Working

## Get API acess

#### Go to https://platerecognizer.com/ and get your credentials

#### Put them in webcam\views.py and add creditals in line 23
## Run the following commands


```
pip install -r requirements.txt

python manage.py createsuperuser (create a super user to acess admin page)   

python manage.py runserver
```
## After starting the server

#### Go to localhost:8000/admin 
#### in two wheller upload image to be tested 

#### Go to localhost:8000/index/camera2 to run the test and see the object detection output

#### Go to localhost:8000/admin/webcam/crime2/ to view the crime result

<br/>

# Achivement

### The Project Recived Gold Medal 

# Result

### A platform was successfully presented to detect people on a two-wheeler and not wear helmets present in a given frame, storing proof of the violation and the number plate of the vehicle, leading to 30 points(max possible) in the Engineering conclave of Inter IIT Tech Meet 10 helping Institute to Bag Bronze Medal for the same   
