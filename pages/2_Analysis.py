import streamlit as st
import sqlite3 as sql
import pandas as pd
from QueriesModule.SQLQueries import BaseQuery
from Analytics.Analysis import ExamThreeGradeAnalysis
import matplotlib.pyplot as plt

st.sidebar.title('Navigation')

st.title('Student Grade Analysis')

con = sql.connect('studentperformance.db')
curs = con.cursor()
Data = pd.read_sql(BaseQuery, con)

tab1, tab2, tab3 = st.tabs(['Grade Analysis by School', 'Grade Analysis by Higher Education Plans', 'Grade Analysis by Failure Count'])

with tab1:
 BySchoolBox = ExamThreeGradeAnalysis(Data, 'SchoolName').PlotBox()
 st.pyplot(BySchoolBox.figure)
 plt.clf() #Without this the plots are overlayed on the same chart (clears current figure)
 BySchoolStrip = ExamThreeGradeAnalysis(Data, 'SchoolName').PlotStrip()
 st.pyplot(BySchoolStrip.figure)
 plt.clf()
 BySchoolMeanComparison = ExamThreeGradeAnalysis(Data, 'SchoolName').PlotMeanAsBar()
 plt.ylabel('Mean ExamThreeGrade')
 plt.xlabel('SchoolName')
 st.pyplot(BySchoolMeanComparison.figure)


with tab2:
 plt.clf()
 ByEducationPlansBox = ExamThreeGradeAnalysis(Data, 'PlansOnHigherEducation').PlotBox()
 st.pyplot(ByEducationPlansBox.figure)
 plt.clf() #Without this the plots are overlayed on the same chart
 ByEducationPlansStrip = ExamThreeGradeAnalysis(Data, 'PlansOnHigherEducation').PlotStrip()
 st.pyplot(ByEducationPlansStrip.figure)
 plt.clf()
 ByEducationPlansMeanComparison = ExamThreeGradeAnalysis(Data, 'PlansOnHigherEducation').PlotMeanAsBar()
 plt.ylabel('Mean ExamThreeGrade')
 plt.xlabel('PlansOnHigherEducation')
 st.pyplot(BySchoolMeanComparison.figure)

with tab3:
 plt.clf()
 ByFailuresBox = ExamThreeGradeAnalysis(Data, 'FailureCount').PlotBox()
 st.pyplot(ByFailuresBox.figure)
 plt.clf() #Without this the plots are overlayed on the same chart
 ByFailuresStrip = ExamThreeGradeAnalysis(Data, 'FailureCount').PlotStrip()
 st.pyplot(ByFailuresStrip.figure)
 plt.clf()
 ByFailuresMeanComparison = ExamThreeGradeAnalysis(Data, 'FailureCount').PlotMeanAsBar()
 plt.ylabel('Mean ExamThreeGrade')
 plt.xlabel('FailureCount')
 st.pyplot(ByFailuresMeanComparison.figure)






