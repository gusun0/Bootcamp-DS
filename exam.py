import pandas as pd

data = pd.read_csv('users.csv')
#print(data)

# mostrar en consola todos los usuarios que no poseen email
#data = data[data['email'].isnull() ][['name','age']]
#print(data)

# listar el nombre y correo de los usuarios mas jovenes de germany y canada

#data = data[data['country'].isin(['Germany','Canada'])]
#data = data.query('age < 30')[['name','email']]
#print(data)

# mostrar los 5 paises con mayor cantidad de usuarios
#data = data.groupby('country')['country'].count().sort_values(ascending=False)[:5]
#print(data)

# obtener el pais con mas usuarios
#data = data.groupby('country')['country'].count().sort_values(ascending=False).head(1)
#print(data)

# obtener el pais con mas usuarios cuya edad sea mayor a 50
#data = data[data['age'] > 50]['country'].count()
#print(data)

# obtener la suma total de todos los usuarios de canada y alemania
data = data[data['country'].isin(['Canada','Germany'])].count().age()
print(data)


