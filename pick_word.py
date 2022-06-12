from random import randint

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

    print(pick_word)

if __name__ == "__main__":
    pick()