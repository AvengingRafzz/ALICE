# File to train ALICE

# Import necessary modules
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new ChatBot instance named "ALICE"
chatBot = ChatBot("ALICE")

# Create a new trainer instance for the ChatBot
trainer = ChatterBotCorpusTrainer(chatBot)

# Train the ChatBot using custom corpus data
trainer.train("chatterbot.corpus.custom")


# Define a function to get AI response
def ai_output(user_input):
    # Process the user input
    query = user_input

    # Get the AI response
    answer = chatBot.get_response(Statement(text=query, search_text=query))

    # Check if the user input contains exit keywords
    if "bye" in query or "quit" in query or "exit" in query:
        return False  # Return False to indicate exiting
    else:
        return str(answer)  # Return the AI response as a string
