def Weakness(Gen1):
    arg2 = input("Choose a Type to find the 6 best Pokemon to combat it: ")
    print('\n')
    Bstat = input("Choose a Base stat to sort the strongest Pokemon by: 'Total' 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed' : ")
    print('\n')
    if arg2 == 'Water':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Grass') ^ (Gen1['Type1']=='Electric') ^ 
                                (Gen1['Type2'] == 'Grass') ^ (Gen1['Type2']=='Electric')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Normal':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Fighting') ^ 
                                (Gen1['Type2'] == 'Fighting')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Fire':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Water') ^ (Gen1['Type1']=='Ground') ^ (Gen1['Type1']=='Rock') ^ 
                                (Gen1['Type2'] == 'Water') ^ (Gen1['Type2']=='Ground') ^ (Gen1['Type2']=='Rock')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Electric':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Ground') ^ 
                                (Gen1['Type2'] == 'Ground')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Grass':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Fire') ^ (Gen1['Type1']=='Ice') ^ (Gen1['Type1']=='Poison') ^ (Gen1['Type1'] == 'Flying') ^ (Gen1['Type1']=='Bug') ^ 
                                (Gen1['Type2'] == 'Fire') ^ (Gen1['Type2']=='Ice') ^ (Gen1['Type2']=='Poison') ^ (Gen1['Type2'] == 'Flying') ^ (Gen1['Type2']=='Bug')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Ice':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Fire') ^ (Gen1['Type1']=='Fighting') ^ (Gen1['Type1']=='Rock') ^ (Gen1['Type1'] == 'Steel') ^ 
                                (Gen1['Type2'] == 'Fire') ^ (Gen1['Type2']=='Fighting') ^ (Gen1['Type2']=='Rock') ^ (Gen1['Type2'] == 'Steel')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Fighting':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Flying') ^ (Gen1['Type1']=='Psychic') ^ (Gen1['Type1']=='Fairy') ^ 
                                (Gen1['Type2'] == 'Flying') ^ (Gen1['Type2']=='Psychic') ^ (Gen1['Type2']=='Fairy')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Poison':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Ground') ^ (Gen1['Type1']=='Psychic') ^ 
                                (Gen1['Type2'] == 'Ground') ^ (Gen1['Type2']=='Psychic')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Ground':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Water') ^ (Gen1['Type1']=='Grass') ^ (Gen1['Type1']=='Ice') ^ 
                                (Gen1['Type2'] == 'Water') ^ (Gen1['Type2']=='Grass') ^ (Gen1['Type2']=='Ice')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Flying':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Electric') ^ (Gen1['Type1']=='Ice') ^ (Gen1['Type1']=='Rock') ^ 
                                (Gen1['Type2'] == 'Electric') ^ (Gen1['Type2']=='Ice') ^ (Gen1['Type2']=='Rock')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Psychic':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Bug') ^ (Gen1['Type1']=='Ghost') ^ (Gen1['Type1']=='Dark') ^ 
                                (Gen1['Type2'] == 'Bug') ^ (Gen1['Type2']=='Ghost') ^ (Gen1['Type2']=='Dark')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Bug':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Fire') ^ (Gen1['Type1']=='Flying') ^ (Gen1['Type1']=='Rock') ^ 
                                (Gen1['Type2'] == 'Fire') ^ (Gen1['Type2']=='Flying') ^ (Gen1['Type2']=='Rock')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Rock':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Water') ^ (Gen1['Type1']=='Grass') ^ (Gen1['Type1']=='Fighting') ^ (Gen1['Type1'] == 'Ground') ^ (Gen1['Type1']=='Steel') ^ 
                                (Gen1['Type2'] == 'Water') ^ (Gen1['Type2']=='Grass') ^ (Gen1['Type2']=='Fighting') ^ (Gen1['Type2'] == 'Ground') ^ (Gen1['Type2']=='Steel')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Ghost':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Ghost') ^ (Gen1['Type1']=='Dark') ^ 
                                (Gen1['Type2'] == 'Ghost') ^ (Gen1['Type2']=='Dark')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Dragon':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Ice') ^ (Gen1['Type1']=='Dragon') ^ (Gen1['Type1']=='Fairy') ^ 
                                (Gen1['Type2'] == 'Ice') ^ (Gen1['Type2']=='Dragon') ^ (Gen1['Type2']=='Fairy')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Dark':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Figthing') ^ (Gen1['Type1']=='Bug') ^ (Gen1['Type1']=='Fairy') ^ 
                                (Gen1['Type2'] == 'Fighting') ^ (Gen1['Type2']=='Bug') ^ (Gen1['Type2']=='Fairy')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Steel':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Fire') ^ (Gen1['Type1']=='Fighting') ^ (Gen1['Type1']=='Ground') ^ 
                                (Gen1['Type2'] == 'Fire') ^ (Gen1['Type2']=='Fighting') ^ (Gen1['Type2']=='Ground')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    elif arg2 == 'Fairy':
            Weakness = Gen1.loc[(Gen1['Type1'] == 'Poison') ^ (Gen1['Type1']=='Steel') ^ 
                                (Gen1['Type2'] == 'Poison') ^ (Gen1['Type2']=='Steel')]
            subGen = Weakness[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
            Strong = subGen.sort_values([Bstat], ascending = False)
            print(Strong.head(6))
    return