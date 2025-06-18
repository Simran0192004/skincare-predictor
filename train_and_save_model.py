import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your dataset
df = pd.read_csv("skincare_data.csv")

# Label Encoding
le_skin = LabelEncoder()
le_climate = LabelEncoder()
le_pref = LabelEncoder()
le_product = LabelEncoder()

df["skin_encoded"] = le_skin.fit_transform(df["skin_type"])
df["climate_encoded"] = le_climate.fit_transform(df["climate"])
df["pref_encoded"] = le_pref.fit_transform(df["preference"])
df["product_encoded"] = le_product.fit_transform(df["recommendation"])

# Train model
X = df[["skin_encoded", "climate_encoded", "pref_encoded"]]
y = df["product_encoded"]
model = RandomForestClassifier()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, "skincare_model.pkl")
joblib.dump(le_skin, "le_skin.pkl")
joblib.dump(le_climate, "le_climate.pkl")
joblib.dump(le_pref, "le_preference.pkl")
joblib.dump(le_product, "le_product.pkl")

print("Model and encoders saved successfully 💚")
