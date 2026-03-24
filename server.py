"""
server.py: Web deployment of the EmotionDetection application using Flask.
Provides routes for the home page and emotion detection API.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the main page of the emotion detection web application.
    Returns the HTML template for the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests from the web interface.
    Accepts user input text as a query parameter and returns
    a formatted string showing emotion scores and dominant emotion.
    Handles blank inputs by returning an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if not result or result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


if __name__ == "__main__":
    # Entry point for the Flask application
    # Runs the server on all network interfaces on port 5000
    app.run(host="0.0.0.0", port=5000)
    