Flashcards=[
    ['what is called the path of the satellite to revolve around earth? ', 'Orbit' ]
    ,['Its function is to control the airplane during rolling? ','Aileron' ]
    ,['what is the thing that provide power to run the equipment on the spacecraft? ', 'Solar panel' ]
]
def my_flashcards():
    index=0
    for flashcard in Flashcards:
        print(f"question {index+1}: {flashcard[0]}")
        index+=1
        print('______________________________')

def add_flashcards():
    Question=input('Enter a question: ')
    Answer=input('Enter its answer: ')
    Flashcards.append([Question, Answer])
    print('___________________________________')
def take_Qiuz():
    index = 0
    for flashcard in Flashcards:
        user_answer=input(f"question {index+1}: {flashcard[0]}")
        index+=1
        if user_answer.title()==flashcard[1]:#.title():
            print('correct')
        else:
            print(f"You mistake, it is {flashcard[1]}")

    print('________________________________________________________')
while True:
   print(''' 
    Let us enjoy flashcard:
    1. View flashcards
    2. Add Flashcard
    3. Take Quiz
    4. Quit''')
   choice=int(input('Enter your choice: '))
   if choice == 1:
       my_flashcards()
   elif choice == 2:
       add_flashcards()
   elif choice == 3:
       take_Qiuz()
   elif choice == 4:
       break
   else:
       print("Invalid choice. Please try again.")


