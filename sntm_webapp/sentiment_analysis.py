from transformers import pipeline


sentiment_pipeline = None

def load_model():
    global sentiment_pipeline
    if sentiment_pipeline is None:
        sentiment_pipeline = pipeline("sentiment-analysis")


def predict(text):
    prediction = sentiment_pipeline(text)
    return prediction
