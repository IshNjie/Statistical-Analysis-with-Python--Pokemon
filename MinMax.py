###### Array of stats to get info####
stats = ['Total','HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']

#### Self defined functions to find Min/Max of overall dataset ####
def maxStat(Poke, column):
    statement = ''
    for col in column:
        stat = Poke[col].max()
        name = Poke[Poke[col]==Poke[col].max()]['Name'].values[0]
        gen =  Poke[Poke[col]==Poke[col].max()]['Generation'].values[0]
        statement += name+' of Generation '+str(gen)+' has the best '+col+' stat of '+str(stat)+'.\n'
    return statement

# print(maxStat('name of dataframe','array of stats'))

def minStat(Poke, column):
    statement = ''
    for col in column:
        stat = Poke[col].min()
        name = Poke[Poke[col]==Poke[col].min()]['Name'].values[0]
        gen = Poke[Poke[col]==Poke[col].min()]['Generation'].values[0]
        statement += name+' of Generation '+str(gen)+' has the worst '+col+' stat of '+str(stat)+'.\n'
    return statement

# print(minStat('name of dataframe','array of stats'))

