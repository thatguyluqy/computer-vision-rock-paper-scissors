import cv2
import time
from keras.models import load_model
import numpy as np

def get_prediction(prediction):
    user_output_choices = ["Rock", "Paper", "Scissors", "Nothing"]
    user_choice = ""
    index = prediction.argmax()
    user_choice = user_output_choices[index]
    return user_choice

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
countdown_time = 5 # Set the countdown time in seconds
start_time = time.time() # Get the start time

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    
    #Checking the probability of the prediction
    print("Rock: ", prediction[0][0], " Paper: ", prediction[0][1], " Scissors: ", prediction[0][2], " Nothing: ", prediction[0][3])
    # Check if the countdown has finished
    current_time = time.time()
    if current_time - start_time > countdown_time:
        user_choice = get_prediction(prediction)
        print(f"You chose, {user_choice}")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
