''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package:
# Import the emotion_detector function from the package created:
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app= Flask("Emotion Detector")

@app.route("/emotionDetector")
def captured_text():
    ''' This code receives the text from the HTML interface and 
        runs emotion quotient over it using emotion_detector()
        function. The output returned shows the dominent emotion and all emotion scores
        for the provided text.
    '''
    test_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(test_to_detect)

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['fear']}, 'sadness': {response['sadness']}. The dominent emotion is <b>{response['dominent_emotion']}.<b>" 

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
  
    app.run(host="0.0.0.0", port=5000)
