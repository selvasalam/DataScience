import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# Read and clean
food = pd.read_csv("food_data.csv")
food.columns = food.columns.str.strip()  # remove spaces just in case
print("Columns:", food.columns)  # check columns

# Split data
x = food[["sweetness", "crunchiness"]]
y = food["Food Type"]

# Scale features
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

# Predict for tomato
tomato = pd.DataFrame({"sweetness": [4], "crunchiness": [6]})
tomato_scaled = scaler.transform(tomato)

# Train and predict
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_scaled, y)
prediction = knn.predict(tomato_scaled)

print("The predicted food type:", prediction[0])
