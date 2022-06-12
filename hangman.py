from random import randint
import os

def pick():
    """
    Picks a word from a pre-set txt.

    Parameters: No needed

    Return: 
        -pick_word -> str: Random word from data.txt file.  
    """

    f = open("data.txt","r")
    #print(f.read()) Opens the archive in the terminal of VS Code 
    words = []

    #Pick a word and then use it with all it's characters except the last one "\n" as it's a line jump. 
    for line in f:
        line = line[0:-1]
        words.append(line)

    #selects a random word from the list -1 in order to avoid an error. 
    randon_index = randint(0,len(words)-1)

    #Index 0 in data structures (for,list,tuple)
    #Index 1 in everything else

    pick_word = words[randon_index]
    vowels = ["á","é","í","ó","ú"]    
    to_replace = ["a","e","i","o","u"]
    counter = 0

    while counter <= 4:
        pick_word = pick_word.replace(vowels[counter],to_replace[counter])
    #Goes through the whole list searching for the vowels and then
    #replaces it with the same vowel fixed

        counter = counter +1
    return pick_word

def hangman(pick_word):
    """
    Creates the underscores which represents the chosen word. 

    Parameters: No needed. Comes from the pick() function. 
    """
    
    answer = False
    tries = 0
    
    #Blanks are the underscores assigned compared to the lenght of the chosen word. 
    blank = list("_"*len(pick_word))
    
    #Es igual a while answer == False o answer != True
    while answer != True:
        print(blank)
        letter = input("Enter a letter: ")
        counter = 0
        if len(letter) > 1:
            print("Ingresa 1 sola letra. ")

        os.system("clear")
        tries += 1

        #Si la letra esta en la palabra aleatoria...
        if letter in pick_word:
            while counter <= len(pick_word): 
                indexes = [index for index, pick in enumerate(pick_word) if pick == letter]
                for i in indexes:
                    blank[i] = letter
                counter += 1
        if "_" not in blank:
            answer = True
        

    print(f"Felicidades carechimba! Te tomo {tries} intentos resolver la palabra {pick_word}")


def run():
    """
    Calls both pick, which picks a word, and hangman, which transforms the word in order to start the game. 

    Parameters: Nothing

    Return nothings
    """
    final = pick()
    hangman(final)

if __name__ == "__main__":
    run() 