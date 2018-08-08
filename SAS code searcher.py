import glob
import os
InputPath  = r'D:' #Modify this to define which folder you want to start at
for files in glob.glob(InputPath +  "/**/*.sas" , recursive=True): #you can replace .sas with some other file extension if you need to search them
    f = open( files, 'r' )
    for line in f:
        if "my_search_term" in line: #Modify the text in quotes to find out the search term
            print( files )
            print(line) # I am printing line here to narrow down my search for the program that actually creates the dataset
