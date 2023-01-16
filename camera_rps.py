import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

# Fuction needs to take in the prediction
# Fuction needs to find the highest value in the list of predictions
# Fuction needs to index the position of the highest value and find where that is equal to the List order, in this case Ropck, Paper Scissors Nothing, and then return that value as a string.

def get_prediction(prediction):
    user_output_choices = ["rock", "paper", "scissors", "nothing"]
    user_choice = ""
    index = prediction.argmax()
    user_choice = user_output_choices[index]
    return user_choice