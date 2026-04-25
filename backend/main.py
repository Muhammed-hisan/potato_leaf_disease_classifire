from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO

model = tf.keras.models.load_model('model_v1.keras')
class_name = ['Early Blight', 'Late Blight', 'Healthy']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_file_as_image(data):
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image, 0)
    pred = model.predict(image_batch)
    predicted_class = class_name[np.argmax(pred[0])]
    confidence = float(np.max(pred[0])) * 100
    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 2),
        "all_scores": {
            class_name[i]: round(float(pred[0][i]) * 100, 2)
            for i in range(len(class_name))
        }
    }