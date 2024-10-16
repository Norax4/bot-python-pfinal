from keras.models import load_model 
from PIL import Image, ImageOps  
import numpy as np

def get_class(model_path, labels_path, image_path):
   
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(model_path, compile=False)

   
    class_names = [line.strip().split(' ', 1)[1] for line in open(labels_path, "r").readlines()]

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)

    # Get the class name and confidence score
    class_name = class_names[index]
    
    # Return the predicted class and confidence score
    return (class_name)