import thinkplot
import thinkstats2

import pandas as pd
import import_ipynb
import solution_file

with open("LabourTrainingEvaluationData.csv") as f:
    data = pd.read_csv(f)
#print(data.dtypes)
#print(data["Earnings_1978"].describe())

def test_rangeMag(df_in, columnName):
    usedColumn = df_in[columnName]
    tmpMax = usedColumn.max()
    tmpMin = usedColumn.min()
    retVal = tmpMax-tmpMin
    #print(tmpMin)
    #print(tmpMax)
    #print(retVal)
    assert (retVal == solution_file.rangeMag(data, columnName))

def test_earnedAbove(df_in, amount, columnName):
    usedColumn = df_in[columnName]
    #print(usedColumn)
    biggerList = usedColumn[usedColumn>amount]
    #print(biggerList)
    retVal = biggerList.size
    #print(retVal)
    assert (retVal == (solution_file.earnedAbove(data, amount, columnName)))

def test_difference_74_78(df_in):
    incomes = df_in[["Earnings_1974", "Earnings_1978"]]
    #print(incomes.dtypes)
    a = (incomes["Earnings_1978"] - incomes["Earnings_1974"])
    #print(a)
    retVal = np.mean(a)
    #print(np.mean(a))
    #print(df_in)
    assert (retVal == solution_file.difference_74_78(data))

def test_ageCount(df_in, low_age, high_age):
    numData = pd.to_numeric(df_in["Age"], errors='raise')
    numData = np.array(numData)
    #print(numData)
    data1 = numData[np.where((numData <= high_age) & (numData >= low_age))]
    retVal = data1.size
    #print(retVal)
    #return retVal
    assert (retVal == solution_file.ageCount(data))

def test_cohort(df_in):
    df_in["Cohort"] = (df_in["Race"]+df_in["Hisp"]+df_in["MaritalStatus"])
    #print(df_in["Cohort"].unique())
    cohortList = df_in["Cohort"].unique()
    i = 0
    resList = []
    lowest = -1
    while i < cohortList.size:
        tmp = df_in[df_in.Cohort == cohortList[i]]
        #print(tmp.shape[0])
        #print(df_in[df_in.Cohort == cohortList[i]])
        #cohortSize = tmp.shape[0]
        cohortMed = np.median(pd.to_numeric(tmp["Earnings_1978"]))
        tmpTuple = (cohortList[i], cohortMed)
        resList.append(tmpTuple)
        if ((cohortMed < lowest) | (lowest == -1)):
            lowest = cohortMed
        i = i + 1
    assert (lowest == solution_file.cohort(data))

# test_ageCount(data, )
# test_average_1(data)
# test_cohort(data)
#test_rangeMag(data,"Earnings_1978")
#test_earnedAbove(data, 19000, "Earnings_1978")