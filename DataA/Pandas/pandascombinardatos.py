import numpy as np
import pandas as pd

clima_p = pd.read_csv(r'C:\Users\franc\PycharmProjects\estudios\DataA\Pandas\ny_precipitaciones.csv')
print(clima_p.shape)
print(clima_p.head())

clima_t = pd.read_csv(r'C:\Users\franc\PycharmProjects\estudios\DataA\Pandas\ny_temperaturas.csv')
print(clima_t.shape)

print(clima_p.NAME)

precip_ithaca = clima_p[clima_p["NAME"] == "ITHACA CORNELL UNIVERSITY, NY US"]
print(precip_ithaca.shape)

#merge un inerjoin de los datas frames (interseccion de elementos comunes)

ithaca_inner_merge = pd.merge(precip_ithaca,clima_t)
print(ithaca_inner_merge.shape)

print(ithaca_inner_merge.head())

ithaca_outer_merge = pd.merge(precip_ithaca,clima_t,how='outer',on=["STATION","DATE"])
print(ithaca_outer_merge.columns)
print(ithaca_outer_merge.shape)

#left join

ithaca_left_merge = pd.merge(precip_ithaca,clima_t,
                             how='left',on=["STATION","DATE"])
print(ithaca_left_merge.shape)

#right join
ithaca_right_merge = pd.merge(precip_ithaca,clima_t,
                             how='right',on=["STATION","DATE"])
print(ithaca_right_merge.shape)



# .join()

#clima_t.join(clima_p)

clima_join = clima_t.join(clima_p,lsuffix='_left')#lsuffix coincidencia de indice
print(clima_join.head())
print(clima_join.columns)

clima_p.set_index(["STATION",'DATE'])
print(clima_p)

clima_joined_total = clima_t.join(clima_p.set_index(["STATION",'DATE']),
                                  lsuffix="_x",
                                  rsuffix="_y",
                                  on=["STATION",'DATE'],)
print(clima_joined_total.head())
for i in clima_joined_total.columns:
    print(i)

#concatenar 2 dataframe
clima_total_outer_concat = pd.concat([clima_t,clima_p],axis=1)#aniade las filas a la derecha
print(clima_total_outer_concat.shape)
print(clima_total_outer_concat.head())

clima_total_outer_concat = pd.concat([clima_t,clima_p],axis=0)#aniade las filas abajo
print(clima_total_outer_concat.shape)
print(clima_total_outer_concat.head())

df_jerar = pd.concat([clima_t,clima_p],keys=['temp','precip'])
print(df_jerar)