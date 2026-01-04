import streamlit as st
import sqlite3 as sql
import pandas as pd
from QueriesModule.SQLQueries import BaseQuery
from Analytics.Analysis import ExamThreeGradeAnalysis
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title('Navigation')

st.title('Student Grade Analysis')

con = sql.connect('studentperformance.db')
curs = con.cursor()
Data = pd.read_sql(BaseQuery, con)

tab1, tab2, tab3, tab4 = st.tabs(['By School', 'By Higher Education Plans', 'By Failure Count', 'By Previous Exam Score'])

with tab1:
 BySchool = ExamThreeGradeAnalysis(Data, 'ocean', 'SchoolName') #object
 #Palettes from, link: https://www.practicalpythonfordatascience.com/ap_seaborn_palette

 BySchoolBox = BySchool.PlotBox()
 st.pyplot(BySchoolBox.figure)

 plt.clf() #Without this the plots are overlayed on the same chart (clears current figure)
 BySchoolStrip = BySchool.PlotStrip()
 st.pyplot(BySchoolStrip.figure)

 plt.clf()
 BySchoolMeanComparison = BySchool.PlotMeanAsBar()
 plt.ylabel('Mean ExamThreeGrade')
 plt.xlabel('SchoolName')
 st.pyplot(BySchoolMeanComparison.figure)


with tab2:
 ByEducationPlans = ExamThreeGradeAnalysis(Data, 'magma', 'PlansOnHigherEducation') #object

 plt.clf()
 ByEducationPlansBox = ByEducationPlans.PlotBox()
 st.pyplot(ByEducationPlansBox.figure)

 plt.clf()
 ByEducationPlansStrip = ByEducationPlans.PlotStrip()
 st.pyplot(ByEducationPlansStrip.figure)

 plt.clf()
 ByEducationPlansMeanComparison = ByEducationPlans.PlotMeanAsBar()
 plt.ylabel('Mean ExamThreeGrade')
 plt.xlabel('PlansOnHigherEducation')
 st.pyplot(BySchoolMeanComparison.figure)

with tab3:
 ByFailures = ExamThreeGradeAnalysis(Data, 'plasma', 'FailureCount') #object

 plt.clf()
 ByFailuresBox = ByFailures.PlotBox()
 st.pyplot(ByFailuresBox.figure)

 plt.clf()
 ByFailuresStrip = ByFailures.PlotStrip()
 st.pyplot(ByFailuresStrip.figure)

 plt.clf()
 ByFailuresMeanComparison = ByFailures.PlotMeanAsBar()
 plt.ylabel('Mean ExamThreeGrade')
 plt.xlabel('FailureCount')
 st.pyplot(ByFailuresMeanComparison.figure)

with tab4:
 plt.clf()
 ExamOne = ExamThreeGradeAnalysis(Data, None, 'ExamOneGrade').FilteredData.rename(columns={'ExamOneGrade': 'Grade'})
 ExamOne['Exam'] = 'One' #To allow for the hue

 ExamTwo = ExamThreeGradeAnalysis(Data, None, 'ExamTwoGrade').FilteredData.rename(columns={'ExamTwoGrade': 'Grade'})
 ExamTwo['Exam'] = 'Two' #Creates Exam columns and sets value equal to ExamTwoGrade for every row

 Exams = pd.concat([ExamOne, ExamTwo]) #Combines the two data frames
 st.pyplot(sns.lmplot(data=Exams, x='Grade', y='ExamThreeGrade', hue='Exam', palette='cool').figure)








