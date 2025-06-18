import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
df = pd.read_csv("skincare_data.csv")

# Encode categorical features
le_skin = LabelEncoder()
le_climate = LabelEncoder()
le_pref = LabelEncoder()
le_product = LabelEncoder()

df["skin_type_encoded"] = le_skin.fit_transform(df["skin_type"])
df["climate_encoded"] = le_climate.fit_transform(df["climate"])
df["preference_encoded"] = le_pref.fit_transform(df["preference"])
df["product_encoded"] = le_product.fit_transform(df["recommendation"])

# Define features and label
X = df[["skin_type_encoded", "climate_encoded", "preference_encoded"]]
y = df["product_encoded"]

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# 🎀 Welcome Message
print("💖 Welcome to the Skincare Product Recommender 💖")
skin_type = input("Enter your skin type (Ex: oily, dry, combination, sensitive): ").strip().lower()
climate = input("Enter your climate (Ex: humid, dry, cold, moderate): ").strip().lower()
preference = input("Enter your preference (Ex: matte, glowing, natural): ").strip().lower()

# 🛡️ Validation
if (
    skin_type not in le_skin.classes_ or
    climate not in le_climate.classes_ or
    preference not in le_pref.classes_
):
    print("\n⚠️ Invalid input. Please enter valid options exactly as mentioned in the dataset.")
else:
    # Encode user input
    skin_encoded = le_skin.transform([skin_type])[0]
    climate_encoded = le_climate.transform([climate])[0]
    pref_encoded = le_pref.transform([preference])[0]

    # Predict
    pred = model.predict([[skin_encoded, climate_encoded, pref_encoded]])[0]
    recommendation = le_product.inverse_transform([pred])[0]

    print("\n✨ Based on your skin needs, we recommend:\n")
    print(f"🧴 {recommendation}")
