from curses.ascii import isalpha

class Hangman :

    def __init__(self, i=0):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = self.possible_words[i].upper()
        self.live = 5
        self.correctly_guessed_letters = []
        for i in self.word_to_find:
            self.correctly_guessed_letters.append('_')
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        self.letter = input("insert a letter: ").upper()
        if int(len(self.letter)) == 1 and self.letter in self.word_to_find :
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == self.letter:
                    self.correctly_guessed_letters[i] = self.letter[0]
            return
        self.live -= 1
        self.error_count += 1
        self.wrongly_guessed_letters.append(self.letter) if self.letter.isalpha() or int(len(self.letter)) != 1 else print("i said a letter !!")
                
    def game_over(self):
        return print(f"game over ... The word was {self.word_to_find}")
    
    def well_played(self):
        return print(f"you fond the word : {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors !")
    
    def print_(self):
        print(f"REMAINING LIFE : {self.live} TURN : {self.turn_count} ERROR : {self.error_count}")
        for i in self.correctly_guessed_letters:
            print(f"{i}",end=" ")
        print()
        for i in self.wrongly_guessed_letters:
            print(f"{i}",end=" ")
        print(end="") if len(self.wrongly_guessed_letters) == 0 else print()
        print("-"*100)   

    def start_game(self) :
        while True:
            self.play()
            print("-"*100)          
            self.turn_count += 1
            if '_' not in self.correctly_guessed_letters:
                return self.well_played()
            if self.live == 0:
                return self.game_over()
            self.print_()
