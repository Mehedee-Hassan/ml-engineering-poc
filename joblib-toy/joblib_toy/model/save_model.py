import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def run_ml_joblib_helper():
    data = load_iris()
    X = data.data  # features
    y = data.target  # labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

    #  Save the trained model using joblib
    joblib.dump(model, './cache/random_forest_model.joblib')

    #  Load the model back from the file
    loaded_model = joblib.load('./cache/random_forest_model.joblib')

    #  Test the loaded model
    y_pred_loaded = loaded_model.predict(X_test)
    print(f"Accuracy (after loading model): {accuracy_score(y_test, y_pred_loaded)}")

    #  Save and load large NumPy arrays (for example, features)
    joblib.dump(X_train, 'X_train_data.joblib')
    X_train_loaded = joblib.load('X_train_data.joblib')

    # Check if the loaded data is the same
    print(np.array_equal(X_train, X_train_loaded))  # Should return True
