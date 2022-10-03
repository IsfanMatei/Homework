import random

cuv = ["string", "class", "branch", "while", "for", "laptop"]

random_word = random.choice(cuv)

print("""*********** Ghiceste cuvantul ***********
            Din lista de cuvinte:
    string,class,branch,while,for,laptop""")

user_guesses = ''
chances = 10

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"Ai ghicit: {character}")
        else:
            wrong_guesses += 1
            print("_")

    if wrong_guesses == 0:
        print("Bravo , ai ghicit!")
        print(f"Cuvantul a fost: {random_word}")
        break
    guess = input("Incearca sa ghicesti: ")
    user_guesses += guess

    if guess not in random_word:
        chances -= 1
        print(f"Gresit , mai ai {chances} sanse. ")
    if chances == 0:
        print("Ai pierdut")

