from Quiz_Data import quiz_dict

score = 0

def quiz(answer, question):
    global score
    if answer.lower() == question.lower():
        score += 1
        print(f"\nYou Got it Right.\nYou Scored {score} points.\n")
    else:
        print(f"\nWrong Answer.\nThe correct answer was {answer_text}.\n")

for questions in quiz_dict:
    question = questions["question"]
    question_text = input(question)
    answer_text = questions["answer"]
    quiz(answer= answer_text, question= question_text)

print(f"You scored {score} / 10.")
if score >= 5:
    print("You Passed The Test")
elif score < 5:
    print("You Failed The Test")