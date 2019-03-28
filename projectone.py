import pandas as pd


#Notes:
#final attribute is always a class
#all attributes are catagorical
def preprocess(dataFilePath, headersFilePath):
    dataSet = pd.read_csv(dataFilePath).values.tolist()
    attributes = getAttributes(dataFilePath, headersFilePath)
    #construct a dict with each attribute as a key, and each catagory of that attribute in a list as the value
    catagories={}
    for row in dataSet:
        for i in range(len(attributes)):
            if attributes[i] in catagories.keys():
                if row[i] not in catagories[attributes[i]]:
                    catagories[attributes[i]].append(row[i])
            else:
                catagories[attributes[i]] = [row[i]]
    return (dataSet, attributes, catagories)

def getAttributes(dataFilePath, headersFilePath):
    attributes=[]
    count=0
    for line in open(headersFilePath).read().split('\n'):
        count=count+1
        if count==2:
            attributes=line.split(',')
        if line==dataFilePath:
            count=0
    return attributes

#write function to count and store the number of catagories per attribute per class label
#for each attribute, for each class label, count the number of each catagory
def makeBigDaddyDict(dataFilePath, headersFilePath):
    dataTuple=preprocess(dataFilePath, headersFilePath)
    data=dataTuple[0]
    attributes=dataTuple[1]
    catagories=dataTuple[2]
    bigDaddyDict={}
    for attribute in attributes[:-1]:
        attributeIndex=attributes.index(attribute)
        bigDaddyDict[attribute] = {}
        print("----")
        print(attribute)
        for catagory in catagories[attribute]:
            bigDaddyDict[attribute][catagory] = {}
            print("----")
            print(catagory)
            for classCatagory in catagories['class']:
                print(classCatagory)
                count=0
                #TODO: add one to count each time 'catagory' is in the same row as 'classCatagory'
                attributeIndex=attributes.index(attribute)

                bigDaddyDict[attribute][catagory][classCatagory] = count
    return bigDaddyDict

#dataSet should be a list of lists, where each list is a row
def train(processedData):
    size = getDimensions()

    return

def predict():
    return

def evaluate():
    return

def infoGain():
    return

#return tuple of (number of columns, number of rows)
def getDimensions(arrayOfRows):
    return (len(arrayOfRows[0]), len(arrayOfRows))


headers=('headers.txt')
test=preprocess('car.csv', headers)
print(test[2])
print("--------------")
print(makeBigDaddyDict('car.csv', headers))
