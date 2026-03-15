from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import sqlite3 as sql
import numpy as np
from ModellingFunctions.DataModelling import *

SchoolQuery = '''SELECT SchoolID, SchoolName
                FROM School'''

def PredictGrade(TrainingData, PredictionData):
    TrainingData = TrainingData.apply(ConvertBoolToInt, axis=1) #Converts any columns that contain yes/no to 1/0
    x = TrainingData[['SchoolID', 'PlansOnHigherEducation', 'FailureCount', 'ExamOneGrade', 'ExamTwoGrade']] #What the model is trained to predict on
    y = TrainingData['ExamThreeGrade'] #What the model is trained to predict
    GradePredictor = RandomForestRegressor(n_estimators=10, random_state=0) #This model will use 10 trees
    GradePredictor.fit(x, y) #Training the model
    return np.round(GradePredictor.predict(PredictionData),0) #returning the prediction as a whole number as grades cannot be decimals


