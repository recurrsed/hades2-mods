# from imageai.Classification.Custom import ClassificationModelTrainer

# model_trainer = ClassificationModelTrainer()
# model_trainer.setModelTypeAsResNet50()
# model_trainer.setDataDirectory(r"D:/Programming/er-qa/monsters")

# model_trainer.trainModel(num_experiments=100, batch_size=32)

from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="monsters")
trainer.setTrainConfig(object_names_array=["monsters"], batch_size=4, num_experiments=200, train_from_pretrained_model="yolov3.pt")
trainer.trainModel()