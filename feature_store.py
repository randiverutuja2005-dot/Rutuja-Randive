# Feature Store Creation

feature_store = {}

# Feature Registration
features = {
    "name": "Rutuja",
    "age": 21,
    "marks": 85
}

feature_store["student1"] = features

# Data Ingestion
print("Data Stored Successfully")

# Online Retrieval
print("Online Retrieval:")
print(feature_store["student1"])

# Offline Retrieval
print("Offline Retrieval:")
for key, value in feature_store.items():
    print(key, value)

# Feature Reusability
print("Student Marks:", feature_store["student1"]["marks"])
