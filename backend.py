# Dictionary of questions
# Class(?)es(?) for 
# body of get_question()
# body of put_answer()
# 




class Question:
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

questions = {
	"1" : Question("Has the project a fixed end date", {"Yes": 2, "(No)": None}),
    "2" : Question("Is there a single developer/maintainer of the project?", {"Yes": 3, "(No)": None}),
    "3" : Question("Is there secured funding to cover ongoing support", {"(Yes)": None, "No": 4}),
    "4" : Question("Do you hope to secure funding to cover ongoing support?", {"Yes": 5, "(No)": None}),
    "5" : Question("What type of ongoing maintenence do you intend to provide?", {"(Answer queries)": None, "(Implement requested features)": None, "Review merge requests": None, "(Curate issues page)": None})
}

#question_returned = ("question text", question[1].keys())



# example data structure containing questions
# format is {id: question}
#example = {
#    1: Question("example text 1",  {"option 1 ": 2, "option 2": 3}),
#    2: Question("example text 2",  {"option 1 ": 2, "option 2": 3}),
#    3: Question("example text 3",  {"option 1 ": 2, "option 2": 3}), 
#}

answer_sheet = []

questions=example

current_question = 1

def get_question():
    """Returns:
    the text of a question,
    an iterable of options, and
    the next steps for each option."""
    #status = boolean -if False get_badge-
    q = questions[str(current_question)]
    if current_question == None:
      status = False
    else:
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
    q = questions[str(current_question)]
    current_question = q.next_step(chosen_option)
    if current_question == None:
      status = False
    else:
      status = True
    return status
    
def get_badge():
    return get_badges()

def get_badges():
    md_code = "[![Twilight Date](https://github.com/elichad/software-twilight/blob/main/twilight_date_example.svg)](https://github.com/elichad/software-twilight)\n[![Twilight Date](https://github.com/elichad/software-twilight/blob/main/twilight_plan_example.svg)](https://github.com/elichad/software-twilight)"
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
  