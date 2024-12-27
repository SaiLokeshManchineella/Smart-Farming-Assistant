import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
df = pd.read_csv('Crop_recommendation1.csv')

# Features and target
X = df.drop('label', axis=1)
y = df['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=25, random_state=2)
model.fit(X_train, y_train)

# Save the model
with open('crop_recommendation_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model training completed and saved as 'crop_recommendation_model.pkl'")
