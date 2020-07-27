import os

def shutdown():
    os.system("shutdown /s /t 1") #shutdown the PC in 1 sec

def restart():
    os.system("shutdown /r /t 1") #restart the PC in 1 sec