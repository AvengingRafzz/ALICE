# File to display a welcome message and wish the user as per system time

# Import necessary module
import datetime


# Define a function to generate a welcome message and wish the user as per system time
def wish_me():
    # Define the welcome message
    welcome = ("Hi, I am ALICE, your personal assistant."
               # "ALICE stands for Automated Listening and Interactive Chat Engine"
               " What can I help you with?")

    # Get the current hour from system time
    current_hour = datetime.datetime.now().hour

    # Determine the appropriate wish based on the current hour
    if 0 <= current_hour < 12:
        wish = "Good Morning."
    elif 12 <= current_hour < 18:
        wish = "Good Afternoon."
    else:
        wish = "Good Evening."

    # Return the wish message concatenated with the welcome message
    return str(wish + " " + welcome)
