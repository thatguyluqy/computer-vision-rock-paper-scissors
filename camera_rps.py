# Fuction needs to take in the prediction
# Fuction needs to find the highest value in the list of predictions
# Fuction needs to index the position of the highest value and find where that is equal to the List order, in this case Ropck, Paper Scissors Nothing, and then return that value as a string.

def get_prediction(prediction):
    user_output_choices = ["rock", "paper", "scissors", "nothing"]
    user_choice = ""
    index = prediction.argmax()
    user_choice = user_output_choices[index]
    return user_choice