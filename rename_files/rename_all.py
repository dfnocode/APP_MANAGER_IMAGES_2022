# importing os module
import os
 
# Function to rename multiple files
def main():
   
    folder = "rename_files//1"

    # Keeps track of count of file name based on first field 
    fileNameCountDic = {}
    
    for count, filename in enumerate(os.listdir(folder)):

        # Original path to file
        src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
         
        # Get first field in file name so "B2011-BLUE-BW.jpg" -> "B2011"
        firstFileNameField = filename.split("-")[0]

        # If first field in filename is not in dic set it to be the first one
        if firstFileNameField not in fileNameCountDic:
          fileNameCountDic[firstFileNameField]=1
        else: # Else inc the count
          fileNameCountDic[firstFileNameField]+=1

        # Turn file count number to String
        fileNumber = str(fileNameCountDic[firstFileNameField])
        if len(fileNumber)==1: # Add space if one digit
          fileNumber="0"+fileNumber

        # Set the new path of the file
        dst = f"{folder}/{firstFileNameField}-{fileNumber}.png"

        # rename() function will
        # rename all the files
        os.rename(src, dst)



main()