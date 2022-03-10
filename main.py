import re # re: used for searching if the word/pattern is present in a document
import random
from timeit import repeat # generates random no, byte, string, etc.
with open('words.txt' , 'r') as wordle:   
    data_base = wordle.read().splitlines()  # read the words.txt file
    #print(data_base)





word_expect = data_base[random.randint(0,len(data_base)-1)] # generate random word
def mygame(user_input, word_expect):
    input_user_list = list(user_input)   #make a list of letter of word that was input

    is_letter_present = {}
    for Index,letter in enumerate(input_user_list):
        is_letter_present.update({str(Index):'black'})      
       
    
    if user_input in data_base:
        count = 0
        #input word is present in our wordlist
          
        
        for Index,letter in enumerate(input_user_list):
            if letter in word_expect: # check if letter was present in the word of the day
                if user_input[Index] == word_expect[Index]: #check if the letter was present at correct index
                    is_letter_present[str(Index)] = 'green'
                    count = count + 1
                elif letter in word_expect:
                    is_letter_present[str(Index)] = 'yellow'
                        
        for Index,letter in enumerate(input_user_list):
            print(letter + ' '+is_letter_present[str(Index)])
        return count
    else:
        print('not in word list')
        return -1

for _ in range(0,6): 
    repeat = True
    count = 0
    while repeat: 
        repeat = False # so that while loop runs only once untill repeat is set to true
        user_input=''  
        while len(user_input) != 5:
            user_input = input("enter five letter word ")
        count = mygame(user_input,word_expect)
        if count == -1:
            repeat = True # take user input again
    if count == 5:
        break   


    


print('word expected was ' + word_expect)