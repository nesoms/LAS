
import os
import lasio
files = []



def getlasfiles(filepath):
    print(filepath)
    listoffiles =[]
    listoffiles = os.listdir(filepath)
    print(listoffiles)
    return listoffiles


#filelocation = "D:\\xxSampleData\\LAS-Test"
#files = getlasfiles(filelocation)


