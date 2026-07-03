import joblib

model = joblib.load("models/model.pkl")

print(type(model))
print(model)