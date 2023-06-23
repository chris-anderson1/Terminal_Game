import multiprocessing
import random
import time
import sys
import os
from playsound import playsound
import pygame
practice = [16]
numbers = [0, 1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
numbers3 = [11, 12, 13, 14, 15]
questions = ["Which Disney character famously leaves a glass slipper behind at a royal ball?", "By definition, a 10-speed bike has 10 what? ", "When playing Blackjack, how many points would be considered a bust?", "In ancient Egyptian mythology, who was the god of the sun?", "The ancient Incan ruins of Machu Picchu are in which country?", "The hammer and sickle is one of the most recognizeable symbols of which political ideology?", "Which toys have been marketed with the phrase 'robots in disguise'?", "Which of these religious observances lasts for the shortest period of time during the calendar year?",
             "What is the celcius equivalent of 77 degrees Fahrenheit?", "Which insect shorted out an early supercomputer and inspired the term 'computer bug'? ", "Which of these animals sleeps up to 22 hours a day?", "Umberto II was the last king of which European country?", "Marie Antoinette was the wife and queen of which French king Louis?", "Which former Beatle narrated the TV adventures of Thomas the Tank Engine?",
             "During World War II, US soldiers used the first commercial aerosol cans to hold what?", "Which of these is not one of the American Triple Crown horse races?", "Where did Scotch whiskey originate?", "What sort of animal is Walt Disney's Dumbo?" ]
answers = [" A.Pocahontas" " B.Sleeping_Beauty" " C.Cinderella" " D.Elsa" " [Final_Answer]: ", " A.Wheels " " B.Spokes " " C.Gears " " D.Paint_Varieties " " [Final_Answer]: ", " A.22 " " B.21 " " C.15 " " D.19 " " [Final_Answer]: ", " A.Ra" " B.Osiris" " C.Horus" " D.Geb" " [Final_Answer]: ", " A.Peru" " B.Chile" " C.Argentina" " D.Mexico" " [Final_Answer]: ",  " A.Republicanism" " B.Communism" " C.Conservatism" " D.Liberalism" " [Final_Answer]: ", " A.Bratz_Dolls " " B.Sylvanian Families " " C.Hatchials " " D.Transformers " " [Final_Answer]: ", " A.Ramadan" " B.Diwali" " C.Lent" " D.Hanukkah" " [Final_Answer]: ",
           " A.15" " B.25" " C.20" " D.30" " [Final_Answer]: ", " A.Moth" " B.Roach" " C.Fly" " D.Japanese_Beetle" " [Final_Answer]: ", " A.Koala " " B.Lion " " C.Copperhead " " D.Beagle " " [Final_Answer]: ", " A.Italy" " B.France" " C.Spain" " D.Germany" " [Final_Answer]: ", " A.XIV" " B.XV" " C.XVI" " D.XIII" " [Final_Answer]: ", " A.John_Lennon" " B.Paul_McCartney" " C.George_Harrison" " D.Ringo_Starr" " [Final_Answer]: ", " A.Cleaning_Fluid" " B.Antiseptic" " C.Insecticide" " D.Shaving_Cream" " [Final_Answer]: ",
            " A.Arlington_Million" " B.Belmont_Stakes" " C.Kentucky_Derby" " D.Preakness_Stakes" " [Final_Answer:] ", " A.Ireland" " B.Wales" " C.The_United_States" " D.Scotland" " [Final_Answer]: ", " A.Deer " " B.Rabbit " " C.Elephant " " D.Donkey" " [Final_Answer]: "]
correct = [ "C.Cinderella", "C.Gears", "A.22", "A.Ra", "A.Peru", "B.Communism","D.Transformers" , "B.Diwali","B.25","A.Moth", "A.Koala", "A.Italy", "C.XVI", "D.Ringo_Starr", "C.Insecticide", "A.Arlington_Million", "D.Scotland", "C.Elephant"]
percentage = [" 48%", " 26%", " 18%", " 8%"]
family_friends = ["Roger (Your Best Friend)", "Debra (Your Coworker)", "Marge (Your Mother)"]
family_friends_answers = [" 'Oh I know this, its:'' ", " 'Ok so I'm fairly confident its:' ", " 'Oh boy I'm not too sure, if I had to guess it would be:' ", " 'Oh I'm sorry I have no idea. I would guess:' " ]
money_levels = ["$0","$100", "$200", "$300", "$500", "$1,000", "$2,000", "$4,000", "$8,000", "$16,000", "$32,000", "$64,000", "$125,000", "$250,000", "$500,000", "1,000,000"]
rounds = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
correct_responses = ["That is......correct", "You've got it!", "By golly you're right"]
money = 0
round = 0
money1 = 1
life_lines = ["1:Fifty_Fifty", "2:Ask_the_Audience", "3:Phone_a_Friend"]
p = multiprocessing.Process(target=playsound, args=("100_up.mp3",))
pygame.init()

def get_question():
  if len(numbers) > 0:
    num = random.choice(numbers)
    Q_A = str(questions[num]) + str(answers[num])
    numbers.remove(num)
    return Q_A
  elif len(numbers) == 0 and len(numbers2) > 0:
    num = random.choice(numbers2)
    Q_A = str(questions[num]) + str(answers[num])
    numbers2.remove(num)
    return Q_A
  else:
    num = random.choice(numbers3)
    Q_A = str(questions[num]) + str(answers[num])
    numbers3.remove(num)
    return Q_A

def fifty_fifty(question):
 corrects = str(correct)
 splits = question.split("?")
 answers = splits[1]
 splita = answers.split()
 removed = 0
 while removed < 2:
  for words in splita:
    if words in corrects:
      continue
    elif words == "[Final_Answer]:":
      continue
    else:
      splita.remove(words)
      removed += 1
  return splita
     
def ask_the_audience(question):
 corrects = str(correct)
 splits = question.split("?")
 answers = splits[1]
 splita = answers.split()
 splitaa = []
 for answers in splita:
  if answers in corrects:
    right_answer = answers + percentage[0]
    splitaa.append(right_answer)
  elif answers == "[Final_Answer]:":
    continue
  else:
    answers_2 = answers + percentage.pop(-1)
    splitaa.append(answers_2)
 return "Well here are the audience survey results " + str(splitaa)

def phone_a_friend(question):
 corrects = str(correct)
 splits = question.split("?")
 answers = splits[1]
 splita = answers.split()
 right_answer = []
 wrong_answers = []
 response = random.choice(family_friends_answers)
 for answers in splita:
    if answers in corrects:
     right_answer.append(answers)
    elif answers == "[Final_Answer]:":
      continue
    else:
     wrong_answers.append(answers)
 if response == family_friends_answers[0]:
  return response + right_answer[0]
 elif response == family_friends_answers[1]:
   return response + right_answer[0]
 else:
  return response + random.choice(wrong_answers)

def increase_rm():
  global money
  money += 1
  global round
  round += 1
  global money1
  money1 += 1

def round_of_play():
  global round
  print("__________________________________________________________________________________________________________________________________________________________")
  print("Begin Round : " + rounds[round])
  print("You've Won: " + money_levels[money])
  print("You're playing for: " + money_levels[money1])
  print("Available Lifelines: " + str(life_lines))
  if round >= 0 and round < 7:
      pygame.mixer.music.load('100_up.mp3')
      pygame.mixer.music.play(-1)
  if round > 6 and round < 11:
      pygame.mixer.music.load('2k_32.mp3')
      pygame.mixer.music.play(-1)
  if round > 10 and round < 12:
      pygame.mixer.music.load('64.mp3')
      pygame.mixer.music.play(-1)
  if round > 11 and round < 14:
      pygame.mixer.music.load('125_250.mp3')
      pygame.mixer.music.play(-1)
  if round > 13 and round < 15:
      pygame.mixer.music.load('500.mp3')
      pygame.mixer.music.play(-1)
  if round == 15:
      pygame.mixer.music.load('1m.mp3')
      pygame.mixer.music.play(-1)
      print("For One Million Dollars....")
  if round == 15:
    print("Your Final Question. For One Million Dollars. Here it is: ")
  question_1 = get_question()
  answer_1 = input(question_1)
  if (answer_1 in correct):
    pygame.mixer.music.load('Correct.mp3')
    pygame.mixer.music.play(0)
    print("_________________________________________________________________________________________________________________________________________________________")
    print(random.choice(correct_responses))
    next = input("Ready for your next question? Type 'Y' and hit enter when ready: ")
    increase_rm()
  elif (answer_1 == "1"):
    if "1:Fifty_Fifty" in life_lines:
      pygame.mixer.music.load('fifty.mp3')
      pygame.mixer.music.play(0)
      answer_11 = input(fifty_fifty(question_1))
      if (answer_11 in correct):
        pygame.mixer.music.load('Correct.mp3')
        pygame.mixer.music.play(0)
        print("_________________________________________________________________________________________________________________________________________________________")
        print(random.choice(correct_responses))
        next = input("Ready for your next question? Type 'Y' and hit enter when ready: ")
        increase_rm()
        life_lines.remove("1:Fifty_Fifty")
      else:
        print("Oh I'm sorry that's incorrect")
        pygame.mixer.music.load('Wrong.mp3')
        pygame.mixer.music.play(0)
        lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
        if lost_1 == "Y":
          new_game()
        else:
          quit()
    else:   
     print("You've used your Fifty_Fifty lifeline")
     input(question_1)
     increase_rm()
  elif (answer_1 == "2"):
    if "2:Ask_the_Audience" in life_lines:
      pygame.mixer.music.load('audience.mp3')
      pygame.mixer.music.play(0)
      answer_11 = input(ask_the_audience(question_1))
      if (answer_11 in correct):
        pygame.mixer.music.load('Correct.mp3')
        pygame.mixer.music.play(0)
        print("_________________________________________________________________________________________________________________________________________________________")
        print(random.choice(correct_responses))
        next = input("Ready for your next question? Type 'Y' and hit enter when ready: ")
        increase_rm()
        life_lines.remove("2:Ask_the_Audience")
      else:
        print("Oh I'm sorry that's incorrect")
        pygame.mixer.music.load('Wrong.mp3')
        pygame.mixer.music.play(0)
        lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
        if lost_1 == "Y":
          new_game()
        else:
          quit()
    else:
     print("You've used your Ask_the_Audience lifeline")
     input(question_1)
     increase_rm()
  elif (answer_1 == "3"):
    if "3:Phone_a_Friend" in life_lines:
      print("Ok so you'd like to Phone a Friend? Who would you like to call? Please type one of the names below and hit ENTER: ")
      answer_0 = input(family_friends)
      pygame.mixer.music.load('Phone.mp3')
      pygame.mixer.music.play(0)
      print("_________________________________________________________________________________________________________________________________________________________")
      print("Alright we've got " + answer_0 + " on the line and here's the question again: " + question_1)
      "/n"
      response = phone_a_friend(question_1)
      print(answer_0 + ":" + response)
      answer_11 = input("Your Answer:")
      if (answer_11 in correct):
          pygame.mixer.music.load('Correct.mp3')
          pygame.mixer.music.play(0)
          print("_________________________________________________________________________________________________________________________________________________________")
          print(random.choice(correct_responses))
          next = input("Ready for your next question? Type 'Y' and hit enter when ready: ")
          increase_rm()
          life_lines.remove("3:Phone_a_Friend")
      else:
          print("Oh I'm sorry that's incorrect")
          pygame.mixer.music.load('Wrong.mp3')
          pygame.mixer.music.play(0)
          lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
          if lost_1 == "Y":
            new_game()
          else:
            quit()
    else:
      print("You've used your Phone_a_Friend lifeline")
      input(question_1)
      increase_rm()
  else:
    print("Oh I'm sorry that's incorrect")
    pygame.mixer.music.load('Wrong.mp3')
    pygame.mixer.music.play(0)
    lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
    if lost_1 == "Y":
      new_game()
    else:
      quit()

def play_game():
  while round < 15:
   round_of_play()
   if round == 15:
    print("""______________________________________________________________________________________________________________________________________________________
           I don't believe it but you've done it, Congratulations. You have won Who Wants to be a Millionaire!
           Here is your $1,000,000 check. Lets give a round of applause for our new MILLIONAIRE!!
           Thanks for playing and Everybody have a great night!""")
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play(0)
    lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
    if lost_1 == "Y":
      new_game()
    else:
      quit()
    

def practice_question():
  print("__________________________________________________________________________________________________________________________________________________________")
  print("""Here is your practice question. Now in order for your answer to be correct, you need to give us BOTH the letter and answer EXACTLY as it is spelled out below. Watch any capital letters and make sure not to add any spaces, but to just type exactly 
  where you start. Some answers may require you to type special characters like underscores. For example if you wanted to guess C, you would need to type out 'C.Elephant' and then hit enter.""")
  answer_1 = input("What sort of animal is Walt Disney's Dumbo?" " A.Deer " " B.Rabbit " " C.Elephant " " D.Donkey" " [Final_Answer]: ")
  if (answer_1 in correct):
    pygame.mixer.music.load('Correct.mp3')
    pygame.mixer.music.play(0)
    print(random.choice(correct_responses))
  elif (answer_1 == "1"):
    if "Fifty_Fifty" in life_lines:
      pygame.mixer.music.load('fifty.mp3')
      pygame.mixer.music.play(0)
      answer_11 = input(fifty_fifty(question_1))
      if (answer_11 in correct):
        pygame.mixer.music.load('Correct.mp3')
        pygame.mixer.music.play(0)
        print(random.choice(correct_responses))
        next = input("Ready for your next question? Type 'Y' and hit enter when ready: ")
        if next == 'Y':
          increase_rm()
          life_lines.remove("Fifty_Fifty")
      else:
        print("Oh I'm sorry that's incorrect")
        pygame.mixer.music.load('Wrong.mp3')
        pygame.mixer.music.play(0)
        lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
        if lost_1 == "Y":
          new_game()
        else:
          quit()
    else:   
     print("You've used your Fifty_Fifty lifeline")
     input(question_1)
     increase_rm()
  elif (answer_1 == "2"):
    if "Ask_the_Audience" in life_lines:
      pygame.mixer.music.load('audience.mp3')
      pygame.mixer.music.play(0)
      answer_11 = input(ask_the_audience(question_1))
      pygame.mixer.music.load('Correct.mp3')
      pygame.mixer.music.play(0)
      print(random.choice(correct_responses))
      next = input("Ready for your next question? Type 'Y' and hit enter when ready: ")
      if next == 'Y':
        increase_rm()
        life_lines.remove("Ask_the_Audience")
      else:
        print("Oh I'm sorry that's incorrect")
        pygame.mixer.music.load('Wrong.mp3')
        pygame.mixer.music.play(0)
        lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
        if lost_1 == "Y":
          new_game()
        else:
          quit()
    else:
     print("You've used your Ask_the_Audience lifeline")
     input(question_1)
     increase_rm()
  elif (answer_1 == "3"):
    if "Phone_a_Friend" in life_lines:
      print("Ok so who would you like to call? Please Type Their Name: ")
      answer_0 = input(family_friends)
      pygame.mixer.music.load('Phone.mp3')
      pygame.mixer.music.play(0)
      print("Alright we've got " + answer_0 + " on the line and here's the question again: " + question_1)
      "/n"
      response = phone_a_friend(question_1)
      print(answer_0 + ":" + response)
      answer_11 = input("Your Answer:")
      if (answer_11 in correct):
          pygame.mixer.music.load('Correct.mp3')
          pygame.mixer.music.play(0)
          print(random.choice(correct_responses))
          next = input("Ready for your next question? Type 'Y' and hit enter when ready: ")
          if next == 'Y':
            increase_rm()
            life_lines.remove("Phone_a_Friend")
      else:
          print("Oh I'm sorry that's incorrect")
          pygame.mixer.music.load('Wrong.mp3')
          pygame.mixer.music.play(0)
          lost_1 = input("Would you like to play again? Type 'Y' or 'N' and hit enter: ")
          if lost_1 == "Y":
            new_game()
          else:
            quit()
    else:
      print("You've used your Phone_a_Friend lifeline")
      input(question_1)
      increase_rm()
  else:
    print("Whoops! Lets try again.")
    print("Whoops! Lets try again.")

def intro():
  print("""__________________________________________________________________________________________________________________________________________________________
  Good Evening Ladies and Gentlemen and welcome to Who Wants to Be A Millionaire!""")
  pygame.mixer.music.load('start.mp3')
  pygame.mixer.music.play(0)
  contestant = input(
  """  Now joining us today is, our contestant... 
  Please type your name and hit ENTER:""")
  print("__________________________________________________________________________________________________________________________________________________________")
  print("Our Contestant " + contestant + "! " + contestant + " it's great to have you with us today.") 
  input("Now before we get started tell us, what would you do with 1 Million Dollars? Type your answer and hit ENTER:")
  print("__________________________________________________________________________________________________________________________________________________________")
  print("""Well that certainly would be a great way to use your winnings! Now lets go over the rules. Now in case you're unfamiliar with how this game works, 
I'm going to ask you a multiple choice question with four possible answers, your job is to tell me the correct answer. The more questions you get the right, the more money you win. 
There are 15 total questions you have to answer correctly before you can call yourself a millionaire.""") 
  print("Would you like to try a practice round before you start?")
  first_response = input("Type 'Y' if you'd like a practice question or 'N' if you'd like to start. Hit ENTER to continue: ")
  if first_response == 'N':
    play_game()
  elif first_response == 'Y':
    practice_question()
  else:
    play_game()
  print("__________________________________________________________________________________________________________________________________________________________")
  print("""See that wasn't so bad was it? Below you'll see the rounds and the money you'd win with each one.

   15. $1 MILLION 
   14. $500,000
   13. $250,000
   12. $125,000
   11. $64,000
   10. $32,000 
   9. $16,000
   8. $8,000
   7. $4,000
   6. $2,000
   5. $1,000 
   4. $500
   3. $300
   2. $200
   1. $100 """)
  input("Type 'Y' and hit ENTER to continue: ")
  print("""__________________________________________________________________________________________________________________________________________________________

  If at any point you run into a question that's giving you troubles, we've got you covered with three lifelines:
  1. 50/50: Which will eliminate two of the possible four answers.
  2. Ask the audience: Our studio crew will survey our audience and ask them what they think the answer is.
  3. Phone a friend: We'll let you call someone to talk it out and see if they can help you find the answer. 
  Simply type one of the corresponding numbers in your answer space to use them. Keep in mind you can only use one lifeline per question, if you try and use more than one, we'll have to disqualify you.
  __________________________________________________________________________________________________________________________________________________________""")
  print("Are you ready to get started?")
  input("Type Y and hit ENTER to continue ")
  pygame.mixer.music.load('Lets_start.mp3')
  pygame.mixer.music.play(0)
  print("You're ready, alright folks here we go lets play Who wants to be a millionaire!")
  play_game
  
def new_game():
  global money
  global round
  global money1
  global numbers
  global life_lines
  global practice
  global numbers2
  global numbers3
  global questions
  global answers
  global correct
  global percentage
  global family_friends
  global family_friends_answers
  global money_levels
  global rounds
  global correct_responses
  practice = [16]
  numbers = [0, 1, 2, 3, 4, 5]
  numbers2 = [6, 7, 8, 9, 10]
  numbers3 = [11, 12, 13, 14, 15]
  questions = ["Which Disney character famously leaves a glass slipper behind at a royal ball?", "By definition, a 10-speed bike has 10 what? ", "When playing Blackjack, how many points would be considered a bust?", "In ancient Egyptian mythology, who was the god of the sun?", "The ancient Incan ruins of Machu Picchu are in which country?", "The hammer and sickle is one of the most recognizeable symbols of which political ideology?", "Which toys have been marketed with the phrase 'robots in disguise'?", "Which of these religious observances lasts for the shortest period of time during the calendar year?",
             "What is the celcius equivalent of 77 degrees Fahrenheit?", "Which insect shorted out an early supercomputer and inspired the term 'computer bug'? ", "Which of these animals sleeps up to 22 hours a day?", "Umberto II was the last king of which European country?", "Marie Antoinette was the wife and queen of which French king Louis?", "Which former Beatle narrated the TV adventures of Thomas the Tank Engine?",
             "During World War II, US soldiers used the first commercial aerosol cans to hold what?", "Which of these is not one of the American Triple Crown horse races?", "Where did Scotch whiskey originate?", "What sort of animal is Walt Disney's Dumbo?" ]
  answers = [" A.Pocahontas" " B.Sleeping_Beauty" " C.Cinderella" " D.Elsa" " [Final_Answer]: ", " A.Wheels " " B.Spokes " " C.Gears " " D.Paint_Varieties " " [Final_Answer]: ", " A.22 " " B.21 " " C.15 " " D.19 " " [Final_Answer]: ", " A.Ra" " B.Osiris" " C.Horus" " D.Geb" " [Final_Answer]: ", " A.Peru" " B.Chile" " C.Argentina" " D.Mexico" " [Final_Answer]: ",  " A.Republicanism" " B.Communism" " C.Conservatism" " D.Liberalism" " [Final_Answer]: ", " A.Bratz_Dolls " " B.Sylvanian Families " " C.Hatchials " " D.Transformers " " [Final_Answer]: ", " A.Ramadan" " B.Diwali" " C.Lent" " D.Hanukkah" " [Final_Answer]: ",
           " A.15" " B.25" " C.20" " D.30" " [Final_Answer]: ", " A.Moth" " B.Roach" " C.Fly" " D.Japanese_Beetle" " [Final_Answer]: ", " A.Koala " " B.Lion " " C.Copperhead " " D.Beagle " " [Final_Answer]: ", " A.Italy" " B.France" " C.Spain" " D.Germany" " [Final_Answer]: ", " A.XIV" " B.XV" " C.XVI" " D.XIII" " [Final_Answer]: ", " A.John_Lennon" " B.Paul_McCartney" " C.George_Harrison" " D.Ringo_Starr" " [Final_Answer]: ", " A.Cleaning_Fluid" " B.Antiseptic" " C.Insecticide" " D.Shaving_Cream" " [Final_Answer]: ",
            " A.Arlington_Million" " B.Belmont_Stakes" " C.Kentucky_Derby" " D.Preakness_Stakes" " [Final_Answer:] ", " A.Ireland" " B.Wales" " C.The_United_States" " D.Scotland" " [Final_Answer]: ", " A.Deer " " B.Rabbit " " C.Elephant " " D.Donkey" " [Final_Answer]: "]
  correct = [ "C.Cinderella", "C.Gears", "A.22", "A.Ra", "A.Peru", "B.Communism","D.Transformers" , "B.Diwali","B.25","A.Moth", "A.Koala", "A.Italy", "C.XVI", "D.Ringo_Starr", "C.Insecticide", "A.Arlington_Million", "D.Scotland", "C.Elephant"]
  percentage = [" 48%", " 26%", " 18%", " 8%"]
  family_friends = ["Roger (Your Best Friend)", "Debra (Your Coworker)", "Marge (Your Mother)"]
  family_friends_answers = [" 'Oh I know this, its:'' ", " 'Ok so I'm fairly confident its:' ", " 'Oh boy I'm not too sure, if I had to guess it would be:' ", " 'Oh I'm sorry I have no idea. I would guess:' " ]
  money_levels = ["$0","$100", "$200", "$300", "$500", "$1,000*", "$2,000", "$4,000", "$8,000", "$16,000", "$32,000", "$64,000", "$125,000", "$250,000", "$500,000", "1,000,000"]
  rounds = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
  correct_responses = ["That is......correct", "You've got it!", "By golly you're right"]
  money = 0
  round = 0
  money1 = 1
  life_lines = ["1:Fifty_Fifty", "2:Ask_the_Audience", "3:Phone_a_Friend"]
  intro()
  play_game()

new_game()

