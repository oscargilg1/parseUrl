from urllib.parse import urlparse, parse_qs
import argparse

paths = []
queryParams = []
values = []

def getPaths(inputFile, outputFile):
    file = open(inputFile, 'r')
    Lines = file.readlines()
    for line in Lines:
        path = urlparse(line).path
        paths.append(path)
    fileWorker(paths, outputFile)

def getParams(inputFile, outputFile):
    file = open(inputFile, 'r')
    Lines = file.readlines()
    for line in Lines:
        queryString = parse_qs(urlparse(line).query)
        for i in queryString.values():
            values.append(i)
        for key in queryString.keys():
            queryParams.append(key)
    storeValues = input("Would you like to export parameter values? ")
    if storeValues == "y":
        file = open("values.txt", "w", encoding='utf-8')
        sortedValues = []
        [sortedValues.append(x) for x in values if x not in sortedValues]
        finalValues = []
        for item in sortedValues:
            finalValues.append("".join(str(x) for x in item))
            file.writelines("\n".join(finalValues))
        file.close()
        print("Parameter values saved to current working directory as values.txt")    
        fileWorker(queryParams, outputFile)
    elif storeValues == "n":
        fileWorker(queryParams, outputFile)

def fileWorker(objects, outputFile):
    paths = objects
    file = open(outputFile, "w")
    pathsSorted = []
    [pathsSorted.append(x) for x in paths if x not in pathsSorted]
    file.writelines("\n".join(pathsSorted))
    queryParams = objects
    queryStringSorted = []
    [queryStringSorted.append(x) for x in queryParams if x not in queryStringSorted]
    file.writelines("\n".join(queryStringSorted))
    file.close()   

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFile", help="Location of your wordlist, Ex: -i /home/user/wordlist.txt"),
parser.add_argument("-p", '--paths' , action='store_true', help="Get a list of paths"),
parser.add_argument("-q", "--queryString", action="store_true", help="Get a list of GET parameters"),
parser.add_argument("-o", "--outputFile", help="File to write the wordlist to, Ex: -o /home/user/mywordlist.txt")  

args = parser.parse_args() 

inputFile = args.inputFile
outputFile = args.outputFile

if args.paths:
    getPaths(inputFile, outputFile)
if args.queryString:
    getParams(inputFile, outputFile)