import seaborn as sns


class ExamThreeGradeAnalysis:
    def __init__(self, BaseData, palette, xcol, ycol='ExamThreeGrade'):
        self.BaseData = BaseData
        self.palette = palette
        self.xcol = xcol
        self.ycol = ycol
        self.FilteredData = self.FilterData() #Setting the variable to the result of the function means these values are computed when a new object is initialised
        self.MeanByCategory = self.GetMeanByCategory()

    def FilterData(self):
        return self.BaseData[[self.xcol, self.ycol]] #Filters out unnecessary

    def PlotBox(self):
        return sns.boxplot(self.FilteredData, x=self.xcol, y=self.ycol, hue=self.xcol, palette=self.palette)

    def PlotStrip(self):
        return sns.stripplot(self.FilteredData, x=self.xcol, y=self.ycol, hue=self.xcol, palette=self.palette)

    def GetMeanByCategory(self):
        Means = []
        for value in self.FilteredData[self.xcol].unique(): #Iterates through each possible value in the columns
            Category = self.FilteredData.loc[self.FilteredData[self.xcol] == value] #Locates all rows equal to that value
            CategoryMean = Category[self.ycol].mean().round(2)
            Means.append(float(CategoryMean)) #Appends the value as a float to the list rather than a numpy array
        MeanDict = {'Category':list(self.FilteredData[self.xcol].unique()), 'Mean':Means} #Stores as key value pairs
        return MeanDict

    def PlotMeanAsBar(self):
        barplot = sns.barplot(x=self.MeanByCategory['Category'], y=self.MeanByCategory['Mean'], hue=self.MeanByCategory['Category'], palette=self.palette)
        for container in barplot.containers:  # link: https://www.geeksforgeeks.org/python/how-to-show-values-on-seaborn-barplot/
            barplot.bar_label(container) #Gives a label to each bar within the bar plot
        return barplot



