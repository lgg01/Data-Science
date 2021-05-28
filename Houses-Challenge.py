import pandas as pd

data = pd.read_csv('datasets/kc_house.csv')

# 1-Quantas casas disponíveis para a compra?
# print(data.shape)
# print(len(data.id))
# print(data)
#   R:21613
# 2 - Quantos atributos as casas possuem?
#   R:21
# 3 - Quais são os atributos das casas?
# print(data.columns)
# R:'id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#   'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#   'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#   'lat', 'long', 'sqft_living15', 'sqft_lot15'],
# 4 - Qual a casa mais cara com o maio valor de venda?
#   print(data[['id', 'price']].sort_values('price', ascending=False))
#   R: Casa 6762700020, linha 7252
# 5 - Qual a casa com o maior número de quartos?
#   print(data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False))
#   R: Casa 2402100895, linha 15870
# 6 - Qual a soma de quartos do conjunto de dados?
# print(sum(data.bedrooms))
#   R:72854
# 7 - Quantas casas possuem 2 banheiros?
#   print(data[data['bathrooms']==2]['bathrooms'])
# print(len(data[data['bathrooms']==2]))
#   R:1930
# 8 - Qual o preço médio de todas as casas do conjunto de dados?
#   soma_price = sum(data.price)
#   n_houses = len(data)
#   print(soma_price/n_houses)
# print(sum(data.price) / len(data))
#   R: $540000,14
# 9 - Qual o preço médio de casas com 2 banheiros?
#   houses_2_bathrooms = data[data['bathrooms']==2]
#   houses_2_bathrooms = sum(houses_2_bathrooms.price)
#   n_houses_2_bathrooms = len(houses_2_bathrooms)
#   print(houses_2_bathrooms/n_houses_2_bathrooms)
#print(sum(data[data["bathrooms"] == 2].price) / len(data[data["bathrooms"] == 2]))  # Conta direta
#   R: 457889,72
# 10 - Qual o preço mínimo entre casas com 3 quartos?
# houses_3_bedrooms = data[]
#print(data[data['bedrooms'] == 3][['bedrooms', 'price']].sort_values('price', ascending=False))  # visualizando
#print(min(data[data["bedrooms"] == 3].price))
#   R: 82000
# 11 - Quantas casas possuem mais de 300 m2 na sala de estar?  (Aqui trocase metros por sqft)
#print(data[data['sqft_living'] > 3229.17]['sqft_living'])
#print(len(data[data["sqft_living"] > 3229.17]))
#   R:2258
# 12 - Quantas casas tem mais de 2 andares?
#print(len(data[data['floors'] > 2]))
#   R:782
# 13 - Quantas casas tem vista para o mar?
#print(len(data[data['waterfront'] == 1]))
#   R:163
# 14 - Das casas com vista para o mar, quantas têm 3 quartos?
#houses_waterfront = data[data['waterfront'] == 1]
#print(len(houses_waterfront[houses_waterfront["bedrooms"] == 3]))
#   R: 64
# 15 - Das Salas com mais de 300 m2 na salar de estar, quantas tem mais de 2 banheiros? (faz o calculo de m2 para sqft)
#big_houses = data[data["sqft_living"] > 3229.17]
#print(len(big_houses[mansoes['bathrooms'] > 2]))
#   R: 2201
