#Import Python Stuff
import thinkplot
import thinkstats2
import pandas as pd
import numpy as np
import pytest
import math

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

#Set Test Variables
df_in = data #data source
#Range
columnNameRange = "Earnings_1978"
#EarnedAbove
amount = 19000
columnNameAbove = "Earnings_1978"
#Difference
column_low = "Earnings_1974"
column_high = "Earnings_1978"
#Age Count
low_age = 18
high_age = 35
columnNameAge = "Age"
#cohort
cohort1 = "Race"
cohort2 = "Hisp"
cohort3 = "MaritalStatus"
earningsColumn = "Earnings_1978"

@pytest.mark.a
def test_rangeMag():
    studAnswer = solution_file.rangeMag(df_in, columnNameRange)
    solAnswer = stats_Quiz1_sol.rangeMag(df_in, columnNameRange)
    assert math.isclose(studAnswer, solAnswer, rel_tol=.05)
    #assert (studAnswer == solAnswer)

@pytest.mark.b
def test_earnedAbove():
    studAnswer = solution_file.earnedAbove(df_in, amount, columnNameAbove)
    solAnswer = stats_Quiz1_sol.earnedAbove(df_in, amount, columnNameAbove)
    assert math.isclose(studAnswer, solAnswer, rel_tol=.05)
    #assert (studAnswer == solAnswer)

@pytest.mark.c
def test_difference_74_78():
    studAnswer = solution_file.difference_74_78(df_in, column_low, column_high)
    solAnswer = stats_Quiz1_sol.difference_74_78(df_in, column_low, column_high)
    assert math.isclose(abs(studAnswer), abs(solAnswer), rel_tol=.05)
    #assert (studAnswer == solAnswer)

@pytest.mark.d
def test_ageCount():
    studAnswer = solution_file.ageCount(df_in, columnNameAge, low_age, high_age)
    solAnswer = stats_Quiz1_sol.ageCount(df_in, columnNameAge, low_age, high_age)
    assert math.isclose(studAnswer, solAnswer, rel_tol=.05)
    #assert (studAnswer == solAnswer)

@pytest.mark.e
def test_cohort():
    studAnswer = solution_file.cohort(df_in, cohort1, cohort2, cohort3, earningsColumn)
    solAnswer = stats_Quiz1_sol.cohort(df_in, cohort1, cohort2, cohort3, earningsColumn)
    assert math.isclose(studAnswer, solAnswer, rel_tol=.05)
    #assert (studAnswer == solAnswer)

#
#test_rangeMag()
#test_earnedAbove()
#test_difference_74_78()
#test_ageCount()
#test_cohort()