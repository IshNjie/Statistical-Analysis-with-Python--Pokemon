def Top10(Gen1,Bstat):
        subGen = Gen1[['Name','Type1', 'Type2','Total' ,'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']]
        Strong = subGen.sort_values([Bstat], ascending = False)
        print(Strong.head(10))
        return