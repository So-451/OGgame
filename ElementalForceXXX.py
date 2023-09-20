import random as r
from cmd import Cmd 
import sys
from os import system

# Global variables (erasing them will break the program)

p1_hp=100
p2_hp=100
p1_turns=5
p2_turns=5
p1_id = "p1"
p2_id = "p2"


action = ""

class GameRuntime():

  global action
  global p1_hp
  global p2_hp
  global p1_turns
  global p2_turns
  


  def __init__(self) -> None:
      pass

  # the place where the player's actions take place
  @classmethod
  def action_phase(self, p_id):
    if action=="fire" or action=="Fire":
      print("Destruction")
      if p_id == "p1":
         self.damage_dealer_p1()

      else:
         self.damage_dealer_p2()
      

    elif action == "water" or action == "Water":
      print("Purification")


      if p_id == "p1":
         self.hp_increase_p1()

      else:
         self.hp_increase_p2()

    elif action == "wind" or action == "Wind":
      print("Increase in Stamina")


      if p_id == "p1":
         self.turns_increase(pl_id=p_id)

      else:
         self.turns_increase(pl_id=p_id)

    elif action == "ice" or action == "Ice":
      print("Frozen")

      if p_id == "p1":
         self.damage_dealer_p1()
         self.turns_decrease(pl_id=p_id)

      else:
         self.damage_dealer_p2()
         self.turns_decrease(pl_id=p_id)

    elif action == "quantum" or action == "Quantum":
      print("Buff Activated") 
    
      if p_id == "p1":
         self.add_element(pl_id=p_id)

      else:
         self.add_element(pl_id=p_id)
      
    elif action == "imaginary" or action == "Imaginary":
      print("Debuff Applied")  

      if p_id == "p1":
         self.remove_element(pl_id=p_id)

      else:
         self.remove_element(pl_id=p_id)


      
    else:
      print("Invalid input")
      return 0

  @classmethod
  def damage_dealer_p1(self):
    global p2_hp

  
    dmg_dealt_2 = r.randint(1,30)

    if p2_hp>=0 and p2_hp<=2:
    
      p2_hp = 0
    
    else:
       
      p2_hp = p2_hp - dmg_dealt_2 #set player 2 hp

  @classmethod
  def damage_dealer_p2(self):
    global p1_hp

    dmg_dealt_1 = r.randint(1,30)
    
    if p1_hp>=0 and p1_hp<=2:
    
      p1_hp = 0
    
    else:
       
      p1_hp = p1_hp - dmg_dealt_1  #set player 1 hp
  
  @classmethod
  def turns_increase(self, pl_id):
    global p1_turns
    global p2_turns

    if pl_id == "p1":
        p1_turns+=2

    else:
       p2_turns+=2

  @classmethod
  def turns_decrease(self, pl_id):
    global p1_turns
    global p2_turns

    if pl_id == "p1":
        p1_turns-=2

    else:
       p2_turns-=2

  @classmethod
  def hp_increase_p1(self):
    global p1_hp

    if p1_hp<100 and p1_hp>=90:
      p1_hp = 100

    else:
      p1_hp+=35

  @classmethod
  def hp_increase_p2(self):
    global p2_hp

    if p2_hp<100 and p2_hp>=90:
      p2_hp = 100

    else:
      p2_hp+=35

  @classmethod
  def add_element(self,pl_id):
    global add_ele
    global p1_set
    global p2_set

    if pl_id == "p1":
       add_ele=input("Enter which element you want to add:\n")
       p1_set.append(add_ele)
       p1_set.remove("Quantum")
       print(f'Updated set{p1_set}')

    else:
       add_ele=input("Enter which element you want to add:\n")
       p2_set.append(add_ele)
       p1_set.remove("Quantum")
       print(f'Updated set{p2_set}')
      

  @classmethod
  def remove_element(self,pl_id):
    global remo_ele
    global p1_set
    global p2_set

    if pl_id == "p1":
       remo_ele=input("Enter which element you want to remove:\n")
       if remo_ele in p2_set:
         p2_set.remove(remo_ele)
         p1_set.remove("Imaginary")
         print(f'Updated set of player 2 is {p2_set}')
         print(f'Updated set of player 1 is {p1_set}')
       else:
         print(f'{remo_ele} not found in the set')


    else:
       remo_ele=input("Enter which element you want to remove:\n")
       if remo_ele in p1_set:
         p1_set.remove(remo_ele)
         p2_set.remove("Imaginary")
         print(f'Updated set of player 1 is {p1_set}')
         print(f'Updated set of player 2 is {p2_set}')
       else:
         print(f'{remo_ele} not found in the set')
      



#main program

class MainGameProcess(Cmd):

  global action
  global p1_id
  global p2_id

  system("cls")
  print("This is the main menu")
  print("To start the game, type start and hit enter.")
  print("To exit the game, type exit and hit enter.")
  print("Type ? or help for help on available commands.")

  prompt = ">"
  
  def do_welcome_message(self, inp:None):
    '''Prints a series of messages as a welcome message on initial launch.'''
    print("This is the main menu")
    print("To start the game, type start and hit enter.")
    print("To exit the game, type exit and hit enter.")
    print("Type ? or help for help on available commands.") # reusable function
  


  def do_exit(self, inp):
    '''exits the game'''
    print("Goodbye!")
    sys.exit(0)

  
  def do_refresh_screen(self, inp:None):
    
    
    self.do_welcome_message(inp=inp)

  def do_start(self, inp:None):
    '''starts the game'''
    global action
    global p1_set
    global p2_set
    print("Welcome!")

    p1=input("Our first player's name is: ")
    p2=input("And the opponent's is: ")
    print("Let the battle begin!")


    elements=["Water","Fire","Wind","Ice","Quantum","Imaginary"]


    p1_set=r.sample(elements,4)

    print(f"{p1} can use the following elements")
    for i in p1_set:
        print(i)

    p2_set=r.sample(elements,4)

    print(f"{p2} can use the following elements")
    for i in p2_set:
        print(i)


    #the place where the game continues till one of the player wins

    while p1_hp >= 0 or p2_hp >= 0  or p1_turns <= 10 or p2_turns <= 10:
      action=input(f"{p1} please select your move: ")
      GameRuntime.action_phase(p_id=p1_id)
      

      print("Current Status")
      print("Player 1 Hp:" , p1_hp)
      print("Player 2 Hp:" ,p2_hp)
      print("Player 1 Turns:" ,p1_turns)
      print("Player 2 Turns:" ,p2_turns)

      if p2_hp <= 0 or p1_turns >= 10:
        print(p1 + " wins!")
        break
      
       

      action=input(f"{p2} please select your move: ")
      GameRuntime.action_phase(p_id=p2_id)


      print("Current Status")
      print("Player 1 Hp:", p1_hp)
      print("Player 2 Hp:", p2_hp)
      print("Player 1 Turns:", p1_turns)
      print("Player 2 Turns:", p2_turns)


    if p1_hp <= 0 or p2_turns >= 10:
      print(p2 + " wins!")
      
    self.do_refresh_screen(inp=inp)

MainGameProcess().cmdloop()
