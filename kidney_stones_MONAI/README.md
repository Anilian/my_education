
**Deidentification_DICOM.py** - script that runs the IT department after receiving the original DICOM files to anonymize the data
**create_DICOM_dataset.ipynb** - contains functions that translate DICOM files into a view suitable for MONAI models
**create_labels_dataset.ipynb**- contains functions that translate json files from CVAT partitioner into a view suitable for MONAI models.
**prepare_dataset.ipynb** - contains functions to thin the data directly into json (not needed for operation)
**monai_Unet.ipynb** - load dataset, apply transformations and run models
* Based on https://github.com/Project-MONAI/tutorials/blob/main/3d_segmentation/spleen_segmentation_3d.ipynb

**Data:**
For training, data from 10 patients with the following class ratio were used

  patient_label_1.nii.gz: кол-во фото с камнем 5, без - 123 

  patient_label_2.nii.gz: кол-во фото с камнем 7, без - 121 

  patient_label_3.nii.gz: кол-во фото с камнем 8, без – 120

  patient_label_4.nii.gz: кол-во фото с камнем 14, без - 114 

  patient_label_5.nii.gz: кол-во фото с камнем 7, без - 121 

  patient_label_6.nii.gz: кол-во фото с камнем 19, без - 109 

  patient_label_7.nii.gz: кол-во фото с камнем 12, без - 116

  patient_label_9.nii.gz: кол-во фото с камнем 6, без - 122 

  patient_label_10.nii.gz: кол-во фото с камнем 5, без - 123

**Method:** google collab GPU with 15gb was used. Batch size = 1 and size one image 192x192

The study used UNet, UNETR, SwinUNETR, different types of optimizers (Adam, SGD, AdamW) and DiceLoss function parameters (include_background =False or true)

**Results:** the model is not trained

![1](https://github.com/Anilian/my_education/assets/122607689/6d704fe4-9f85-4e3f-8e3c-78e0f2fbf412)
![2](https://github.com/Anilian/my_education/assets/122607689/7cf555cb-2254-4bae-b432-5d4151549759)
![3](https://github.com/Anilian/my_education/assets/122607689/07fe5e0d-35de-4221-8d10-3ef2876e9c9b)





