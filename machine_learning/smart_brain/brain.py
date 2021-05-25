"""https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Classification/README.md"""

# from imageai.Prediction import ImagePrediction
from imageai.Classification import CustomImageClassification

import os
exection_path = os.getcwd()

prediction = ImageClassification()
# prediction = ImagePrediction()
# prediction.setModelTypeAsMobileNetV2()
prediction.setModelTypeAsResNet50()

prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0h5"))
prediction.loadModel()


predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "lion.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)