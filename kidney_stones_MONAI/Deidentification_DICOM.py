# %%
import pydicom as dicom
import os

# %%

if __name__ == "__main__":
  dataset_path = input("ввести путь до папки, где хранятся другие папки с данными каждого пациента '\\':")
  dataset_path = dataset_path.replace('\\', '/')
  upper_folders = os.listdir(dataset_path)

  # верхний слой папок
  for upper_folder in upper_folders:
    
    path_to_upper_folder = os.path.join(dataset_path,upper_folder)
    if upper_folder == 'desktop.ini':
       continue
    
    folders = os.listdir(path_to_upper_folder)

    # нижний слой папок
    for folder in folders:
      path_to_folder = os.path.join(path_to_upper_folder,folder)
      files = os.listdir(path_to_folder)

      # files
      for file in files:
          file_path = os.path.join(path_to_folder,file)
          patient_dcm = dicom.dcmread(file_path)
          patient_dcm.InstitutionName = ''
          patient_dcm.InstitutionAddress = ''
          patient_dcm.StudyDescription = ''
          patient_dcm.PatientName = ''
          patient_dcm.PatientID = ''
          patient_dcm.PatientBirthDate = ''
          patient_dcm.save_as(file_path)
      print(upper_folder + '\\' + folder)



