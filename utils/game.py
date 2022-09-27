
from curses.ascii import isalpha

class Hangman :
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']   
    def __init__(self, i=0):
        '''
            Function that will init all the variable
            :param number_two: a random number who gonna be use for choise a word to find
        '''
        self.word_to_find = Hangman.possible_words[i].upper()
        self.live = 5
        self.correctly_guessed_letters :List[str] = []
        for i in self.word_to_find:
            self.correctly_guessed_letters.append('_')
        self.wrongly_guessed_letters:List[str] = []
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        '''
             Function that will ask the player to put a letter after that they check if the letter was in the word or not
        '''
        self.letter = input("insert a letter: ").upper()
        if len(self.letter) == 1 and self.letter in self.word_to_find :
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == self.letter:
                    self.correctly_guessed_letters[i] = self.letter[0]
            return
        self.live -= 1
        self.error_count += 1
        if self.letter.isalpha() or len(self.letter) != 1:
            self.wrongly_guessed_letters.append(self.letter)  
        else:
            print("i said a letter !!")
                
    def game_over(self):
        '''
            the player is dead :(
        '''
        print(f"game over ... The word was {self.word_to_find}")
    
    def well_played(self):
        '''
            Function that will says you won
        '''
        print(f"you fond the word : {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors !")
    
    def print_(self):
        '''
            Function that will print the result of each turn
        '''
        print(f"REMAINING LIFE : {self.live} TURN : {self.turn_count} ERROR : {self.error_count}")
        print(" ".join(self.correctly_guessed_letters))
        print(" ".join(self.wrongly_guessed_letters)) if len(self.wrongly_guessed_letters) else print(end="")
        print("-"*100)   

    def start_game(self) :
        '''
            This function start the game after that, they check if the player is dead or won the game
        '''
        while True:
            self.play()
            print("-"*100)          
            self.turn_count += 1
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                break
            if self.live == 0:
                self.game_over()
                break
            self.print_()
