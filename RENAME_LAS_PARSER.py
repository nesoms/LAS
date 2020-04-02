import os

import lasio

currentDirectory = os.getcwd()
print(currentDirectory)
os.chdir('F:/Temp/Logs')
currentDirectory = os.getcwd()
print(currentDirectory)

#ListofFiles = os.listdir(currentDirectory)
ListofFiles = [f for f in os.listdir(currentDirectory) if f.endswith('.las')]
print(ListofFiles)
FileCount = len(ListofFiles)
#print(FileCount)


for index in range( len(ListofFiles)):
        FiletoParse = currentDirectory + '\\' + ListofFiles[index]

        las = lasio.read(FiletoParse)
        # print('files to parse: ' + FiletoParse)
        #print(FiletoParse)
        #print(las.well)
        #print(las.header)
        #print(las.sections.keys())
        #print(las.well.comp.value)
        #company = las.well.comp.value
        #print(las.well.well.value)
        #wellname = las.well.well.value
        #print(las.well.uwi.value)
        #uwi = las.well.uwi.value
        #print(las.well.strt.value)
        #start = las.well.strt.value
        #print(las.well.stop.value)
        #stop = las.well.stop.value
        # newfilename = company + '---' + wellname + '--' + str(uwi) + '.las'
        # print(newfilename)
        # print(las.sections.keys())
        # print(len(las.header))
        # print(curvelist[:-1])
        # print(las.other)
        # las.write(sys.stdout)
        # print(las.header)

        try:
            if las.well.comp.value is not None:
                company = las.well.comp.value
                company = company.replace(',', '')

            else:
                company = "unknown"
                print('unknown company')
        except:
            company = "[unknown Company]"

        try:
            if las.well.well.value is not None:
                wellname = las.well.well.value
            else:
                wellname = "unknown"

        except:
            wellname = "[unknown WellName]"

        try:
            if las.well.uwi.value is not None:
                uwi = las.well.uwi.value
            else:
                uwi = las.well.api.value
        except:
            try:
                if las.well.api.value is not None:
                    uwi = las.well.api.value
                else:
                    uwi = las.well.api.value
            except:
                uwi = '[unknown api]'


        ##########################################################
        #  building a string no order
        ##########################################################

        # varfoo = ''
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
        #         varfoo += las.curves[curvesNames].mnemonic + "_"
        #
        # print(varfoo[:-1])
        ##########################################################
        #  sorting array in order
        ##########################################################
        varfoo = []
        if(len(las.curves) >= 15):
            counter = 15
        else:
            counter = len(las.curves)
        for curvesNames in range (counter):
            #print(curvesNames)

            if (las.curves[curvesNames].mnemonic == 'DEPTH'):
               # print(las.curves[curvesNames].mnemonic)
               #print(las.curves[curvesNames].mnemonic)
                varempty = 0
            elif(las.curves[curvesNames].mnemonic == 'DEPT'):
                varempty = 0
            else:
                #print("Something")
                varfoo.append(las.curves[curvesNames].mnemonic)

        varfoo.sort()
        curvelist = ""
        #print(varfoo)
        for item in (varfoo):
            #print(item)
            curvelist += item + "_"


        newfilename = company + '--' + wellname + '--' + str(uwi) +'--(' + str(curvelist[:-1]) +').las'

        try:
            print(newfilename)
            os.rename(FiletoParse,newfilename)

        except:
            print("An exception occurred")


