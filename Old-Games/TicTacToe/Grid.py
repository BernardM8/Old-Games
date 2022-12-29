class Grid:

    #____Default constructor____
    def __init__(self):
        self.A = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.player = 'X'
        self.I = 0

    #____Getters and Setters____
    def getPlayer(self):
        return self.player

    def getI(self):
        return self.I

    def getA(self,i):
        return self.A[i]

    def setPlayer(input):
        player=input

    def setI(input):
        I=input

    def setA(self, i):
        self.A[i]=self.player

    #______print out methods_________
    def show_grid(self):  # print matrix function
        print(self.A[0:3])
        print(self.A[3:6])
        print(self.A[6:9])

    def p_turn(self):  # print Player function
        print('player ' + self.player + ' your turn')

    def display_winner(self):  # print player wins function
        print('player ' + self.player + ' Wins!')


    #_____functional methods_____
    def p_flip(self):  # flip Player function
        if self.player == 'O':
            self.player = 'X'
        else:
            self.player = 'O'


    def check_winner(self):  # Check for winning conditions
        if self.A[0:3] == [self.player, self.player, self.player]:
            self.show_grid()
            self.display_winner()
            self.I = 1
        if self.A[3:6] == [self.player, self.player, self.player]:
            self.show_grid()
            self.display_winner()
            self.I = 1
        if self.A[6:9] == [self.player, self.player, self.player]:
            self.show_grid()
            self.display_winner()
            self.I = 1
        if self.A[0] == self.player and self.A[3] == self.player and self.A[6] == self.player:
            self.show_grid()
            self.display_winner()
            self.I = 1
        if self.A[1] == self.player and self.A[4] == self.player and self.A[7] == self.player:
            self.show_grid()
            self.display_winner()
            self.I = 1
        if self.A[2] == self.player and self.A[5] == self.player and self.A[8] == self.player:
            self.show_grid()
            self.display_winner()
            self.I = 1
        if self.A[0] == self.player and self.A[4] == self.player and self.A[8] == self.player:
            self.show_grid()
            self.display_winner()
            self.I = 1
        if self.A[2] == self.player and self.A[4] == self.player and self.A[6] == self.player:
            self.show_grid()
            self.display_winner()
            self.I = 1


    def check_draw(self):   #check if game is a draw
        count=0
        for i in range(9):
            temp=self.A[i]
            if temp.isdigit() is not True:
                count+=1
        if count>=9:
            self.I=1
            self.show_grid()
            print('Game is a draw')
            exit()