# -*-Exercise 1 and 5
from Dataset import csvReader,Dataset,csvSplitReader,predictions

if __name__ == "__main__":
    #testing with my data 
    choose = input("Please press '1' if you want to use Iris.csv or else press '0':  ")
    choose = int(choose)
    k = input("Enter value of k: ")
    k = int(k)
    if choose == 1:
        #test with Iris.csv data
        dtPoints = csvSplitReader("Iris.csv",100,"start")
        dtSet = Dataset(dtPoints)
        qrPoints = csvSplitReader("Iris.csv",50,"end")
        qrSet = Dataset(qrPoints)
        if k > len(dtSet.elements):
            print("k is too large!")
        else:
            predictions(dtSet,qrSet,"Iris.csv",k)
    else:
        datasetPoints = csvReader('trainingSet.csv')
        dataset = Dataset(datasetPoints)
        queries = csvReader('testSet.csv')
        queryset = Dataset(queries)
        if k > len(dataset.elements):
            print("k is too large!")
        else:
            predictions(dataset,queryset,"testSet.csv",k)
