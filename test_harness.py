import thinkplot
import thinkstats2

import import_ipynb
import solution_file

def test_sampleFunction():
    correctAnswer = 7
    assert correctAnswer == solution_file.sampleFunction() 

def test_secondFunction():
    incorrectAnswer = 9
    assert incorrectAnswer == solution_file.secondFunction()