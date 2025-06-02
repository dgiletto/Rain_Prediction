import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def train_and_predict_rainfall(test_input):
    """
    Trains an SVC model on weather data and predicts rainfall.
    
    Args:
        test_input (list or array-like): New input [temperature, humidity, wind_speed, 
                                         precipitation, cloud_cover, pressure] for prediction.
    
    Returns:
        bool: Says whether or not it will rain tomorrow
    """
    # Load Dataset
    df = pd.read_csv('usa_rain_prediction_dataset_2024_2025.csv')

    # Select features and target
    features = df.drop(['Date','Location', 'Rain Tomorrow'], axis=1)
    target = df['Rain Tomorrow']

    # Split Dataset
    X_train, X_val, y_train, y_val = train_test_split(features, target, test_size=0.2, stratify=target, random_state=2)

    # Normalize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)

    # Train SVC Model
    model = SVC(kernel='rbf', probability=True)
    model.fit(X_train, y_train)

    # Predict on given data
    test_scaled = scaler.transform([test_input])
    prediction = model.predict(test_scaled)[0]

    if prediction:
        return True
    return False