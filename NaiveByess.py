from irisDataSet import irisDataSet
from operator import itemgetter

irisTypes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

sepalLength = 5.9
sepalWidth = 3.0
petalLength = 5.1
petalWidth = 1.8

featureValueList = [sepalLength, sepalWidth, petalLength, petalWidth]

totalNumOfPlants = len(irisDataSet)  # 150


# Find the probablity of a specific plant type
def probabilityOfPlant(dataset, classType):
    count = 0
    for data in dataset:
        if data['class'] == classType:
            count = count+1
    return count


# Finds the probability of single feature to a single class type
def probabilityOfFeatureToClass(feature, classType, featureValue, dataset):
    count = 0
    for data in dataset:
        if data['class'] == classType and data[feature] == featureValue:
            count = count+1
    return count


# Returns the probability of a feature(length etc) to a class(plant type)
def probabilityOfAllFeatures(classType, countOfClass, featureValue, dataset):
    probabilityOfSepalLength = probabilityOfFeatureToClass(
        'sepalLength', classType, featureValue[0], dataset)
    probabilityOfSepalWidth = probabilityOfFeatureToClass(
        'sepalWidth', classType, featureValue[1], dataset)
    probabilityOfPetalLength = probabilityOfFeatureToClass(
        'petalLength', classType, featureValue[2], dataset)
    probabilityOfPetalWidth = probabilityOfFeatureToClass(
        'petalWidth', classType, featureValue[3], dataset)
    probabilities = {
        'probabilityOfSepalLength': probabilityOfSepalLength/countOfClass,
        'probabilityOfSepalWidth': probabilityOfSepalWidth/countOfClass,
        'probabilityOfPetalLength': probabilityOfPetalLength/countOfClass,
        'probabilityOfPetalWidth': probabilityOfPetalWidth/countOfClass
    }
    return probabilities


# Computes the total probability
def totalProbability(probabilityOfClass, probabilityOfAllFeaturesToClass):
    w, x, y, z = itemgetter('probabilityOfSepalLength', 'probabilityOfSepalWidth',
                            'probabilityOfPetalLength', 'probabilityOfPetalWidth')(probabilityOfAllFeaturesToClass)
    return probabilityOfClass*w*x*y*z


# <--------------------MAIN--------------------->


# Getting the count of every plant type
countOfIrisSetosa = probabilityOfPlant(irisDataSet, 'Iris-setosa')
countOfIrisVersicolor = probabilityOfPlant(
    irisDataSet, 'Iris-versicolor')
countOfIrisVirginica = probabilityOfPlant(irisDataSet, 'Iris-virginica')

# Getting the probability of every plant type
probabilityOfIrisSetosa = countOfIrisSetosa/totalNumOfPlants
probabilityOfIrisVersicolor = countOfIrisVersicolor/totalNumOfPlants
probabilityOfIrisVirginica = countOfIrisVirginica/totalNumOfPlants

# Getting probabilitie of all features to a class
probOfAllFeaturesToSetosa = probabilityOfAllFeatures(
    'Iris-setosa', countOfIrisSetosa, featureValueList, irisDataSet)
probOfAllFeaturesToVersicolor = probabilityOfAllFeatures(
    'Iris-versicolor', countOfIrisVersicolor, featureValueList, irisDataSet)
probOfAllFeaturesToVirginica = probabilityOfAllFeatures(
    'Iris-virginica', countOfIrisVirginica, featureValueList, irisDataSet)

# Getting Results for all plants
resultOfSetosa = totalProbability(
    probabilityOfIrisSetosa, probOfAllFeaturesToSetosa)
resultOfVersicolor = totalProbability(
    probabilityOfIrisVersicolor, probOfAllFeaturesToVersicolor)
resultOfVirginica = totalProbability(
    probabilityOfIrisVirginica, probOfAllFeaturesToVirginica)

results = [resultOfSetosa, resultOfVersicolor, resultOfVirginica]

maxValue = max(resultOfSetosa, resultOfVersicolor, resultOfVirginica)

for i, value in enumerate(results):
    if maxValue == value:
        print("Given values belongs to Iris-Setosa Plant") if i == 0 else print(
            "Given values belongs to Iris-Versicolor Plant") if i == 1 else print("Given values belongs to Iris-Virginica Plant") if i == 2 else print('Theres some error')
