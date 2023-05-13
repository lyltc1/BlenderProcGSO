''' Script for unzip all files in this directory '''
import os
import zipfile

dir_path = os.path.abspath(os.path.dirname(__file__))
print(dir_path)
extension = ".zip"

for item in os.listdir(dir_path): # loop through items in the directory
    if item.endswith(extension): # check for ".zip" extension
        file_path = os.path.join(dir_path, item) # get full path of files
        zip_ref = zipfile.ZipFile(file_path) # create zipfile object
        zip_ref.extractall(os.path.join(dir_path, item.split('.')[0])) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_path) # delete zipped file