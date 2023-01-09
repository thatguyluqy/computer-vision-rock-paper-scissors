# Computer Vision RPS

## Outline of scope
Through this project ill be using google's teachable machine tensor flow model to learn to detect hand positions of rock paper and scissors to be able to identify which pose the user is displaying. ill then create a python program that will randomly select one of these states and then challenge the user. the program will then compare the user input to the computers randomly selected position, and decide the outcome as a win, lose or draw based on the rules of rock paper scissors. 

## Teachable Machine 

the program will utilise machine learning via teachable machine and logic based code using python and fuse the two. so far i have created 4 states.

Rock - a collection of images with the hand gesture
Paper - a collection of images with the paper gesture
Scissors - a collection of immages with the scissors gesture
Nothing - a collection of images with no gesture.

ive then downloaded the model, and pushed it to my repository on github.

## Coding the python logic

Now that the model is generated its time to move on to writing some python code for the rock paper scissors game.

## Getting the computers choice

first i created a function that defines the computers choice, to do this the function has a list of the three possible choice (rock, paper, scissors) i then imported the random module, selected the choice function and past in the list. i set a variable as computer choice and assigned the output of the above function to the variable, i then closed out the function by returning the variable.

## Getting the users choice

next i needed a way to take in the users choice and assign it to a variable. i creadted a funtion that prompts the user to either enter rock paper or scissors and then store that input to a variable called user choice and return it.

## Creating the logic for all possible outcomes

next was to create a function to decide the winner. as there are three possible options for the computer to make and three for the user that leaves us with nine possible outcomes (3 choices x 3 choices = 9 possible outcomes)


there are three out comes where the user can tie, three where they can win and three where the user will lose. using if and elseif statements i outlined the three scenarious where the user would lose

    if computer_choice == "Rock" and user_choice == "Scissors":
        print("You lost")
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("You lost")
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("You lost")

after these there are three outcomes that lead to a tie, and thats when both the user and computer choice are equal so that line of code simply states in user choice == to computer choice print "its a tie"
    elif computer_choice == user_choice:
        print("It is a tie!")

and then finally the last three outcomes left can only be if the user wins so its just an else staement to print you win

    else:
        print("You won!")

this simple logic can be seen in a basic flow diagram 

if the outcome is one of the first three situations then the user has lost -> if its the situation where user and computer choices are equal then the user has tied -> in all other circumstances user has won.

finally i  created a function called play which just ties the functions together and in order.
get the user choice then get the computer choice, outline every outcome and print the result.