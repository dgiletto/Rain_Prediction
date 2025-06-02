# Rainfall Prediction
Rainfall prediction classifier which uses features such as temperature, wind speed, cloud cover, etc. to determine if it will rain tomorrow. Within the project is a notebook which compares an XGB classifier, Support Vector Classifier, and a Logistic Regressor to see which has the best performance. I then picked one of the models (The Support Vector Classifier) and created a website where users can enter features to determine if it will rain the next day or not!
# Dataset
[USA Rainfall Prediction](https://www.kaggle.com/datasets/waqi786/usa-rainfall-prediction-dataset-2024-2025?resource=download)
# Link
- This is a link to the website to run the SVC function and predict whether or not it will rain the next day. It is a little slow so be patient when running it, this is due to the fact it has to train the model first on a large dataset then make a prediction. I used netlify to run the frontend (index.html), then I used render to run the backend fastapi.
- [Website](https://venerable-lily-35c7fc.netlify.app/)
