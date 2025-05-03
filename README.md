# CFG-ProjectGroup5
# Beauty Haul Generator ✨💄

Welcome to the **Beauty Haul Generator**, an interactive Python application that crafts a personalised beauty product 
routine based on your preferences, skin type, and values. Whether you're budget-conscious or ingredient-aware, our tool 
tailors a glowing routine just for you.

---

## Features

- **Interactive CLI** with step-by-step questions
- **Custom routine generation** based:
- - Skin Type
- - Budget
- - Product interests
- - Personal values (e.g., Vegan-friendly, Eco-conscious)
- **Advanced filtering** using a prioritisation algorithm
- **Save your routine** locally for future use
- **Fun, friendly UX** with emojis and spinner loading animation
- Extensible structure for future integration of **user reviews**

---

## How It Works ⭐️

1. You'll answer a few simple questions about your beauty preferences.
2. The app fetches and filters products using your answers.
3. A custom haul is displayed just for you.
4. You can choose to save it or modify your preferences.

---

## Installation

1. **Clone the repository** via **SSH**, run the following:
`git clone git@github.com:sirenc0de/CFG-ProjectGroup5.git`
2. Install dependencies:
`pip install -r requirements.txt`
3. Run the Flask application
---
## Project Structure

sirenc0de/CFG-ProjectGroup5/
│
├── main.py                        # 🚀 Entry point of the application
│
├── products.py                     # 🧴 Defines the Product class and scoring logic
├── filters.py             # ⚙️ Applies filtering based on user budget, type, ethics
├── routine_generator.py           # 🔄 Generates a personalized beauty routine
├── routine_display.py             # 🖥️ Displays and saves the final routine
├── routine_api.py                 # 🌱 Interfaces for vegan, eco, and natural product filtering
│
├── db_utils.py                    # 💾 Utility for saving routines to CSV
│
├── ui/
│   └── loading_spinner.py         # ⏳ CLI loading spinner to show progress
│
├── user_interactions.py           # 🎯 Handles all user inputs and preference collection
│
├── tests/                          # ✅ Unit tests (expandable for future use)
│   └── test_products.py            #   - Tests for product filtering logic
│
├── data/                          # 📊 Stores saved user routines
│   └── user_routines.csv          #   - CSV file generated from user sessions
│
├── requirements.txt               # 📦 List of required packages (if any)
└── README.md                      # 📝 Project documentation
---

## 💡How Reviews Influence Filtering (Planned Feature) ##

In future versions, the system will:
- Analyse product reviews for sentiment
- Boost relevance scores for positive reviews aligned with a user's skin type
- Penalise products with consistently negative feedback

This would involve scraping or importing review data and performing text classification or sentiment analysis using tools like NLTK, spaCy, or TextBlob. 

---

## To Do📌

- Submit project via PR
- Update project logs
- Prepare and finalise project presentation
- **Potentially**: 
- - Integrate live product API (e.g., Makeup API)
- - Add review scraping or upload functionality 
- - Incorporate sentiment analysis for review-aware ranking
- - Build a basic web interface (Flask or Streamlit)

## 🔬Developers

Ellen Daly,
Ekum Jaswal,
Tiffany Scott-Vaughan,
Laura Wheaton,
Lauren Blayney


