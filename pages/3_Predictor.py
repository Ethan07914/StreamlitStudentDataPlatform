import pandas as pd
import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt
from QueriesModule.SQLQueries import BaseQuery
import sqlite3 as sql
from PredictionModels.predict import *
from ModellingFunctions.DataModelling import *

con = sql.connect('studentperformance.db')
curs = con.cursor()
Data = pd.read_sql(BaseQuery, con)

st.sidebar.title('Navigation')

st.title('Student Grade Prediction')

with st.form(key='my_form'):
 School = st.selectbox(label='What school does the student attend?', options=['MS', 'GP'])
 SchoolID = ConvertSchoolNameToID(School, Data) #Gets each the schools unique id which has been used in the training of the model

 HigherEducation = st.selectbox(label='Does the student plan on pursuing Higher Education?', options=['Yes', 'No'])
 if HigherEducation == 'Yes':
     HigherEducation = 1 #Random forest models can only compute on numeric values so it is essential for this to be converted
 else:
     HigherEducation = 0 #Converts no to zero

 FailureCount = st.slider(label='What is the students current failure count?', min_value=0, max_value=4, step=1)

 ExamOneGrade = st.slider(label='What was the students score on exam one?', min_value=0, max_value=20, step=1)

 ExamTwoGrade = st.slider(label='What was the students score on exam two?', min_value=0, max_value=20, step=1)

 Submit = st.form_submit_button(label='Submit')


 if Submit:
     col1, col2 = st.columns(2)
     PredictOn = pd.DataFrame({'SchoolID': SchoolID,
                               'PlansOnHigherEducation': HigherEducation,
                               'FailureCount': FailureCount,
                               'ExamOneGrade': ExamOneGrade,
                               'ExamTwoGrade': ExamTwoGrade})
     prediction = PredictGrade(Data, PredictOn)
     percentile = (Data[Data.ExamThreeGrade <= prediction[0]].StudentID.count() / len(Data)) * 100
     #Counts all rows with an ExamThreeGrade less than or equal to the prediction then divides that by the total number of rows and multiplies by 100 to get a percentage
     Data = Data.apply(FindEquivalent, axis=1, args=(prediction,)) #This allows us to highlight the portion of the histogram where the students predicted grade falls into
     #This is done by creating a new column and only and only setting the value to yes for the row that is equivalent to the prediction then adding a hue to the plot on that column
     fig, ax = plt.subplots() #Returns a figure and an array of axes, creates the axes for the histogram to be written on
     plt.ylabel('Students')
     sns.histplot(data=Data, x='ExamThreeGrade', hue='Equivalent', legend=False, palette='Set1') #hue on Equivalent (dynamically derived columns) causes the section of a histogram equal to the prediction to be highlighted
     #legend = False hides it so the user is unaware of how it is working in the backend system
     plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
     with col1:
      st.metric(label='Predicted Grade', value=prediction)
     with col2:
      st.metric(label='Percentile', value=round(percentile,2))

     st.pyplot(fig)






