from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib


MODEL_PATH = "../models/anomaly_model.pkl"


def train_model(features):

    df = pd.DataFrame(
        features,
        columns=[
            "ip",
            "failed",
            "success"
        ]
    )

    X = df[
        [
            "failed",
            "success"
        ]
    ]

    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    model.fit(X)

    joblib.dump(
        model,
        MODEL_PATH
    )

    return model


def load_model():

    return joblib.load(
        MODEL_PATH
    )


def detect_anomalies(
    features
):

    model = load_model()

    df = pd.DataFrame(
        features,
        columns=[
            "ip",
            "failed",
            "success"
        ]
    )

    X = df[
        [
            "failed",
            "success"
        ]
    ]

    predictions = model.predict(X)

    df["anomaly"] = predictions

    return df