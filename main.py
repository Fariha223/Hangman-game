import random
from hangman_stages import stages
from word_list import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"The solution is {chosen_word}")

lives = 7

display = []
for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You have {lives} lives left")
        if lives == 0:
            print("You lose.")
            break
    print(" ".join(display))
    print("\n")

    if "_" not in display:
        end_of_game= True
        print("You win.")
