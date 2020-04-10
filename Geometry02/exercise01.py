# -*-Exercise 1
from Dataset import csvReader,Dataset,classify

if __name__ == "__main__":
    datasetPoints = csvReader('trainingSet.csv')
    dataset = Dataset(datasetPoints)
    #dataset.printPoints()
    queries = csvReader('testSet.csv')
    queryset = Dataset(queries)
    k = input("Enter value of k: ")
    k = int(k)
    if k > len(dataset.elements):
        print("k is too large!")
    else:
        for i in range(0,len(queryset.elements)):
            classify(dataset,queryset.elements[i],k)    
