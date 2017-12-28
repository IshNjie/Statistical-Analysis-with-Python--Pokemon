def Top10():
    print('Choose Generation from 1-6')
    print('\n')
    arg = input("What Generation do you wish to see the strongest Pokemon of: ")
    print('\n')
    if arg == '1':
        Bstat = input("Get the top 10 Pokemon based on the stat you provide, you can choose from 'Total' 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed' : ")
        subGen = Gen1[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
        Strong = subGen.sort_values([Bstat], ascending = False)
        print(Strong.head(10))
    elif arg == '2':
        Bstat = input("Get the top 10 Pokemon based on the stat you provide, you can choose from 'Total' 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed' : ")
        subGen = Gen2[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
        Strong = subGen.sort_values([Bstat], ascending = False)
        print(Strong.head(10))
    elif arg == '3':
        Bstat = input("Get the top 10 Pokemon based on the stat you provide, you can choose from 'Total' 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed' : ")
        subGen = Gen3[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
        Strong = subGen.sort_values([Bstat], ascending = False)
        print(Strong.head(10))
    elif arg == '4':
        Bstat = input("Get the top 10 Pokemon based on the stat you provide, you can choose from 'Total' 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed' : ")
        subGen = Gen4[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
        Strong = subGen.sort_values([Bstat], ascending = False)
        print(Strong.head(10))
    elif arg == '5':
        Bstat = input("Get the top 10 Pokemon based on the stat you provide, you can choose from 'Total' 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed' : ")
        subGen = Gen5[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
        Strong = subGen.sort_values([Bstat], ascending = False)
        print(Strong.head(10))
    elif arg == '6':
        Bstat = input("Get the top 10 Pokemon based on the stat you provide, you can choose from 'Total' 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed' : ")
        subGen = Gen6[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
        Strong = subGen.sort_values([Bstat], ascending = False)
        print(Strong.head(10))
    else:
        print('Please enter a correct entry')
        arg = input("What Generation do you wish to see the strongest Pokemon of: ")
    return