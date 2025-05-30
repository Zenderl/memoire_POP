from pandas import read_csv
import sqlite3

fichier_import = './metier_export.csv'
cle_primaire = 'pk_metier'
table = 'metier'


df = read_csv(fichier_import, sep=';')

df.set_index(cle_primaire)

print(df.head())

connection = sqlite3.connect('C:/Users/LZender/Documents/Travail/unine/histoire/mémoire/AEN/grand_conseil/memoire_POP/liste_grand_conseil.db')

df.to_sql(table, connection, if_exists='replace', index=False)