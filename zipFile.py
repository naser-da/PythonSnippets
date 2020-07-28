from zipfile import ZipFile

file_dir = "C:\\Users\\Naser\\Desktop\\SahlaaFeedback(2).zip" #zip file location

with ZipFile(file_dir,"r") as zip_: #the "with" ensures the file is closed after we get out of the code block
    zip_.printdir() #print all containing files

    zip_.extractall() #extract files to the script destination




