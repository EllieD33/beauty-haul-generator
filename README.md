# CFG-ProjectGroup5
# Beauty Haul Generator ✨💄

Welcome to the **Beauty Haul Generator**, an interactive Python application that crafts a personalised beauty product 
routine based on your preferences, skin type, and values. Whether you're budget-conscious or ingredient-aware, our tool 
tailors a glowing routine just for you.

---

## Features

- **Interactive CLI** with step-by-step questions
- **Custom routine generation** based:
  - Skin Type
  - Budget
  - Product interests
  - Personal values (e.g., Vegan-friendly, Eco-conscious)
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

## Installation and Configuration

1. **Clone the repository** via **SSH**, run the following:
```sh
git clone git@github.com:sirenc0de/CFG-ProjectGroup5.git
```
2. Install dependencies
```sh
pip install -r requirements.txt
```
3. Add your database password to `config.py`. Replace "PASSWORD" with your own DB password.
4. Set up the database.
   - Open your MySQL database management tool.
   - Run the `create_db.sql` script to initialise the database.
5. Run the application from `main.py`.

---
## Project Structure ##

📁 CFG-ProjectGroup5/

    config.py – 🛠️ Configuarations necessary to run the application
    
    main.py – 🚀 Entry point of the application

    README.md – 📝 Project documentation
    
    requirements.txt – 📦 List of required packages

    Group 5 Project Document.pdf - 📝 Additional project documentation

📂 api/

    routine_api.py – 🌱 Interfaces for skin-type, vegan, eco, and natural product filtering

📂 core/

    filters.py – ⚙️ Applies filtering based on user budget, product type, and ethics

    routine_display.py – 🖥️ Displays and saves the final routine

    routine_generator.py – 🔄 Generates a personalised beauty routine

    user_interactions.py – 🎯 Handles all user inputs and preference collection

📂 data/

    create_db.sql – 🗄️ Creation script for the database

    db_utils.py – 💾 Utilities for interacting with the DB

📂 models/

    products.py – 🧴 Defines the Product class and scoring logic

    user_preferences.py – ⭐ Defines the User_Preferences class 

📂 ui/

    loading_spinner.py – ⏳ CLI loading spinner to indicate activity during API calls

📂 tests/

    test_db_utils.py – ✅ Tests for database utilities

    test_filters.py – ✅ Tests for product filtering logic

    test_products.py – ✅ Tests for product class methods

    test_user_interactions.py – ✅ Tests for validating user inputs

---

## Future Roadmap

### 💡 How Reviews Influence Filtering (Planned Feature) ##

In future versions, the system will:
- Analyse product reviews for sentiment
- Boost relevance scores for positive reviews aligned with a user's skin type
- Penalise products with consistently negative feedback

This would involve scraping or importing review data and performing text classification or sentiment analysis using tools like NLTK, spaCy, or TextBlob. 


### 💡 Other features on our roadmap include:
- **User Login System:** Enable users to save/update preferences and revisit routines.
- **API Data Caching:** Improve performance and reduce API calls.
- **DB Caching:** Return past recommendations when identical inputs are detected.
- **Refined Logic:** Allow product rejection and regeneration of specific items, not the whole haul.
- **Enhanced UI/UX:** Potential GUI or web-based interface in future phases.
- **Migration to a full database:** E.g., MySQL, PostgreSQL, or Firebase. Enabling more complex queries, user authentication, and integration with a future web frontend.

---

## To Do📌

- Submit project via PR
- Update project logs
- Prepare and finalise project presentation
- **Potentially**: 
  - Integrate live product API (e.g., Makeup API)
  - Add review scraping or upload functionality 
  - Incorporate sentiment analysis for review-aware ranking
  - Build a basic web interface (Flask or Streamlit)

## 🔬Developers

Ellen Daly,
Ekum Jaswal,
Tiffany Scott-Vaughan,
Laura Wheaton,
Lauren Blayney


