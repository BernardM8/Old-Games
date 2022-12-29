A=[1, 2, 3, 4, 5, 6, 7, 8, 9]
player = 'X'
I=0

def show_grid(): #print matrix function
 print(A[0:3])
 print(A[3:6])
 print(A[6:9])


def p_flip(): #flip Player function
 global player
 if player == 'O':
  player='X'
 else:
  player='O'


def p_turn(): #print Player function
 print('player '+ player +' your turn')


def display_winner(): #print player wins function
 print('player '+ player +' Wins!')


def check_winner(): #Check for win function
 global I
 if A[0:3] == [player,player,player]:
  show_grid()
  display_winner()
  I=1
 if A[3:6] == [player,player,player]:
  show_grid()
  display_winner()
  I = 1
 if A[6:9] == [player,player,player]:
  show_grid()
  display_winner()
  I = 1
 if A[0] == player and A[3] == player and A[6] == player:
  show_grid()
  display_winner()
  I = 1
 if A[1] == player and A[4] == player and A[7] == player:
  show_grid()
  display_winner()
  I = 1
 if A[2] == player and A[5] == player and A[8] == player:
  show_grid()
  display_winner()
  I = 1
 if A[0] == player and A[4] == player and A[8] == player:
  show_grid()
  display_winner()
  I = 1
 if A[2] == player and A[4] == player and A[6] == player:
  show_grid()
  display_winner()
  I = 1


#Main Program
while I==0:
 show_grid()
 p_turn()
 IN=input()
 if IN.isalpha():
   print('Invalid Entry')
 if IN.isdigit():
   Input = int(IN)
 if A[(Input - 1)] == 'X' or A[(Input - 1)] == 'O':
   print('Invalid Entry')
 for i in range(0,9,1):
   if i+1 == Input and A[i]!= 'X' and A[i]!= 'O':
     A[i]=player
     check_winner()
     p_flip()