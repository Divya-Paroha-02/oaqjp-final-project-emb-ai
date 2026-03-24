import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions from text using Watson NLP EmotionPredict API.
    Returns a dictionary of emotion scores and dominant emotion.
    Handles blank input with status_code = 400.
    """

    # If blank input, simulate API 400 response
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload)

    # Handle status_code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse JSON
    data = response.json()
    emotions = data.get('text', {})

    # Extract individual scores
    anger = emotions.get('anger')
    disgust = emotions.get('disgust')
    fear = emotions.get('fear')
    joy = emotions.get('joy')
    sadness = emotions.get('sadness')

    # Determine dominant emotion
    dominant_emotion = max(
        [('anger', anger), ('disgust', disgust), ('fear', fear), ('joy', joy), ('sadness', sadness)],
        key=lambda x: x[1]
    )[0]

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }