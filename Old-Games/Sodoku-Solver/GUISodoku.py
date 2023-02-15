import pygame
from SodokuSolver import SodokuSolver, Backtracking
pygame.init()


class Start:

    error = False
    duplicate = False

    def button(self,event):
      pygame.font.init()
      self.font = pygame.font.Font(None, 64)
      self.startBox = pygame.Rect(480,710,75,50)
      self.colourInactive = pygame.Color(0, 255, 0)
      self.colourActive = pygame.Color(255, 0, 0)
      self.colour = self.colourInactive
      self.text = 'Start'
      self.active = False
      self.isGreen = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.active = self.startBox.collidepoint(event.pos)
        self.colour = self.colourActive if self.active else self.colourInactive


    def drawstart(self, screen):
        txtSurface = self.font.render(self.text, True, self.colour)
        self.startBox.w = 115
        screen.blit(txtSurface, (self.startBox.x+5, self.startBox.y+5))
        pygame.draw.rect(screen, self.colour, self.startBox, 2)
        #Condition when mouse hovers and presses start
        pos = pygame.mouse.get_pos()
        if self.startBox.collidepoint(pos):
            #When start is clicked validate inputs and transfer to array
            if pygame.mouse.get_pressed()[0] == 1 and self.active == False:
                # print("Start Clicked")
                self.active = True
                self.error = False
                self.duplicate = False
                #check for 0, non digits errors
                if Grid().validateEntry():
                    newArray = Grid().gridToArray()
                    backtrack=Backtracking(newArray)
                    collisions = backtrack.duplicate_check(newArray)
                    #check for collision errors
                    if not collisions:
                        #start program here
                        start_time = pygame.time.get_ticks()
                        sodoSolObj = SodokuSolver(newArray)
                        solutionGrid = sodoSolObj.solve()
                        Grid.updateGrid(solutionGrid)
                        time_since_enter = pygame.time.get_ticks() - start_time
                        print("time in milliseconds = ",time_since_enter)
                    else:
                        #print("invalid entry from duplicate")
                        self.duplicate = True
                else:
                    #print("invalid entry")
                    self.error=True


class InputBox:

    def __init__(self, x, y):
        self.font = pygame.font.Font(None, 64)
        self.inputBox = pygame.Rect(x, y, 70, 70)
        self.colourInactive = pygame.Color('lightskyblue3')
        self.colourActive = pygame.Color(0,255,0)
        self.colour = self.colourInactive
        self.text = ''
        self.active = False
        self.isBlue = True


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
            mousex, mousey = event.pos
            #print("X=",mousex)
            #print("Y=",mousey)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text = event.unicode
                    return self.text


    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.colour)
        self.inputBox.w = 70
        screen.blit(txtSurface, (self.inputBox.x+22, self.inputBox.y+15))
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)
        if self.isBlue:
            self.color = (0, 128, 255)
        else:
            self.color = (255, 100, 0)



class Grid:

    inputArray = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],

    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],

    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]

    widgets = [
        InputBox(0, 0), InputBox(70, 0), InputBox(140, 0), InputBox(215, 0), InputBox(285, 0), InputBox(355, 0),InputBox(430, 0), InputBox(500, 0), InputBox(570, 0),
        InputBox(0, 70), InputBox(70, 70), InputBox(140, 70), InputBox(215, 70), InputBox(285, 70), InputBox(355, 70),InputBox(430, 70), InputBox(500, 70), InputBox(570, 70),
        InputBox(0, 140), InputBox(70, 140), InputBox(140, 140), InputBox(215, 140), InputBox(285, 140),InputBox(355, 140), InputBox(430, 140), InputBox(500, 140), InputBox(570, 140),
        InputBox(0, 215), InputBox(70, 215), InputBox(140, 215), InputBox(215, 215), InputBox(285, 215),InputBox(355, 215), InputBox(430, 215), InputBox(500, 215), InputBox(570, 215),
        InputBox(0, 285), InputBox(70, 285), InputBox(140, 285), InputBox(215, 285), InputBox(285, 285),InputBox(355, 285), InputBox(430, 285), InputBox(500, 285), InputBox(570, 285),
        InputBox(0, 355), InputBox(70, 355), InputBox(140, 355), InputBox(215, 355), InputBox(285, 355),InputBox(355, 355), InputBox(430, 355), InputBox(500, 355), InputBox(570, 355),
        InputBox(0, 430), InputBox(70, 430), InputBox(140, 430), InputBox(215, 430), InputBox(285, 430),InputBox(355, 430), InputBox(430, 430), InputBox(500, 430), InputBox(570, 430),
        InputBox(0, 500), InputBox(70, 500), InputBox(140, 500), InputBox(215, 500), InputBox(285, 500),InputBox(355, 500), InputBox(430, 500), InputBox(500, 500), InputBox(570, 500),
        InputBox(0, 570), InputBox(70, 570), InputBox(140, 570), InputBox(215, 570), InputBox(285, 570),InputBox(355, 570), InputBox(430, 570), InputBox(500, 570), InputBox(570, 570)
    ]

    def gridToArray(self):
        newArray = [
            [self.widgets[0].text,self.widgets[1].text,self.widgets[2].text,self.widgets[3].text,self.widgets[4].text,self.widgets[5].text,self.widgets[6].text, self.widgets[7].text, self.widgets[8].text],
            [self.widgets[9].text,self.widgets[10].text,self.widgets[11].text,self.widgets[12].text,self.widgets[13].text,self.widgets[14].text,self.widgets[15].text, self.widgets[16].text, self.widgets[17].text],
            [self.widgets[18].text,self.widgets[19].text,self.widgets[20].text,self.widgets[21].text,self.widgets[22].text,self.widgets[23].text,self.widgets[24].text, self.widgets[25].text, self.widgets[26].text],

            [self.widgets[27].text,self.widgets[28].text,self.widgets[29].text,self.widgets[30].text,self.widgets[31].text,self.widgets[32].text,self.widgets[33].text, self.widgets[34].text, self.widgets[35].text],
            [self.widgets[36].text,self.widgets[37].text,self.widgets[38].text,self.widgets[39].text,self.widgets[40].text,self.widgets[41].text,self.widgets[42].text, self.widgets[43].text, self.widgets[44].text],
            [self.widgets[45].text,self.widgets[46].text,self.widgets[47].text,self.widgets[48].text,self.widgets[49].text,self.widgets[50].text,self.widgets[51].text, self.widgets[52].text, self.widgets[53].text],

            [self.widgets[54].text,self.widgets[55].text,self.widgets[56].text,self.widgets[57].text,self.widgets[58].text,self.widgets[59].text,self.widgets[60].text, self.widgets[61].text, self.widgets[62].text],
            [self.widgets[63].text,self.widgets[64].text,self.widgets[65].text,self.widgets[66].text,self.widgets[67].text,self.widgets[68].text,self.widgets[69].text, self.widgets[70].text, self.widgets[71].text],
            [self.widgets[72].text,self.widgets[73].text,self.widgets[74].text,self.widgets[75].text,self.widgets[76].text,self.widgets[77].text,self.widgets[78].text, self.widgets[79].text, self.widgets[80].text]]
        self.inputArray = newArray
        return newArray


    def updateGrid(input):
        count = 0
        for i in input:
            for j in i:
                Grid.widgets[count].text=j
                count += 1


    def getWidget(self):
        return self.widgets


    def validateEntry(self):
        for select in self.widgets:
            if select.text == '0' or (not select.text.isdigit() and not select.text == ''):
                return False
                break
        return True


# ____________________main_______________________________

#Screen/display settings
screen = pygame.display.set_mode((640,800))
pygame.display.set_caption('Sodoku Solver')
smallFont = pygame.font.SysFont("None",20)
mediumFont = pygame.font.SysFont("None",30)
startText = smallFont.render('Enter numbers and press start ', True, (230, 255, 0))
errorText = mediumFont.render('Error invalid entry. Only enter numbers ', True, (255, 0, 0))
errorText2 = mediumFont.render('from 1 to 9, or keep cell empty', True, (255, 0, 0))
duplicateText = mediumFont.render('Error you have conflicting duplicate entries', True, (255, 0, 0))

def divider_grid():
    pygame.draw.line(screen, (255, 255, 255), (213, 0), (213, 640), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 213), (640, 213), 5)
    pygame.draw.line(screen, (255, 255, 255), (427, 0), (427, 640), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 427), (640, 427), 5)


def main():
    objGrid=Grid()
    StartBOX = [Start()]
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.QUIT
            for child in objGrid.getWidget():
                store = child.handle_event(event)
            for child in StartBOX:
                child.button(event)

        # display grid
        screen.fill((30, 30, 30))
        for child in objGrid.getWidget():
            child.draw(screen)

        # display start button text
        for child in StartBOX:
            child.drawstart(screen)
        screen.blit(startText, (440, 670))

        # if errors are true then display error text
        if StartBOX[0].error:
            screen.blit(errorText, (20, 710))
            screen.blit(errorText2, (20, 740))
        if StartBOX[0].duplicate:
            screen.blit(duplicateText, (20, 710))

        divider_grid()
        pygame.display.flip()
        pygame.display.update()


main()
