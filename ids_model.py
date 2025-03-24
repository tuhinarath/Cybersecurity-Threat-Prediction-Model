import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Creating a simple dataset (normal = 0, attack = 1)
data = {
    'traffic_speed': [100, 120, 300, 90, 400, 110, 500, 80, 150, 350, 200, 250, 450],
    'packet_size': [500, 550, 1500, 480, 2000, 600, 2500, 450, 700, 1800, 1200, 1600, 2200],
    'is_attack': [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]  # 0 = normal, 1 = attack
}


# Convert to DataFrame
df = pd.DataFrame(data)

# Splitting into training and testing data
X = df[['traffic_speed', 'packet_size']]
y = df['is_attack']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = LogisticRegression()
model.fit(X_train, y_train)

# Predicting on test data
y_pred = model.predict(X_test)

# Printing accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
