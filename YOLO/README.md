# Here are the steps to develop a model for detecting plastic and paper with an industrial camera
## 1. Create your own dataset
### 1.1 Open Images Dataset V7.
This can be done by following the instructions in the [notepad](https://github.com/Anilian/my_education/blob/main/YOLO/My_test_YOLOv4.ipynb), using the marked images on a large number of classes. 
### 1.2 Labeling own photo 
Using computer vision annotation [tool](https://app.cvat.ai/tasks?page=1) 300 photos were labeled

<img src = "https://github.com/Anilian/my_education/blob/main/YOLO/cvat_label.png" width="300" height="300" />
## 1.3 Dataset organization of YOLOv8
```bush                           
The structure of the google.drive file org chart own_dataset
.
├── train
│   ├── images
│   └── labels
├── test
│   ├── images
│   └── labels
├── val
│   ├── images
│   └── labels
├── custom_data.yaml
└── yolov8x-seg_custom.yaml
```
                           
## 2. Training using the online GPU google collab
The [notebook](https://github.com/Anilian/my_education/blob/main/YOLO/train_yolov8.ipynb) describes the procedure for training and validation
Additional training files [yolov8x-seg_custom.yaml](https://github.com/Anilian/my_education/blob/main/YOLO/yolov8x-seg_custom.yaml),[custom_data.yaml](https://github.com/Anilian/my_education/blob/main/YOLO/custom_data%20(1).yaml)

Using a step-by-step guide we trained the model on 50 epochs. It took about 25 minutes and obtained the following metrics.

<img src = "https://github.com/Anilian/my_education/blob/main/YOLO/results.png" width="800" height="300" />

The predictions on the test sample showed excellent results

<img src = "https://github.com/Anilian/my_education/blob/main/YOLO/228.jpg" width="300" height="300" />

## 3.Testing using an industrial camera ##
The project was implemented to detect garbage at a rate of 10FPS using the computer's GPU. The notepad is located [here](https://github.com/Anilian/my_education/blob/main/YOLO/Waste%20Management%20System.ipynb). 
The task was as follows: to get the coordinates of one of the 5 areas on one track on which the garbage is moving. 

<img src="https://github.com/Anilian/my_education/blob/main/YOLO/Slow%20test.gif" alt="My Project GIF" width="300" height="300">

