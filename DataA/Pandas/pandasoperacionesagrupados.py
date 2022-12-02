import numpy as np
import pandas as pd

ratings = pd.read_csv(r'C:\Users\franc\PycharmProjects\estudios\DataA\Pandas\ratings.csv')
peliculas = pd.read_csv(r'C:\Users\franc\PycharmProjects\estudios\DataA\Pandas\peliculas.csv')
usuarios = pd.read_csv(r'C:\Users\franc\PycharmProjects\estudios\DataA\Pandas\usuarios.csv')

print(ratings.columns)
print(peliculas.columns)
print(usuarios.columns)

peli_ratings = pd.merge(peliculas,ratings)

clasif = pd.merge(peli_ratings,usuarios)

mas_ratings = clasif.groupby('titulo').size().sort_values(ascending=False)[:25]
print(mas_ratings)

#.agg() aplicar una lista de funciones en columnas especificas
#promedio de cada pelicula
peli_stats = clasif.groupby('titulo').agg({'rating':[np.size,np.mean]})
print(peli_stats.head())

print(peli_stats.sort_values([('rating','mean')],ascending=False).head())

minimo_100 = peli_stats['rating']['size'] >= 100
print(minimo_100)

print(peli_stats[minimo_100].sort_values([('rating','mean')],ascending=False)[:25])
