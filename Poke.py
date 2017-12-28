# i) IMPORT lIBRARIES
import pandas as pd # To read csv
import re # Regex
import seaborn as sb # Statistical data visualization
import matplotlib.pyplot as plt


# 1) SETTING UP DATA FRAME AND CLEAN DATA
frame = pd.read_csv('Pokemon.csv') # Read csv into dataframe

###### RENAME FIELDS ######
frame = frame.set_index('#')
frame.columns = ['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed', 'Generation', 'Legendary']
#####Name infront of Mega and Primal needs to be removed.. HoopaHoopa => Hoopa#####
frame.Name = frame.Name.apply(lambda x: re.sub(r'(.+)(Mega.+)',r'\2',x))
frame.Name = frame.Name.apply(lambda x: re.sub(r'(.+)(Primal.+)',r'\2',x))
frame.Name = frame.Name.apply(lambda x: re.sub(r'(HoopaHoopa)(.+)','Hoopa'+r'\2',x))

####Pokemon with Mega or Primal need to be removed. Notice Mega space => Meganium
All = frame.loc[(frame['Name'].str.contains('Mega ')==False) & (frame['Name'].str.contains('Primal')==False)] # filter all pokemon without Mega and Primal in name
Poke = All.loc[(All['Legendary']==False)]
PokeL = All.loc[(All['Legendary']==True)]

Poke['Type1'].count() - Poke['Type2'].count() #  Amount of Pokemon with only 1 type

###### Each Gen has own data frame####
Gen1 = Poke.loc[Poke['Generation'] == 1]
Gen2 = Poke.loc[Poke['Generation'] == 2]
Gen3 = Poke.loc[Poke['Generation'] == 3]
Gen4 = Poke.loc[Poke['Generation'] == 4]
Gen5 = Poke.loc[Poke['Generation'] == 5]
Gen6 = Poke.loc[Poke['Generation'] == 6]

####### Strongest from each Gen based on any stat #######
# See Strong py file 


### See Attack vs Total scatter plot ### => Seems to be correlation? 
