
import random
import threading

import website_code 
from timeit import repeat # generates random no, byte, string, etc.
with open('words.txt' , 'r') as wordle:   
    data_base = wordle.read().splitlines()  # read the words.txt file
    #print(data_base)



output_table = []
for x in range(6): # 6 rows
    output_table.append([('grey',' ') for _ in range(5)])

word_expect = data_base[random.randint(0,len(data_base)-1)] # generate random word
def check_word(**kwargs):
    input_user_list = list(kwargs['user_input'])   #make a list of letter of word that was input

    is_letter_present = {}
    for Index,letter in enumerate(input_user_list):
        is_letter_present.update({str(Index):'black'})      
       
    
    if kwargs['user_input'] in data_base:
        count = 0
        #input word is present in our wordlist
          
        
        for Index,letter in enumerate(input_user_list):
            if letter in word_expect: # check if letter was present in the word of the day
                if kwargs['user_input'][Index] == word_expect[Index]: #check if the letter was present at correct index
                    is_letter_present[str(Index)] = 'green' , letter
                    count = count + 1
                elif letter in word_expect:
                    is_letter_present[str(Index)] = 'yellow' , letter
                else:
                    is_letter_present[str(Index)] = 'grey' , letter

                        
        # for Index,letter in enumerate(input_user_list):
        #     print(letter + ' '+is_letter_present[str(Index)])
        # return count
        for index in range(5):
            output_table[kwargs['attempt_no']][index] = is_letter_present[str(index)] 

    else:
        print('not in word list')
        return -1

def play_game():
    for attempt_no in range(0,6): 
        repeat = True
        count = 0
        while repeat: 
            repeat = False # so that while loop runs only once untill repeat is set to true
            user_input=''  
            while len(user_input) != 5:
                user_input = input("enter five letter word ")
            count = check_word(user_input = user_input,word_expect = word_expect , attempt_no = attempt_no)
            if count == -1:
                repeat = True # take user input again
        if count == 5:
            break   
    

    print('word expected was ' + word_expect)



@website_code.app.route('/play_game')
def my():
    return str(output_table)

@website_code.app.route('/')
def hello_world():
    return website_code.render_template('index.html',output_table = output_table)

website = threading.Thread(target= lambda : website_code.start_server())
game = threading.Thread(target= play_game)


if __name__ == '__main__':
    website.start()
    game.start()



