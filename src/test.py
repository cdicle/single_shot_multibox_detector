import numpy as np

from ssd import SSD300
from utils.utils import read_image
from utils.utils import resize_image
from utils.utils import preprocess_image

model = SSD300()
weights_filename = '../trained_models/model_checkpoints/weights.hdf5'
model.load_weights(weights_filename)
image_size = model.input_shape[1:3]
image_filename = '../images/008745.jpg'
image_array = read_image(image_filename)
image_array = resize_image(image_array, image_size)
image_array = image_array.astype('float32')
image_array = np.expand_dims(image_array, 0)
image_array = preprocess_image(image_array)
predictions = model.predict([image_array])
predictions = np.squeeze(predictions)
predicted_classes = predictions[: , 4:]
best_classes = np.argmax(predicted_classes, axis=1)
positive_mask = best_classes != 0


