import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sb

type1_colours= ['#6890F0',  # Water
                    '#A8A878',  # Normal
                    '#A8B820',  # Bug
                    '#78C850',  # Grass
                    '#F08030',  # Fire
                    '#F85888',  # Psychic
                    '#F8D030',  # Electric
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#A040A0',  # Poison
                    '#E0C068',  # Ground
                    '#705848',  # Dark
                    '#C03028',  # Fighting
                    '#98D8D8',  # Ice
                    '#B8B8D0',  # Steel
                    '#7038F8',  # Dragon
                    '#EE99AC',  # Fairy
                    '#A890F0',  # Flying
                   ]

type2_colours= ['#78C850',  #None
                '#A890F0',  # Flying
                '#A040A0',  # Poison
                '#E0C068',  # Ground
                '#78C850',  # Grass
                '#F85888',  # Psychic
                '#B8B8D0',  # Steel
                '#C03028',  # Fighting
                '#EE99AC',  # Fairy
                '#705848',  # Dark
                '#B8A038',  # Rock
                '#6890F0',  # Water
                '#705898',  # Ghost
                '#7038F8',  # Dragon
                '#98D8D8',  # Ice
                '#F08030',  # Fire
                '#F8D030',  # Electric
                '#A8A878',  # Normal
                '#A8B820',  # Bug  
                ]

########## SCATTER PLOT FOR ATTACK VS TOTAL ########
sb.set()
AttvTot = sb.lmplot(x='Attack', y='Total',data=Poke,
                   fit_reg = False, size = 9, aspect = 1.2) #Can Add Hue to distinguish types?
plt.ylim(150,700)
plt.xlim(0,175)
plt.title('Attack vs. Total',fontsize = 25)
plt.xlabel('Attack',fontsize = 18)
plt.ylabel('Total',fontsize = 18)
AttvTot.savefig("SP_AttvsTot.png")

####### Scatter for Sp.Def ####
sb.set()
AttvTot = sb.lmplot(x='Sp.Def', y='Total',data=Poke,
                   fit_reg = False, size = 9, aspect = 1.2) #Can Add Hue to distinguish types
plt.ylim(150,700)
plt.xlim(0,175)
plt.title('Sp.Def vs. Total',fontsize = 25)
plt.xlabel('Sp.Def',fontsize = 18)
plt.ylabel('Total',fontsize = 18)
AttvTot.savefig("SP_SpDefvsTot.png")

######## SCATTER PLOT OF ATTACK VS DEFENSE ########
sb.set()
AttvDef = sb.lmplot(x='Attack',y='Defense',data=Poke,
                   fit_reg = False, size = 9, aspect = 1.2) 
plt.title('Attack vs. Defense',fontsize = 25)
plt.xlabel('Attack',fontsize = 18)
plt.ylabel('Defense',fontsize = 18)
AttvDef.savefig("SP_AttvsDef.png")


##### VIOLIN PLOT #######
sb.set()
dims = (11.7,8.27) #A4 dimensions
fig, ax = plt.subplots(figsize=dims)
vp = sb.violinplot(x='Generation',y='Total', data=Poke, ax=ax)
plt.title('Violin plot of Generation base stat total',fontsize = 18)
plt.xlabel('Generation',fontsize = 12)
plt.ylabel('Total',fontsize = 12)
figVP = vp.get_figure()
figVP.savefig("Violin_Gen.png")


###### BOX PLOT #####
sb.set()
dims = (11.7,8.27) #A4 dimensions
fig, ax = plt.subplots(figsize=dims)
bp = sb.boxplot(x='Generation',y='Total', data=Poke, ax=ax)
plt.title('Box plot of Generation base stat total',fontsize = 18)
plt.xlabel('Generation',fontsize = 12)
plt.ylabel('Total',fontsize = 12)
figBP = bp.get_figure()
figBP.savefig("Box_Gen.png")


#########CREATING BAR PLOT FOR TYPE 1#########
Type1 = pd.value_counts(Poke['Type1'])
sb.set()
dims = (11.7,8.27) #A4 dimensions
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x=Type1.index,y=Type1,data=Poke, palette = type1_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation = 75, fontsize = 12)
BarT.set(xlabel ='Pokemon Primary Types', ylabel='Freq')
BarT.set_title('Dist. of Primary Pokemon Types')
FigBar = BarT.get_figure()
FigBar.savefig("BarPlot_PrimaryType.png")

for row in Poke.loc[Poke.Type2.isnull(), 'Type2'].index:
    Poke.at[row, 'Type2'] = 'None'

Type2 = pd.value_counts(Poke['Type2'])
sb.set()
dims = (11.7,8.27) #A4 dimensions
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x=Type2.index,y=Type2,data=Poke, palette = type2_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation = 75, fontsize = 12)
BarT.set(xlabel ='Pokemon Secondary Types', ylabel='Freq')
BarT.set_title('Dist. of Secondary Pokemon Types')
FigBar = BarT.get_figure()
FigBar.savefig("BarPlot_SecondaryType.png")


#########PIE CHART FOR TYPE 1 VS TYPE 2#########
TySplit = [Poke['Type1'].count() - Poke['Type2'].count(),Poke['Type2'].count()]
TypePie = plt.pie(TySplit,labels= ['Primary only', 'Pri and Sec'], autopct ='%1.1f%%', shadow = True, startangle = 90,explode=(0, 0.1))
plt.title('Single Type vs Dual Type Pokemon',fontsize = 12)
fig = plt.gcf()
fig.set_size_inches(11.7,8.27)
plt.savefig("TypePie.png")

#########PIE CHART FOR Legendary#########
LSplit = [Poke['Name'].count(),PokeL['Name'].count()]
LegendPie = plt.pie(LSplit,labels= ['Not Legendary', 'Legendary'], autopct ='%1.1f%%', shadow = True, startangle = 90,explode=(0, 0.1))
plt.title('Legendary Split',fontsize = 12)
fig = plt.gcf()
fig.set_size_inches(11.7,8.27)
plt.savefig("LegendPie.png")

######### HEATMAP######
Corr = Poke[['Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]

sb.set()
dims = (11.7,8.27) #A4 dimensions
fig, ax = plt.subplots(figsize=dims)
CorrelationMap = sb.heatmap(Corr.corr(),annot = True, ax = ax)
CorrelationMap.set(title = 'HeatMap to show Correlation between Base Stats')
FigMap = CorrelationMap.get_figure()
FigMap.savefig("HeatMapCorr.png")


#### Histogram####
dims = (11.7,8.27) #A4 dimensions
fig, ax = plt.subplots(figsize=dims)
Atthist = sb.distplot(Poke['Attack'],color='r',hist=False,ax=ax)
SpAhist = sb.distplot(Poke['Sp.Atk'],color = 'b', hist = False,ax=ax)
SpAhist.set(title = 'Distribution of Attack and Sp.Atk', xlabel = 'Attack:r , Sp.Atk:b')
FigHist=SpAhist.get_figure()
FigHist.savefig("Hist.png")

DS = Corr.describe()
print(DS)