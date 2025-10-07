# Password Strength Prediction using Machine Learning

import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample training data (you can expand this later)
passwords = [
    "password", "123456", "qwerty", "Ajay123", "Hello@123", "StrongPass@2024", 
    "MyNameIsAjay123$", "abc", "Admin@123", "Good#Pass9"
]
labels = ["weak", "weak", "weak", "medium", "medium", "strong", "strong", "weak", "medium", "strong"]

# Convert passwords to feature vectors
vectorizer = CountVectorizer(analyzer='char')
X = vectorizer.fit_transform(passwords)
y = labels

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Predict custom input
user_pass = input("\nEnter a password to test its strength: ")
user_vec = vectorizer.transform([user_pass])
prediction = model.predict(user_vec)[0]
print(f"Predicted Password Strength: {prediction.capitalize()}")