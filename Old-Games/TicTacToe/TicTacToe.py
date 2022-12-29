import Grid

# method to check if entry is valid
def checkEntry(IN):
    if IN.isalpha():
        print('Invalid Entry')
        return False
    elif IN.isdigit():
        Input = int(IN)
        temp = gameGrid.getA(Input - 1)
        if temp == 'X' or temp == 'O':
            print('Invalid Entry')
            return False
        else:
            return True


#_____Main Client Program_____
gameGrid=Grid.Grid()
while gameGrid.getI()==0:
    gameGrid.show_grid()   #print grid
    gameGrid.p_turn()      #print player
    value=input()          #input for keyboard

    if (checkEntry(value)):
        gameGrid.setA(int(value)-1) #set value in grid
        gameGrid.check_winner()     #check if there is a winner
        gameGrid.check_draw()       #check if gid is full/game is a draw
        gameGrid.p_flip()           #change player
exit()