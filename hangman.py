import random

words = ["python", "java", "kotlin", "javascript", "hangman", "challenge", "programming", "game", "developer", "function","variable"]

word = random.choice(words)
turns = 10
guesses = ""
failed = 0

while turns > 0:

  for char in word:
    if char in guesses:
      print(char, end="")
    else:
      print("_", end="")
      failed += 1
  print (" ")

  if failed == 0:
    print("You won")
    break
  else:
    failed = 0

  print("Used letters: ", guesses)
  print("▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖")
  guess = input("guess a character: ")
  if len(guess) == 1:
    geuss = guess.lower()
    if geuss not in guesses:
      guesses += guess

      if guess not in word:
        turns -= 1
        print("Wrong! Lives=", turns)

        if turns == 0:
          print("Game over! The secret word was:", word)
    else:
      print("Used letter!")
  else:
    print("Only 1 char!")