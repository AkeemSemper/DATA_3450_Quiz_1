#Import Python Stuff
import thinkplot
import thinkstats2
import pandas as pd
import numpy as np

#Import solution file
import import_ipynb
import solution_file

#Load data file
with open("LabourTrainingEvaluationData.csv") as f:
    data = pd.read_csv(f)

#Import remote solutions
import httpimport
from httpimport import *
url = "https://gist.githubusercontent.com/AkeemSemper/5efb8626f92408eb17149905bf564d92/raw/5d250b0129aa534b39f5e384c3417ab9c35aa4e9/"
with httpimport.remote_repo(["stats_Quiz1_sol"], url):
    import stats_Quiz1_sol

def test_rangeMag(df_in, columnName):
    studAnswer = solution_file.rangeMag(df_in, columnName)
    solAnswer = stats_Quiz1_sol.rangeMag(df_in, columnName)
    assert (studAnswer == solAnswer)

def test_earnedAbove(df_in, amount, columnName):
    studAnswer = solution_file.earnedAbove(df_in, amount, columnName)
    solAnswer = stats_Quiz1_sol.earnedAbove(df_in, amount, columnName)
    assert (studAnswer == solAnswer)

def test_difference_74_78(df_in, column_low, column_high):
    studAnswer = solution_file.difference_74_78(df_in, column_low, column_high)
    solAnswer = stats_Quiz1_sol.difference_74_78(df_in, column_low, column_high)
    assert (studAnswer == solAnswer)

def test_ageCount(df_in, low_age, high_age):
    studAnswer = solution_file.ageCount(df_in, low_age, high_age)
    solAnswer = stats_Quiz1_sol.ageCount(df_in, low_age, high_age)
    assert (studAnswer == solAnswer)

def test_cohort(df_in, cohort1, cohort2, cohort3, earningsColumn):
    studAnswer = solution_file.cohort(df_in, cohort1, cohort2, cohort3, earningsColumn)
    solAnswer = stats_Quiz1_sol.cohort(df_in, cohort1, cohort2, cohort3, earningsColumn)
    assert (studAnswer == solAnswer)

#
#test_rangeMag(data, "Age")
#test_earnedAbove(data, 19000, "Earnings_1978")
#test_difference_74_78(data, "Earnings_1974", "Earnings_1978")
#test_ageCount(data, 18, 35)
#test_cohort(data, "Race", "Hisp", "MaritalStatus", "Earnings_1978")