import pandas as pd 

file = "flashcards.xlsx"
f1 = pd.read_excel(file, sheet_name = 'Vocabulaire')
f1 = f1.loc[:, ['Question', 'Rep']]
f2 = pd.read_excel(file, sheet_name = 'Grammaire')
f2.rename(columns={'Réponse':'Rep'}, inplace=True)
f2 = f2.loc[:, ['Question', 'Rep']]
f = pd.concat([f1, f2])
pd.to_csv('dataframe.csv')