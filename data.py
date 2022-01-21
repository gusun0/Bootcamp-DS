import numpy as np
import pandas as pd


data = pd.read_csv('users.csv', index_col='id')
#print(data)
data = data.dropna()
# mayor de 40
#data = data[data['age'] > 40]
#data2 = data.query('age > 40')['name']
#print(data)
#print(data2)

# edad > 20 y sexo femenino

#data = data[ (data['age'] > 20) & (data['gender'] == 'female')]['age']
#data2 = data.query('age > 20 and gender == "female"')
#print(data)
#print(data2)

# TODOS LOS USUARIOS CUYO CORREO NO TERMINE EN @EXAMPLE.COM
#data = data[ ~data['email'].str.endswith('@example.com')]
#print(data)


# OBTENER EL NOMBRE Y EL MAIL DE TODOS AQUELLOS USUARIOS DE PAIS GERMANY, FINLAND O CANADA

#data = data[(data['country'] =='Germany') | (data['country'] == 'Finland') | (data['country'] == 'Canada')]['name']
#data_query = data.query('country in ("Germany","Finland","Canada")')
#print(data_query)

#data = data[data['country'].isin(['Germany','Finland','Canada'])]
#data = [(data['name']) & (data['email'])]
#print(data)

# OBTENER EL NOMBRE Y EL CORREO ELECTRONICO DE TODOS LOS USUARIOS DE SEXO FEMENINO DEL PAIS GERMANY

#data = data[ (data['country'] == 'Germany') & (data['gender'] == 'female') ]
#data_query = data.query('gender == "female" and country == "Germany"')
#print(data_query)


# OBTENER LA CANTIDAD DE USUARIOS DE SEXO MASCULINO EN CANADA
#data = data[ (data['gender'].isin(['male']))  & (data['country'].isin(['Canada']))].count()
#data_query = data.query('gender == "male" and country == "Canada"')
#print(data_query)

# MOSTRAR EN CONSOLA LA CANTIDAD DE HOMBRES Y MUJERES
#data = data.groupby('gender').count()
#print(data)
# MOSTRAR EN CONSOLA EL PAIS CON MAS MUJERES

#data = data[(data['gender'] == 'female')]
#data = data.groupby('country')['country'].count().sort_values(ascending=False).head(1)
#print(data)
# OBTENER LOS 5 PAISES CON MAS USUARIOS

data = data.groupby('country')['country'].count().sort_values(ascending=False).head(5)
print(data)


