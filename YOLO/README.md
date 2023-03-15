# Here are the steps to develop a model for detecting plastic and paper with an industrial camera
## 1. Create your own dataset
### 1.1 Open Images Dataset V7.
This can be done by following the instructions in the file DataSet for train YOLOv4.ipthon, using the marked images on a large number of classes. 
### 1.2 Labeling own photo 
Using computer vision annotation[tool](https://app.cvat.ai/tasks?page=1) 300 photos were labeled

<img src = "https://github.com/Anilian/my_education/blob/main/YOLO/cvat_label.png" width="200" height="200" />

|The structure of the google.drive file org chart
---own_dataset----|custom_data.yaml
                  |yolov8x-seg_custom.yaml
                  |train--------------------------|images
                                                  |labels
                  |test---------------|images
                                      |labels
                  |val---- |images
                           |labels
