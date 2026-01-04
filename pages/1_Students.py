import streamlit as st
from QueriesModule.SQLQueries import BaseQuery
from StudentSearch.FunctionsForSearch import *
import sqlite3 as sql
import pandas as pd


con = sql.connect('studentperformance.db')
curs = con.cursor()
Data = pd.read_sql(BaseQuery, con)[['StudentID',
                                    'SchoolName',
                                    'PlansOnHigherEducation',
                                    'FailureCount',
                                    'ExamOneGrade',
                                    'ExamTwoGrade',
                                    'ExamThreeGrade']]

st.sidebar.title('Navigation')
st.title('Search for Students')

SchoolOptions = ['Either', 'GP', 'MS'] #Options for each of the select box's
HigherEducationOptions = ['Either', 'yes', 'no']
Grades = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Inequalities = [
                '≥ Greater than or equal to',
                '> Greater than',
                '≤ Less than or equal to',
                '< Less than',
                '= Equal to',
                '≠ Not Equal to'
               ]


SelectSchool = st.selectbox(label='School', options=SchoolOptions)
SchoolName = (GetFilterValues(SelectSchool, SchoolOptions)) #This function handles if the user selects the either option

SelectHigherEducationPlans = st.selectbox(label='Higher Education', options=HigherEducationOptions)
HigherEducationPlans = (GetFilterValues(SelectHigherEducationPlans, HigherEducationOptions))

FailureCount = st.multiselect(options = [0,1,2,3], label='Failure Count', default=[0,1,2,3])
col1, col2 = st.columns(2)


with col1:
    Inequality1 = st.selectbox(label='Exam One Grade', options=Inequalities)
    Inequality2 = st.selectbox(label='Exam Two Grade', options=Inequalities)
    Inequality3 = st.selectbox(label='Exam Three Grade', options=Inequalities)

with col2:
    ExamOne = st.selectbox('Exam One Grade Value',options=Grades, label_visibility='hidden') #Labels are hidden to make page tidier
    ExamTwo = st.selectbox('Exam Two Grade Value', options=Grades, label_visibility='hidden')
    ExamThree = st.selectbox('Exam Three Grade Value', options=Grades, label_visibility='hidden')


frame = Data.loc[
                    (Data.SchoolName.isin(SchoolName[0])) #* means and in pandas, only returns the rows that meet all conditions
                    *(Data.PlansOnHigherEducation.isin(HigherEducationPlans[0]))
                    *(Data.FailureCount.isin(FailureCount))
                    *(InequalitiesCalculator(Data, 'ExamOneGrade', Inequality1, ExamOne))
                    *(InequalitiesCalculator(Data, 'ExamTwoGrade', Inequality2, ExamTwo))
                    *(InequalitiesCalculator(Data, 'ExamThreeGrade', Inequality3, ExamThree))
                ] #Inequalties calculator function converts what is selected by the user into the actual mathematical inequality



st.dataframe(frame)
st.scatter_chart(frame, x='StudentID', y='ExamThreeGrade', color="#ff4e4e") #Dynamically creates a scatter chart
with col1:
    st.metric(value=len(frame), label='Number of Students') #Metrics are calculated dynamically so update when the frame is changed
with col2:
    st.metric(value=round(frame.ExamThreeGrade.mean(), 2), label='Average Exam Three Grade')