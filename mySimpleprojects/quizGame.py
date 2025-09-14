import random
Questions = []

with open("Questions.txt" , "r") as file :
    for line in file:
        q , a = line.strip().split('|')
        Questions.append({"q":q , "a":a})
selected = random.sample(Questions , 5)
score =0
for question in selected :
    ans = input(f"{question["q"]} (Yes/No)")
    if ans.strip().lower() == question["a"].lower() :
        print("Correct!\n")
        score+=1
    else:
        print(f"wrong! the correct answer is {question["a"]}\n")
print(f"Your final score: {score}/{len(selected)} .")