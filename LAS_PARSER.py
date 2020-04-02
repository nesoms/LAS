import os
import re
import shutil
from os import path

# import lasio
import lasio

from _getfiles import getlasfiles

currentDirectory = os.getcwd()
print(currentDirectory)

file_location = 'F:\\Temp\\Logs'


#file_location = "c:\\Temp\\"
list_of_Files = getlasfiles(file_location)
destination = "F:\\Temp\\Logs\Run1\\"
os.chdir(file_location)
currentDirectory = os.getcwd()

#list_of_Files = os.listdir(currentDirectory)
list_of_Files = [f for f in os.listdir(currentDirectory) if f.endswith('.las')]

#print(list_of_Files)
FileCount = len(list_of_Files)
print("Number of files to parse....." + str(FileCount))

os.chdir(file_location)

for index in range(len(list_of_Files)):
    try:
        #File_to_Parse = file_location + '\\' + list_of_Files[index]
        File_to_Parse = list_of_Files[index]
        #File_to_Parse = currentDirectory + '\\' + list_of_Files[index]
        #File_to_Parse = list_of_Files[index]
        #print(index)
        print(File_to_Parse)
        las = lasio.read(File_to_Parse)

        print(File_to_Parse)
        #print(las.well)
        #print(las.header)
        #print(las.sections.keys())
        # print(las.well.comp.value)
        # print(las.well.well.value)
        #print(las.well.api.value)
        #
        #if hasattr(las.well, 'uwi'):
        #    print(las.well.uwi.value)
        #else:
        #    message = 'no-uwi'
        #    print('no uwi present')
        #print(las.well.uwi.value)
        #print(las.well.strt.value)
        #start = las.well.strt.value
        #print(las.well.stop.value)
        #stop = las.well.stop.value
        # new_file_name = company + '---' + wellname + '--' + str(uwi) + '.las'
        # print(new_file_name)
        # print(las.sections.keys())
        # print(len(las.header))
        # print(curve_list[:-1])
        # print(las.other)
        # las.write(sys.stdout)
        # print(las.header)

        if len(las.well.comp.value) > 0:
            #print("Company is " + str(len(las.well.comp.value)))
            company = las.well.comp.value
            company = company.replace(',', '')
            company = re.sub('[^A-Za-z0-9]+', ' ', company)
        else:
            company = "unknown"
            # print('else- unknown company')

        if las.well.well.value is not None:
            wellname = las.well.well.value
            wellname = re.sub('[^A-Za-z0-9]+', ' ', wellname)
        else:
            wellname = "unknown"
############################################################## Original
        #if len(str(las.well.uwi.value)) > 0:
        #    uwi = las.well.uwi.value
        #else:
        #    if len(str(las.well.api.value)) > 0:
        #        uwi = las.well.api.value
        #    else:
        #        uwi = '_unknown_api'

########################################################### End Original

#variable != "":

        if hasattr(las.well, 'uwi'):
            uwi = las.well.uwi.value
        else:
            if hasattr(las.well, 'api'):
                uwi = las.well.api.value
            else:
                uwi = '_unknown_api'
        ##########################################################
        #  building a string no order
        ##########################################################

        # curve_array = ''
        # if(len(las.curves) >= 15):
        #     counter = 15
        # else:
        #     counter = len(las.curves)
        # for curvesNames in range (counter):
        #     #print(curvesNames)
        #
        #     if (las.curves[curvesNames].mnemonic == 'DEPTH'):
        #        # print(las.curves[curvesNames].mnemonic)
        #        #print(las.curves[curvesNames].mnemonic)
        #         varempty = 0
        #     elif(las.curves[curvesNames].mnemonic == 'DEPT'):
        #         varempty = 0
        #     else:
        #         #print("Something")
        #         curve_array += las.curves[curvesNames].mnemonic + "_"
        #
        # print(curve_array[:-1])
        ##########################################################
        #  sorting array in order
        ##########################################################
        curve_array = []
        curvelimit = 5
        if len(las.curves) >= curvelimit:
            counter = curvelimit
        else:
            counter = len(las.curves)
        # print("Curve Count is  .... " + str(counter))
        for curvesNames in range (counter):
            #print(curvesNames)
            if las.curves[curvesNames].mnemonic == 'DEPTH':
               # print(las.curves[curvesNames].mnemonic)
               #print(las.curves[curvesNames].mnemonic)
                varempty = 0
            elif las.curves[curvesNames].mnemonic == 'DEPT':
                varempty = 0
            else:
                #print("Something")
                curve_array.append(las.curves[curvesNames].mnemonic)


        curve_array.sort()
        curve_list = ""

        # print('curves' + str(curve_array))
        for item in curve_array:
            #print(item)
            item = re.sub(':', '', item)
            curve_list += item + ","

        #head, tail = os.path.split(File_to_Parse)
        #
        #       This section sets the new name of the written LAS file
        #        [UWI] -- [original file name] -- [ top 5 curves]


        #new_file_name = str(uwi) + '--' + str(File_to_Parse[:-4]) + '--(' + str(curve_list[:-1]) + ').las'
        new_file_name = str(uwi) + '---(' + str(curve_list[:-1]) + ').las'


        # print('files to parse: ' + File_to_Parse)
        # print('new file name ' + new_file_name)
        # print('destination ' + destination)

        #original_name = destination + tail
        # original_name = destination + tail
        # print('original name...' + original_name)
        # rename = destination + new_file_name
        # print('rename file...' + rename)
        # shutil.copy2(File_to_Parse, rename)

        original_name =  destination + File_to_Parse
        #print('original name...' + original_name)
        new_name = destination + new_file_name
        #print('rename file...' + new_name)
        if path.exists(new_name):
            new_file_name = new_file_name + str(counter) + '.las'
            new_name = destination + new_file_name
            shutil.copy2(File_to_Parse, new_name)
        else:
            shutil.copy2(File_to_Parse, new_name)
    except:

        #File_to_Parse = destination + list_of_Files[index]
        message = ''
        File_to_Parse = file_location + '\\' + list_of_Files[index]
        error_file = open(destination + "_ErrorLog.txt", "a")
        error_file.write( str(File_to_Parse + '-----' + message + "\n"))
        error_file.close()
        print("An exception logged to Errorlog")

