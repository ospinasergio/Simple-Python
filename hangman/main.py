import random
import stagLogo
import words

print(stagLogo.logo)

stages = stagLogo.stages
end_of_game = False
word_list = words.word_list
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
playing = True

for letter in chosen_word:
    display.append("_")

print(" ".join(display) + "\n")

lives = 6
already_atempted = []

while playing:
    guess = input("Guess a letter: " + "\n").lower()

    index = 0
    atempted = False
    found = False

    for letter in chosen_word:

        # mund ta besh for i in range(len(chosen_word))
        if guess in chosen_word:
            found = True

        if guess in already_atempted:
            print(f"You have already atempted {guess}" + "\n")
            atempted = True
            break

        if letter == guess:
            display[index] = guess


        elif found == False:
            lives -= 1
            print(stages[lives])
            print(f"that {guess} is not in the word" + "\n")
            break

        index += 1

    print(" ".join(display) + "\n")

    if atempted == False:
        already_atempted.append(guess)

    if not "_" in display:
        playing = False
        print("You win. You Smart!" + "\n")

    if lives == 0:
        print("You lost. Try again maybe later" + "\n")
        playing = False

