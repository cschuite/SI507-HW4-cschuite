import random

def ask_question():
	response = input("What is your question? Enter 'quit' to quit.")
	while response != "quit":
		response = input("What is your question? Enter 'quit' to quit.")
		if response[-1] != "?":
			print("I'm sorry, I can only answer questions.")
			response = input("Please input a question this time.")
		answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
		print(answers[random.randrange(21)])
print(ask_question())





