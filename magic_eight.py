def ask_question():
	response = input("What is your question? Enter 'quit' to quit.")
	while response != "quit":
		if response[-1] != "?":
			print("I'm sorry, I can only answer questions.")
			response = input("Please input a question this time.")
		response = input("What is your question? Enter 'quit' to quit.")
	return response

