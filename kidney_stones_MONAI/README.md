**Deidentification_DICOM.py** - script that runs the IT department after receiving the original DICOM files to anonymize the data
**create_DICOM_dataset.ipynb** - contains functions that translate DICOM files into a view suitable for MONAI models
**create_labels_dataset.ipynb**- contains functions that translate json files from CVAT partitioner into a view suitable for MONAI models.
**prepare_dataset.ipynb** - contains functions to thin the data directly into json (not needed for operation)
**monai_Unet.ipynb** - load dataset, apply transformations and run models
