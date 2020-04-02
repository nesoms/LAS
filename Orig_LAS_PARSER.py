import os

import lasio

currentDirectory = os.getcwd()
print(currentDirectory)
os.chdir('F:/Temp/Logs')
currentDirectory = os.getcwd()
print(currentDirectory)

#ListofFiles = os.listdir(currentDirectory)
ListofFiles = [f for f in os.listdir(currentDirectory) if f.endswith('.LAS')]
print(ListofFiles)
FileCount = len(ListofFiles)
#print(FileCount)


for index in range( len(ListofFiles)):
    try:
        FiletoParse = currentDirectory + '\\' + ListofFiles[index]
        #print('files to parse: ' + FiletoParse)
        las = lasio.read(FiletoParse)

        print(FiletoParse)
        #las.sections.keys()
        #print(las.header)
        #print(las.sections.keys())
        #print(las.well.comp.value)
        company = las.well.comp.value
        #print(las.well.well.value)
        wellname = las.well.well.value
        #print(las.well.uwi.value)
        uwi = las.well.uwi.value
        #print(las.well.strt.value)
        start = las.well.strt.value
        #print(las.well.stop.value)
        stop = las.well.stop.value

        newfilename = company + '---' + wellname + '--' + str(uwi) + '.las'
        print(newfilename)
        #print(len(las.sections.keys()))
        #for sectionName in range (len(las.header)):
        #    las.sections[sectionName]
        #    print(las.well[sectionName].mnemonic)
        #print(las.curves)
        #print(las.params)
        #print(las.other)
        #las.write(sys.stdout)
        #print(las.header)
        try:
            os.rename(FiletoParse,newfilename)
        except:
            print("An exception occurred")

    except:
        print('Bad Log' + FiletoParse )
#print(las.sections.keys())
#print(len(las.sections.keys()))
counter = 0
for VarItem in (las.well):
    #print(las.well[counter].mnemonic)
    Column1 = las.well[counter].mnemonic
    Column2 = las.well[counter].value
    #print(VarItem)
    counter += 1
    if Column2 is not None:
        #print('Column 1 %s and Column2 %s' (Column1,  len(Column1)))
        if bool(Column2):
            print(Column1)
            print(Column2)
        else:
            Column2 = 'N/A'
            print(Column1)
            print(Column2)
            f = open("well.txt", "a+")

            Info = Column1 + ',' + Column2
            f.write(Info)
            f.close()