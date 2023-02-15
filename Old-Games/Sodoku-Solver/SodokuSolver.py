import copy

class SodokuSolver:

    inputGrid=[
    ["0","0","0",  "0","0","0",  "0","0","0"],
    ["0","0","0",  "0","0","0",  "0","0","0"],
    ["0","0","0",  "0","0","0",  "0","0","0"],

    ["0","0","0",  "0","0","0",  "0","0","0"],
    ["0","0","0",  "0","0","0",  "0","0","0"],
    ["0","0","0",  "0","0","0",  "0","0","0"],

    ["0","0","0",  "0","0","0",  "0","0","0"],
    ["0","0","0",  "0","0","0",  "0","0","0"],
    ["0","0","0",  "0","0","0",  "0","0","0"]]

    possibilities=[
    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],
    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],
    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],

    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],
    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],
    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],

    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],
    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"],
    ["123456789","123456789","123456789",   "123456789","123456789","123456789",   "123456789","123456789","123456789"]]

    def __init__(self, input):
        self.inputGrid = input
        print("Initial input array")
        print(*input, sep="\n")
        print("\n")
        for i in range(0, 9):
            for j in range(0, 9):
                if input[i][j] != '':
                    self.possibilities[i][j] = input[i][j]
        # print("possibilities initial with no reductions")
        # print(*self.possibilities, sep="\n")
        # print("\n")

    # method to solve sodoku, reduce possibilites and bruteforce while checking reductions and leftover unique singles
    def solve(self):
        reduction = Reduction()
        backtracking = Backtracking(self.possibilities)
        self.possibilities = reduction.reduction_loop(self.possibilities)
        # print("first reduction")
        # print(*self.possibilities, sep="\n")
        # print("\n")
        solutionGrid = backtracking.backtrack_process()
        print("Sodoku Solver Solution")
        print(*solutionGrid, sep="\n")
        return solutionGrid



class Reduction:

    reductionGrid=[]
    duplicateCheckGrid = []

    # _______________Reduction Process_________________________
    def reduce_row(self,select,row):
        for k in range(0,9):
            possiblitiesAtPosition = list(self.reductionGrid[row][k])
            if select in possiblitiesAtPosition:
                if len(possiblitiesAtPosition) > 1:
                    possiblitiesAtPosition.remove(select)
                    self.reductionGrid[row][k] = ''.join(possiblitiesAtPosition)

    def reduce_col(self,select,col):
        for k in range(0,9):
            possiblitiesAtPosition = list(self.reductionGrid[k][col])
            if select in possiblitiesAtPosition:
                if len(possiblitiesAtPosition) > 1:
                    possiblitiesAtPosition.remove(select)
                    self.reductionGrid[k][col] = ''.join(possiblitiesAtPosition)

    # scans for single entries in linear directions and calls reduction of row/col
    def scan_for_linear_reductions(self):
        for i in range (0,9):
            for j in range(0, 9):
                if len(self.reductionGrid[i][j]) == 1:
                    selectedNumber=self.reductionGrid[i][j]
                    rowToReduce=i
                    colToReduce=j
                    self.reduce_row(selectedNumber, rowToReduce)
                    self.reduce_col(selectedNumber, colToReduce)


    # removes selected number in the subbox of possibilities
    def reduce_subboxes(self,select,box):
        k=box[0]
        l=box[1]
        for i in range(0, 3):
             for j in range(0, 3):
                 possibleList = list(self.reductionGrid[i+2*k+k][j+2*l+l])
                 if select in possibleList:
                        if len(possibleList) > 1:
                            possibleList.remove(select)
                            self.reductionGrid[i+2*k+k][j+2*l+l] = ''.join(possibleList)

    # scans subboxes for single entries and calls reduce_subboxes
    def scan_subboxes_for_reduction(self):
        for k in range(0,3):
            for l in range(0,3):
                for i in range(0,3):
                    for j in range(0,3):
                        if len(self.reductionGrid[i+2*k+k][j+2*l+l]) == 1:
                         selected = self.reductionGrid[i+2*k+k][j+2*l+l]
                         boxSection = [k,l]
                         self.reduce_subboxes(selected, boxSection)



    # _______________Find unique numbers leftover in grid ___________________
    def check_row(self,number,row,col):
        for k in [x for x in range(9) if x != col]:
            possibleListRow = list(self.reductionGrid[row][k])
            if number in possibleListRow:
                    return False
        else: True


    def check_col(self,number,row,col):
        for k in [x for x in range(9) if x != row]:
            possibleListCol = list(self.reductionGrid[k][col])
            if number in possibleListCol:
                    return False
        else: True


    def check_single_linear(self):
        for i in range (0,9):
            for j in range(0, 9):
                if len(self.reductionGrid[i][j]) > 1:
                    selectedList=list(self.reductionGrid[i][j])
                    for k in range (0,len(selectedList)):
                        checkNumber= selectedList[k]
                        rowResult= self.check_row(checkNumber, i, j)
                        if rowResult==True:
                            self.reductionGrid[i][j]=checkNumber
                        colResult= self.check_col(checkNumber, i, j)
                        if colResult==True:
                            self.reductionGrid[i][j]=checkNumber
    

    # __________________Check_for single numbers in subboxes  _________________________
    def find_single_in_subbox(self,select,box):
        k=box[0]
        l=box[1]
        for i in range(0, 3):
            for j in range(0, 3):
                if box != [k,l,i,j]:
                     possibleList = list(self.reductionGrid[i+2*k+k][j+2*l+l])
                     for n in range (0,len(possibleList)):
                        if select == possibleList[n]:
                            return False
        return True

    # find single leftover number in subbox of possibilities grid and replace grid entry if found
    def check_single_subbox(self):
        for k in range(0,3):    #box column
            for l in range(0,3):    #box row
                for i in range(0,3):    #column position in box
                    for j in range(0,3):    #row position in box
                        if len(self.reductionGrid[i+2*k+k][j+2*l+l])> 1:
                         selected = self.reductionGrid[i+2*k+k][j+2*l+l]
                         for m in range(0, len(selected)):
                             boxPosition = [k,l,i,j]
                             foundSingle= self.find_single_in_subbox(selected[m], boxPosition)
                             if foundSingle == True:
                                 self.reductionGrid[i+2*k+k][j+2*l+l]=selected[m]


    # runs a reduction loop until no more changes are made
    def reduction_loop(self,possibilitiesGrid):
        self.reductionGrid = possibilitiesGrid
        running = True
        while running:
            self.duplicateCheckGrid = copy.deepcopy(possibilitiesGrid)
            self.scan_for_linear_reductions()
            self.scan_subboxes_for_reduction()
            self.check_single_linear()
            self.check_single_subbox()
            # Check to see if there are any changes after reductions
            if self.duplicateCheckGrid == self.reductionGrid:
                running = False
                return self.reductionGrid



# ____________________Backtracking process _______________________
class Backtracking:

    solution = False
    duplicates = False
    backtrackGrid = []
    backtrackGridCopy = []
    lastpossibilities = []
    storedPossibEntry = []
    xStoredLoc = []
    yStoredLoc = []
    storedNum = []

    def __init__(self, grid):
        self.backtrackGrid = grid
        self.backtrackGridCopy = copy.deepcopy(grid)

    def row_check(self,grid,number,row,col):
        for k in [x for x in range(9) if x != col]:
            if len(grid[row][k])==1:
                possibleListRow = list(grid[row][k])
                if number in possibleListRow:
                    return False
        return True

    def col_check(self,grid,number,row,col):
        for k in [x for x in range(9) if x != row]:
            if len(grid[k][col]) == 1:
                possibleListCol = list(grid[k][col])
                if number in possibleListCol:
                    return False
        return True

    def check_single_in_subboxes(self,grid,select,box):
        k=box[0]
        l=box[1]
        for i in range(0, 3):
            for j in range(0, 3):
                if box != [k,l,i,j]:
                    if len(grid[i+2*k+k][j+2*l+l]) == 1:
                        possibleList = (grid[i+2*k+k][j+2*l+l])
                        if select[0] == possibleList:
                            return False
        return True


    # checks for duplicates in grid
    def duplicate_check(self, grid):
        for k in range(0, 3):  # box column
            for l in range(0, 3):  # box row
                for i in range(0, 3):  # column position in box
                    for j in range(0, 3):  # row position in box
                        check_number = str(grid[i + 2 * k + k][j + 2 * l + l])
                        if len(check_number) == 1:
                            boxPosition = [k, l, i, j]
                            if not self.row_check(grid, check_number, (i + 2 * k + k),(j + 2 * l + l)):
                                return True
                            if not self.col_check(grid, check_number, (i + 2 * k + k),(j + 2 * l + l)):
                                return True
                            if not self.check_single_in_subboxes(grid, check_number, boxPosition):
                                return True
        return False


    # backtacking last storedPossibilites and storedNumber(from bruteforce and backtrackprocess)
    def backtrack_last_stored_possibilities(self):
        for i in range(len(self.storedPossibEntry)-1,-1,-1):
            lastList = self.storedPossibEntry[i]
            for j in range(len(lastList)):
                # if lastList is the last element, remove last entries of storedPossibilites, storedNumber and coordinates
                if lastList[j] == lastList[-1]:
                    self.storedPossibEntry.pop()
                    self.storedNum.pop()
                    self.xStoredLoc.pop()
                    self.yStoredLoc.pop()
                else:
                    temp = self.storedPossibEntry[-1][1:]
                    self.storedPossibEntry[i] = temp
                    self.storedPossibEntry[i] = temp
                    self.storedNum[-1] = self.storedPossibEntry[-1][:1]
                    return self.storedNum


    def insert_new_list_to_grid(self,newlist):
        for i in range (0,len(newlist)):
            self.backtrackGrid[self.xStoredLoc[i]][self.yStoredLoc[i]]=newlist[i]
        # print("insert_new_list_to_grid()  new list = ", newlist)
        # print(*self.backtrackGrid, sep="\n")
        # print("\n")


    # bruteforce method with possiblilties
    def brute_force(self):
        reductionObj = Reduction()
        self.duplicates = False
        self.solution = False

        for k in range(0,3):
            for l in range(0,3):
                for i in range(0,3):
                    for j in range(0,3):
                        if len(self.backtrackGrid[i+2*k+k][j+2*l+l])> 1:
                            selectedPoss= self.backtrackGrid[i+2*k+k][j+2*l+l]
                            self.storedPossibEntry.append(selectedPoss)

                            for m in range (0,len(selectedPoss)):
                                selectedNumber=selectedPoss[m]
                                self.backtrackGrid[i + 2 * k + k][j + 2 * l + l] = selectedNumber        #<--insert selected number into grid
                                self.latestPossiblitiesRestore = copy.deepcopy(self.backtrackGrid)
                                self.backtrackGrid = reductionObj.reduction_loop(self.backtrackGrid)
                                self.duplicates = self.duplicate_check(self.backtrackGrid)
                                """print("brute_Force() SelectedNumber ", selectedNumber, "in", selectedPoss, "at",str([i + 2 * k + k]), str([j + 2 * l + l]))
                                print("After reduction loop")
                                print(*self.backtrackGrid, sep="\n")
                                print("\n")
                                """
                                # _____________Duplicate Failure condition______
                                # if duplicates exist restore grid back to previous iteration
                                if self.duplicates:
                                    self.backtrackGrid = copy.deepcopy(self.latestPossiblitiesRestore)
                                    if not len(self.storedPossibEntry[-1])>1:
                                        self.storedPossibEntry.pop()
                                    else:
                                        temp=self.storedPossibEntry[-1][1:]
                                        self.storedPossibEntry[-1]=temp
                                    """print("Duplicate Failure in brute_force()!")
                                    print("restoring grid")
                                    print(*self.backtrackGrid, sep="\n")
                                    print("\n")"""
                                    # ________________Duplicate Pass condition_______
                                else:
                                    self.storedNum.extend(selectedNumber)
                                    self.xStoredLoc.extend([i + 2 * k + k])
                                    self.yStoredLoc.extend([j + 2 * l + l])
                                    break
                            """print("bruteforce() outer Number selection iteration")
                            print("duplicate = ",self.duplicates)
                            print("SelectedNumber = "+selectedNumber)
                            print("storedNumber = " + str(self.storedNum))
                            print("storedPossibilities = ", self.storedPossibEntry)
                            print("Stored X Row locations", self.xStoredLoc)
                            print("Stored Y Col locations", self.yStoredLoc)
                            print(*self.backtrackGrid, sep="\n")
                            print("\n")"""
                            # if duplicates exist, restore possibiites grid and return to backtrack_process while loop
                            if self.duplicates:
                                self.backtrackGrid = copy.deepcopy(self.backtrackGridCopy)
                                return self.backtrackGrid
        # case when all possiblities are single entries and no duplicates
        self.solution = True
        return self.backtrackGrid


    def backtrack_process(self):
        reductionObj = Reduction()
        while not self.solution:
            if self.duplicates:
                self.backtrackGrid = copy.deepcopy(self.backtrackGridCopy)
                newList = self.backtrack_last_stored_possibilities()
                self.insert_new_list_to_grid(newList)
                self.backtrackGrid = reductionObj.reduction_loop(self.backtrackGrid)
                self.duplicates = self.duplicate_check(self.backtrackGrid)
                # print("grid after reduction loop")
                # print(*self.backtrackGrid, sep="\n")
                # print("\n")
                # print("duplicates = ", self.duplicates)
            else:
                solutionGrid = self.brute_force()
        return solutionGrid



