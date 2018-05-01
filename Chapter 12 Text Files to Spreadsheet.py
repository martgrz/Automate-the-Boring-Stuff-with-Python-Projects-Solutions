#   openpyxl.__version__
#   '2.5.3'

import os
import openpyxl


text_files =[]
files_content = []

#get only text files from the folder
#save text files and python file in the same folder

for filename in os.listdir():
    if filename.endswith('txt'):
        text_files.append(filename)

#open and read text from each file
#and nest them in files_content list.

for file in text_files:
    file = open(file)
    file = file.readlines()
    files_content.append(file)


#create a new Excel workbook

wb = openpyxl.Workbook()
sheet = wb.active

#insert content of text files to the spreadsheet
#len of file_content list indicates number of columns in the spreadsheet
#len of each nested list indicates number of rows 

for column in range(len(files_content)):
    for row in range(len(files_content[column])):
        sheet.cell(row+1,column+1).value = files_content[column][row]

#save data in new Excel Workbook
wb.save('total.xlsx')
