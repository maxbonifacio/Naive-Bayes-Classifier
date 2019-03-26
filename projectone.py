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

#dataSet should be a list of lists, where each list is a row
def train(processedData):
    size = getDimensions()

    #count and store the number of catagories per attribute per class label

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
