class Question:

    def __init__(self, question, choices=None, allow_text=False):

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:

    def __init__(self, title, instructions, questions):

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "Customer  Survey",
    "Please fill out the survey about your experience with our company.",
    [
        Question("Have you shopped with us before?"),
        Question("Did someone else shop with you?"),
        Question("On average, how much do you spend on basketballs?",
                 ["Less than $500", "$5,000 or more"]),
        Question("Would you shop here again?"),
    ])

personality_quiz = Survey(
    "Personality Test",
    "take our personality quiz!",
    [
        Question("Do you ever think about code?"),
        Question("Do you ever have bad dreams about code?"),
        Question("Do you prefer dogs or cats?",
                 ["dogs", "cats"]),
        Question("Which is the best type of loop, and why?",
                 ["for loop", "while loop", "for of"],
                 allow_text=True),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}