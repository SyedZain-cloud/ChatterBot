from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the chatbot
chatbot = ChatBot("LearningBot")

# Create the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train using ChatterBot's English corpus
trainer.train("chatterbot.corpus.english")
trainer.train("my_corpus/conversations.yml")
# Start chatting
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chatbot.get_response(user_input)

    print("Bot:", response.text)