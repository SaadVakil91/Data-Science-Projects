# =============================================================================
# Spiced Academy: Data Science Bootcamp Course
# Week 1 Project: Visual Data Analysis in Python
# Summary: To show the evolution of Life Expectancy vs Fertility Rate from 1960 to 2015
# Author: Saad Vakil
# Date 16 May 2021
# =============================================================================

# Importing required python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio
import seaborn as sns

# Reading the dataset
# life-expectancy (le) dataset
df_le = pd.read_excel("C:/Users/saadv/Desktop/Spiced/sumac-sample-student-code/week_1/data/gapminder_lifeexpectancy.xlsx",index_col=0,nrows=260)
# population (p) dataset
df_p = pd.read_excel("C:/Users/saadv/Desktop/Spiced/sumac-sample-student-code/week_1/data/gapminder_population.xlsx",sheet_name="Data",index_col=0)
# fertility (f) dataset
df_f = pd.read_csv("C:/Users/saadv/Desktop/Spiced/sumac-sample-student-code/week_1/data/gapminder_total_fertility.csv",index_col=0)


# Tidying the dataset and making all the datasets the same format
df_f.shape
df_le.shape
df_f.columns #fertility dataset has columns type as object, to convert to integer since column consists of years
df_f.columns = df_f.columns.astype(int)
df_f.index.name = "country"
df_f = df_f.reset_index()
df_f = df_f.melt(id_vars="country",var_name="year", value_name="fertility_rate") #Converting to long format
df_le.columns
df_le.reset_index()
df_le.index.name = "country"
df_le = df_le.reset_index()
df_le = df_le.melt(id_vars="country",var_name="year",value_name="life_expectancy") #Converting to long format
df_p.shape #population dataset has extra blank rows. removing it below!
df_p = df_p.iloc[:260,:] #population dataset has extra blank rows. removing it below!
df_p.columns #has blank columns removing it below!
df_p.drop(['Unnamed: 82', 'Unnamed: 83', 'Unnamed: 84',
       'Unnamed: 85', 'Unnamed: 86', 'Unnamed: 87', 'Unnamed: 88',
       'Unnamed: 89', 'Unnamed: 90', 'Unnamed: 91'],axis=1,inplace=True)
df_p.shape
df_p = df_p.reset_index()
df_p = df_p.rename(columns={"Total population":"country"})
df_p = df_p.melt(id_vars="country",var_name="year",value_name="population")

# Adding continents column in the life expectancy dataset
df_continents = pd.read_csv("C:/Users/saadv/Desktop/Spiced/sumac-sample-student-code/week_1/data/countryContinent.csv", encoding="ISO-8859-1")
df_continents= df_continents.rename(columns={"Country":"country"})
df_le = pd.merge(df_le,df_continents,how="left",on="country")

# Checking the shape of the datasets before merging
df_f.shape
df_le.shape
df_p.shape

# Mergin the fertility, population and lifeexpectancy dataset
df = pd.merge(df_f,df_le,how="outer",on=["country","year"])
df1 = pd.merge(df,df_p,how="outer",on=["country","year"])

# Creating a subset of the fulldataset since there are lots of missing values before 1960
df2 = df1.copy()
df2_subset = df2.loc[(df2["year"] >= 1960) & (df2["year"] <= 2015)]

# Creating and saving the plots of the life expectancy dataset
color_dict = dict({'Africa': "#96bb7c",
                  'Asia': "#583d72",
                  'Europe': '#a9294f',
                  'Oceania': '#03c4a1',
                   'Americas': '#fa9905'}) #Assigning colors for each of the continents to be used in the scatter plot

for i in range(1960,2016): #looping through 1960 to 2015 in order to generate the plots and save for each year
    plt.figure(figsize=(20,8))
    g = sns.scatterplot(x="fertility_rate",y="life_expectancy",size="population",palette=color_dict,sizes=(50,1000),hue="Continent",data=df2_subset[df2_subset["year"]==i],alpha=0.6)
    h,l = g.get_legend_handles_labels()
    plt.legend(h[1:6],l[1:6],title="Continents", loc="lower right", borderaxespad=0.5,frameon=True,fontsize=15,title_fontsize=15)
    plt.axis((0.5,10,0.5,90))
    plt.title("Life Expectancy vs Fertility Rate ("+str(i)+")",fontsize=20)
    sns.set_style('ticks')
    plt.xlabel("Fertility Rate",fontsize=15)
    plt.ylabel("Life Expectancy (years)",fontsize =15)
    plt.savefig("C:/Users/saadv/Desktop/Spiced/sumac-sample-student-code/week_1/plots/lifeexp_"+str(i)+".png")
    plt.close()
    
# Creating an animated graph using the imageio library
images = []
for i in range(1960,2016):
    filename = "C:/Users/saadv/Desktop/Spiced/sumac-sample-student-code/week_1/plots/lifeexp_"+str(i)+".png"
    images.append(imageio.imread(filename))
imageio.mimsave("C:/Users/saadv/Desktop/Spiced/sumac-sample-student-code/week_1/LifeExp_vs_Fertility_animation.gif",images,fps=5)