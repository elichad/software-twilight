# Dictionary of questions
# Class(?)es(?) for 
# body of get_question()
# body of put_answer()
# 

Class Question():
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def get_text(self):
        return self.text

    def get_options(self):
        return list(self.options.keys())
      
    def next_step(self, option):
        # get the next question ID
        next = self.options[option]
        return next

    def get_info():
        return (self.get_text(), self.get_options())

question_returned = ("question text", question[1].keys())

# example data structure containing questions
# format is {id: question}
example={
    1: Question("example text 1",  {"option 1 ": 2, "option 2": 3}),
    2: Question("example text 2",  {"option 1 ": 2, "option 2": 3}),
    3: Question("example text 3",  {"option 1 ": 2, "option 2": 3}), 
}

answer_sheet = []

questions=example

current_question = 1

def get_question():
    """Returns:
    the text of a question,
    an iterable of options, and
    the next steps for each option."""
    #status = boolean -if False get_badge-
    q=questions[current_question]
    status = True
    return (status, q.get_info())

# should return the response and add
# the question/answer to the answer sheet
def put_answer(question_text, chosen_option):
    """ Returns status:
    Error, etc.
    More questions True/False"""
    #chosen option = string
    answer_sheet.append((current_question, chosen_option))
    q=questions[current_question]
    current_question = q.next_step(chosen_option)
    status=True
    return status
    
def get_badge():
    md_code="something"
    return md_code

def print_answers(responses):
	'''Returns a string:
	   Question1: Answer1
	   Question2: Answer2'''
	answers = []
	for item in responses:
		question, answer = item
		answers.append(str(question) + ': ' + str(answer))
	return ''.join(answers)

def reset():
    current_question = 1


#def select_badge():
  