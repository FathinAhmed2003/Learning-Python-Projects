secret_word = "hi"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("What is the secret word? \n")
        guess_count += 1
        if guess != secret_word:
            print("Please try again.\n")

    else:
        out_of_guesses = True

if guess == secret_word:
    print("YOU WIN!!")
else:
    print("Your out of guesses!")





