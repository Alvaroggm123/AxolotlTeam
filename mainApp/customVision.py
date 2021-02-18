from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import time
from decouple import config


# Replace with valid values
def customVisionPrediction(imageUrl):
    ENDPOINT = config("ENDPOINT")
    prediction_key = config("prediction_key")

    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

    results = predictor.classify_image_url(
        config("project_id"), config("iteration_name"), imageUrl)
    resultsPrediction = ""
    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
        formated =  "{0:.2f}".format(prediction.probability * 100)
        resultsPrediction += f"<div>{prediction.tag_name}: {str(formated)} %</div>"

    return resultsPrediction