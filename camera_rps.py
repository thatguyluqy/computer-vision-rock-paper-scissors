import cv2
import time
import random
from keras.models import load_model
import numpy as np

computer_wins = 0
user_wins = 0

def get_prediction(data):
    model = load_model('keras_model.h5')
    prediction = model.predict(data)
    user_output_choices = ["Rock", "Paper", "Scissors", "Nothing"]
    user_choice = ""
    index = prediction.argmax()
    user_choice = user_output_choices[index]
    return user_choice

def get_computer_choice():
    rps = (["Rock","Paper","Scissors"])
    computer_choice = random.choice(rps)
    return computer_choice

def get_winner(computer_choice, user_choice):
    global computer_wins
    global user_wins
    if computer_choice == "Rock" and user_choice == "Scissors":
        print("You lost")
        computer_wins += 1
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("You lost")
        computer_wins += 1
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("You lost")
        computer_wins += 1
    elif computer_choice == user_choice:
        print("It is a tie!")
    else:
        print("You won!")
        user_wins += 1

def play():
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
        cv2.imshow('frame', frame)

        # Check if the countdown has finished
        current_time = time.time()
        if current_time - start_time > countdown_time:
            user_choice = get_prediction(data)
            print(f"You chose, {user_choice}")
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)

while True:
    if computer_wins >= 3 or user_wins >= 3:
        break
    play()
    print("Computer wins:", computer_wins, "User wins:", user_wins)

if computer_wins == 3:
    print("Computer wins the game!")
else:
    print("You win the game!")
