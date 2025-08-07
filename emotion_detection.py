''' This function connects the application to watson emotion detectors.
'''
# import requests function.
import requests, json

'''This defiinition is to call the watson emotion detector API service
   and fetch a json response
'''
def emotion_detector(text_to_analyse):
    # URL to connect to watson-emotion service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # API headers for the request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # API json payload
    body = { "raw_document": { "text": text_to_analyse }}
    # trigger request of method post and capture response in response variable 
    response=requests.post(url, headers = header, json = body)
    #convert response to json using json library.
    formatted_response = json.loads(response.text)
    # return response body 
    return formatted_response