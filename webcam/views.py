from PIL import Image
from msilib.schema import File
from django.shortcuts import render
from django.core.files import File
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http.response import StreamingHttpResponse
from webcam.models import two_weeler, crime2
import cv2
import numpy as np
import json
import requests


def Api(img):
    regions = ['in']  # Change to your country
    with open(img, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions),  # Optional
            files=dict(upload=fp),
            headers={'Authorization': 'Token '})
        return response.json()["results"][0]["candidates"][0]["plate"]


# HOME PAGE -------------------------


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
# -----------------------------------

# CAMERA 1 PAGE ---------------------


def camera_1(request):
    template = loader.get_template('camera1.html')
    return HttpResponse(template.render({}, request))
# -----------------------------------

# CAMERA 1 PAGE ---------------------


def camera_2(request):
    template = loader.get_template('camera2.html')
    return HttpResponse(template.render({}, request))
# -----------------------------------

# DISPLAY CAMERA 1 ------------------


Crime = False
def test(video):
    global Crime
    vid = cv2.VideoCapture(video)
    whT = 320
    confThreshold = 0.5
    nmsThreshold = 0.6
    classesFile = 'objdet\coco.names'
    classNames = []
    f = open(classesFile, 'rt')
    classNames = f.read().rstrip('\n').split('\n')
    modelConfiguration = 'objdet\yolov3.cfg'
    modelWeights = 'objdet\yolov3.weights'
    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    

    classesFile2 = 'helmet\classes.names'
    classNames2 = []
    f2 = open(classesFile2, 'rt')
    classNames2 = f2.read().rstrip('\n').split('\n')
    modelConfiguration2 = 'helmet\yolov3.cfg'
    modelWeights2 = 'helmet\yolov3_final.weights'
    net2 = cv2.dnn.readNetFromDarknet(modelConfiguration2, modelWeights2)
    net2.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
    net2.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    
    def findObjects2(outputs, img):
        global Crime
        print(Crime)
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []
        for output in outputs:

            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold:
                    w, h = int(det[2] * wT), int(det[3]*hT)
                    x, y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

    # print(len(bbox))
        indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

        for i in indices:
            i = i[0]
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',
            #                 (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         
            print(classIds[i])
            if classIds[i] == 0:
                
                Crime=True
    def findObjects(outputs, img):
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []
        for output in outputs:

            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold:
                    w, h = int(det[2] * wT), int(det[3]*hT)
                    x, y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

    # print(len(bbox))
        indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

        for i in indices:
            i = i[0]
            box = bbox[i]
            global Crime
            print(Crime)
            if  Crime:
                
                di=crime2()
                di.name = two_weeler.objects.all()[len(two_weeler.objects.all())-1].name
                di.np = Api("currentframe.jpg")
                di.proof.save("proof2.jpg", File(open(r"currentframe.jpg", 'rb')), save=True)
                pass
            
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',
                            (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
   
    ret, frame = vid.read()
    cv2.imwrite('currentframe.jpg', frame)
    frame = cv2.resize(frame, (1000, 700))
    blob = cv2.dnn.blobFromImage(
        frame, 1/255, (whT, whT), [0, 0, 0], crop=False)
    net2.setInput(blob)

    layerNames = net2.getLayerNames()
    outputNames = [layerNames[i[0]-1]
                    for i in net2.getUnconnectedOutLayers()]

    outputs2 = net2.forward(outputNames)
    findObjects2(outputs2, frame)

    blob = cv2.dnn.blobFromImage(
        frame, 1/255, (whT, whT), [0, 0, 0], crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    outputNames = [layerNames[i[0]-1]
                    for i in net.getUnconnectedOutLayers()]

    outputs = net.forward(outputNames)
    findObjects(outputs, frame)


    cv2.imwrite('currentframe.jpg', frame)
    yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('currentframe.jpg', 'rb').read() + b'\r\n')


def stream_1():

    cam_id = 0
    vid = cv2.VideoCapture(cam_id)
    whT = 320
    confThreshold = 0.5
    nmsThreshold = 0.3
    classesFile = 'yolov3_weight\coco.names'
    classNames = []
    f = open(classesFile, 'rt')
    classNames = f.read().rstrip('\n').split('\n')
    modelConfiguration = 'yolov3_weight\yolov3.cfg'
    modelWeights = 'yolov3_weight\yolov3.weights'
    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def findObjects(outputs, img):
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []
        for output in outputs:

            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold:
                    w, h = int(det[2] * wT), int(det[3]*hT)
                    x, y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

    # print(len(bbox))
        indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

        for i in indices:
            i = i[0]
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
            try:
                cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',
                            (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
            except:
                cv2.putText(img, f'{"unidentified"} {int(confs[i]*100)}%',
                            (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

    while True:
        ret, frame = vid.read()

        frame = cv2.resize(frame, (1000, 700))
        blob = cv2.dnn.blobFromImage(
            frame, 1/255, (whT, whT), [0, 0, 0], crop=False)
        net.setInput(blob)

        layerNames = net.getLayerNames()
        outputNames = [layerNames[i[0]-1]
                       for i in net.getUnconnectedOutLayers()]

        outputs = net.forward(outputNames)
        findObjects(outputs, frame)

        cv2.imwrite('currentframe.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('currentframe.jpg', 'rb').read() + b'\r\n')


def video_feed_1(request):
    return StreamingHttpResponse(stream_1(), content_type='multipart/x-mixed-replace; boundary=frame')



# DISPLAY CAMERA 2 ------------------
def video_feed_2(request):
    print("x", str(two_weeler.objects.all()[0].file))
    return StreamingHttpResponse(test(str(two_weeler.objects.all()[len(two_weeler.objects.all())-1].file)), content_type='multipart/x-mixed-replace; boundary=frame')

