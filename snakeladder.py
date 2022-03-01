# number and consequence database for storing all numbers from 1 - 100 and things will happend
# when the player goes to that position
import random
class Snake_Ladder : 
    
    table = {
        0 : [ ],
        1 : [], 
        2 : [2, 7], # it is a ladder
        3 : [],
        4 : [],
        5 : [],
        6 : [6, 1], # it is a snake
        7 : [],
        8 : [],
        9 : [],
        10 : [10, 1], # it is a snake
    }

class Players :
    
    def __init__(self,name, position, num_of_roll = 0) :
        self.name = name
        self.position = position
        self.num_of_roll = num_of_roll
        
class Game :
    
    def __init__(self) :
        self.player1 = Players('player1', 0)
        self.player2 = Players('player2', 0)
        
        
    def helper_function(self, player) :
        prompt = input("Press Enter to Roll your dice")
        print()
        if prompt == '' :
            self.number = random.randint(0, 6)
            if player.num_of_roll == 0 and (self.number == 0 or self.number == 6) :
                print("you started the game")
                print()
                player.num_of_roll += 1
            elif player.num_of_roll != 0 :
                print("Keep Going on ")
                player.num_of_roll += 1
                print()
            else :
              print("yous hould roll 0 or 6")
              print()
        
        print("sss", self.number)
        return self.number
            
         
    def rolling_dice(self) :
        
        while self.player1.position <= 10 and self.player2.position <= 10 :
            table = Snake_Ladder.table
            
            print("Player1 to roll")
            print()
            value = self.helper_function(self.player1)
            self.player1.position += value
            if self.player1.position >= 10 :
              break
            new_value = self.player1.position
            if len(table[self.player1.position]) > 0 :
              new_value = table[self.player1.position][1] 
              self.player1.position = new_value
            print(f"player1 rolled a number {value} and moved from {self.player1.position} ")

            
            print("--------------")
            while value == 0 or value == 6 :
                print("Player1 still to roll")
                print()
                value = self.helper_function(self.player1)
                self.player1.position += value
                new_value = self.player1.position 
                if self.player1.position >= 10 :
                  break

                if len(table[self.player1.position]) > 0 :
                  new_value = table[self.player1.position][1] 
                  self.player1.position = new_value
                
                
                print(f"player1 rolled a number {value} and moved from {self.player1.position } ")
                

        # player2
            print("Player2 to roll")
            value = self.helper_function(self.player2)      
            self.player2.position += value
            new_value = self.player2.position 
            if self.player2.position >= 10 :
              break

            if len(table[self.player2.position]) > 0 :
              new_value = table[self.player2.position][1] 
              print("newvalue", newvalue)
              self.player2.position = new_value
            print(f"player2 rolled a number {value} and moved from {self.player2.position  } ")

            while value == 0 or value == 6 :
                print("Player2 still on the game !!!!")
                value = self.helper_function(self.player2)
                self.player1.position += value
                new_value = self.player2.position 
                if self.player2.position >= 10 :
                  break
                if len(table[self.player2.position]) > 0 :
                  new_value = table[self.player2.position][1] 
                  self.player2.position = new_value
                print(f"player1 rolled a number {value} and moved from {self.player2.position } to {new_value}")

                
                
            
        print("Game Ends" )

game = Game()

game.rolling_dice()
                
