question = [
["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
["Which planet is known as the red planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
["What is the largest mamal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen","Homer", 2],
["What is the square root of 64?", "6", "8", "10", "12", 2],
["Which country is known as the Land of Rising sun?", "China", "Japan", "South Korea", "India", 2],
["Who Painted the Monsa Lisa?", "Vincet van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 2],
["What is the fastest land Animal?", "Cheetah", "Lion", "Elephant", "Horse", 2], 
["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 2],
["What is the smallest country in the world?", "Vatican City", "Monaco", "San Marino", "Liechtenstein", 2],
]

prize = ["$100000", "$320000", "$400000", "$450000", "$500000", "$1000000", "$2000000", "$3000000", "$4000000", "$5000000", "$600000"]

i = 0
for question in question:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

     #check whether is answer is correct or not
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d:\n "))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time")
        break
    print(f"You won {prize[i]}")
    i = i + 1
