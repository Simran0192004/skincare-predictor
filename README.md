# 🌿 Climate-Aware Skincare Recommender

This AI-powered system recommends personalized skincare products based on:

- **Skin type & concerns**
- **Local climate factors** (temperature, humidity, UV, pollution)
- **User preferences** (e.g., natural ingredients, product form, vegan)

---

## 🧠 How It Works

1. **User Input**: Upload image/questionnaire responses (skin type, concerns, preferences).  
2. **Climate Data**: Fetch real-time weather and pollution data for the user's region.  
3. **Filtering Logic**:  
   - **Content-based filtering**: Recommends products with ingredients suited to the user's profile.  
   - **Climate adjustment**: Tweaks recommendations based on current local weather.  
4. **Results**: Outputs skincare products with explanations.

---

## 🔧 Tech Stack

- **Python**  
- **scikit-learn** for filtering logic  
- **Requests / climate API** to fetch weather/pollution  
- **Streamlit** for the user interface

---

## 🚀 Setup & Usage

```bash
git clone <repo_url>
cd climate-skincare-recommender
python3 -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
