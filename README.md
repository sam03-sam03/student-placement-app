# 🎓 Student Placement Predictor

A machine learning web app that predicts a student's placement likelihood 
based on CGPA, internships, and backlog history — built with scikit-learn 
and deployed live with Streamlit.

🔗 **[Try the live app here](https://student-placement-app-ykfvuqn5t9obszj8vdh8qk.streamlit.app/)**

## Overview

This project uses a logistic regression model trained on ~3,000 student 
records to predict whether a student is likely to be placed, based on 
three key factors. The model is wrapped in an interactive Streamlit app 
where anyone can input their own stats and get an instant prediction.

## Dataset

- **Source:** [Student Placement Dataset (Kaggle)]
- **Size:** 2,966 student records
- **Features:**
  - `Internships` — number of internships completed
  - `CGPA` — current CGPA
  - `HistoryOfBacklogs` — whether the student had academic backlogs
- **Target:** `PlacedOrNot` — whether the student was placed (1) or not (0)

## Approach

1. Loaded and explored the dataset (checked distribution, class balance)
2. Split data into training (80%) and testing (20%) sets
3. Trained a **Logistic Regression** model using scikit-learn
4. Evaluated performance on unseen test data
5. Analyzed feature importance to understand what drives placement
6. Built a Streamlit app for live, interactive predictions
7. Deployed the app publicly using Streamlit Community Cloud

## Results

- **Model Accuracy:** 73.4% on test data (vs. 57% baseline from always 
  predicting the majority class)
- **Feature Importance:**
  - **CGPA** had the strongest positive influence on placement
  - **Internships** also positively influenced placement, to a lesser degree
  - **History of backlogs** had a smaller negative effect

## Tech Stack

- Python
- pandas
- scikit-learn
- Streamlit
- joblib (model serialization)

## Files

| File | Description |
|---|---|
| `app.py` | Streamlit app — loads the model and serves predictions |
| `placement_model.pkl` | Trained logistic regression model |
| `requirements.txt` | Python dependencies for deployment |
| `*.ipynb` | Full analysis and model training notebook |

## Run Locally

```bash
git clone https://github.com/sam03-sam03/student-placement-app.git
cd student-placement-app
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

- Add more features (aptitude scores, communication skills, projects done)
- Try other models (Random Forest, XGBoost) for comparison
- Add confidence/probability score alongside the prediction
