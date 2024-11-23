import pandas as pd

#3
# data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
# print(data_frame)

#4
# list_0 = [23,45,7,34,6,63,36,78,54,34]
# series_0 = pd.Series(list_0)
# print(series_0)

#4.1
# date_range = pd.date_range(start = "2021-05-01", end = "2021-05-12", freq='D')
# print(date_range)

#4.2
# my_series = pd.Series([2, 4, 6, 8, 10])
# half_my_series = my_series/2
# print(half_my_series)

# #5
# import pandas as pd
# # Two-dimensional array of [name, age] values
# data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]

# # Create the DataFrame and name the columns
# df = pd.DataFrame(data, columns=['Name', 'Age'])

# # Print the DataFrame
# print(df)

# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
# cols = ['Brand', 'Model', 'Color']
# df = pd.DataFrame(data, columns=cols)
# print(df)

#5.1
# data = [
#     { 
#         "brand": "Toyota", 
#         "model": "Corolla",
#         "color": "Blue",
#     },
#     {
#         "brand": "Ford", 
#         "model": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porsche", 
#         "model": "Cayenne",
#         "color": "White"
#     },
#     {
#         "brand": "Tesla",
#         "model": "Model S",
#         "color": "Red"
#     }
# ]

# df = pd.DataFrame(data)
# print(df)

#5.2
data = pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data.iloc[133,6])

#5.3
#print(data.head(3))

#5.4
#print(data.tail(3))

#5.5
#print(data[['Name','Type 1']][0:10])

#5.6
#print(data.loc[data['Attack']>80])

#5.7
#print(len(data.loc[data['Legendary']==True]))

#6
us_baby_names = pd.read_csv(".learn/assets/us_baby_names_right.csv")
#print(us_baby_names.head())

#6.1
us_baby_names = us_baby_names.drop('Unnamed: 0', axis = 1)
#print(us_baby_names.head())

#6.2
#print(us_baby_names['Gender'].value_counts())

#6.3
print(len(us_baby_names.groupby('Name').sum()))