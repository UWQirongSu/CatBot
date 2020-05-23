from PIL import Image
from numpy import*
import os
import pyautogui
import time


def findReset():#finds the reset button and returns a tuple of the location
    resetLocation = pyautogui.locateCenterOnScreen(r"C:\Users\Qiron\Desktop\Python\CircleTheCatScript\Images\Reset.png")
    pyautogui.moveTo(resetLocation[0],resetLocation[1])
    return resetLocation

def screenshot():
    
	return pyautogui.screenshot(r"C:\Users\Qiron\Desktop\Python\CircleTheCatScript\Screenshots\image"+str(1)+".png")

#def play():
    #if debug : print(resetLocation)

def EvenRowAdjust(rowNum, initialRowX):#adjusts the X value to account for the slight indent in the even rows
    if (-1)**rowNum > 0:
        initialRowX = initialRowX + 30
    return initialRowX
	

def findBoard():
    firstCell = (resetLocation[0]-10,resetLocation[1]-480)
    
    for row in range(11):
        rowFirstCell = (EvenRowAdjust(row+1,firstCell[0]),firstCell[1]+row*42)
        #pyautogui.moveTo(rowFirstCell)
        for column in range(11):
            currentCell = (rowFirstCell[0]+55*column,rowFirstCell[1])
            #pyautogui.moveTo(currentCell)
			
            cellLocationDict.update({(row,column):currentCell})#adds location to Location dictionary
			
            print(scrnsht.getpixel(currentCell))#empty cell(204,255,0), filled cell(114,133,1), occupied cell(0,0,0)
            board[row][column] = cellDict.get(scrnsht.getpixel(currentCell))#updates the board with occupied cells
            print("Board State")
            print(board)
			
def getCellLocation(cellTuple):
    return cellLocationDict.get(cellTuple)

	
def clickCell(cellTuple):
    board[cellTuple[0]][cellTuple[1]] = 1
    pyautogui.moveTo(cellLocationDict.get(cellTuple))
    pyautogui.click()
    time.sleep(3)
    scrnsht = screenshot()
	
	
def updateCat(catCell):
    updateBoard(catCell,0) 
    if catCell[0]%2 == 1: #if machine odd and human even
	#if human even row/ machine odd row
	#check r-1,c ; r-1,c+1
	#check r, c-1 ; r, c+1
	#check r+1, c ; r+1, c+1
        pyautogui.moveTo(getCellLocation((catCell[0]-1,catCell[1])))#check topleft
        print("Cell 1" + str(cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]-1,catCell[1]))))))
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]-1,catCell[1])))) == 2:
            return (catCell[0]-1,catCell[1])
		
        pyautogui.moveTo(getCellLocation((catCell[0]-1,catCell[1]+1)))#check topright
        print("Cell 2" + str(cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]-1,catCell[1]+1))))))
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]-1,catCell[1]+1)))) == 2:
            return (catCell[0]-1,catCell[1]+1)

        pyautogui.moveTo(getCellLocation((catCell[0],catCell[1]-1)))#check left
        print("Cell 3" + str(cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0],catCell[1]-1))))))
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0],catCell[1]-1)))) == 2:
            return (catCell[0],catCell[1]-1)
		
        pyautogui.moveTo(getCellLocation((catCell[0],catCell[1]+1)))#check right
        print("Cell 4" + str(cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0],catCell[1]+1))))))
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0],catCell[1]+1)))) == 2:
            return (catCell[0],catCell[1]+1)
		
        pyautogui.moveTo(getCellLocation((catCell[0]+1,catCell[1])))#check bottomleft
        print("Cell 5" + str(cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]+1,catCell[1]))))))
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]+1,catCell[1])))) == 2:
            return (catCell[0]+1,catCell[1])
		
        pyautogui.moveTo(getCellLocation((catCell[0]+1,catCell[1]+1)))#check bottomright
        print("Cell 6" + str(cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]+1,catCell[1]+1))))))
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]+1,catCell[1]+1)))) == 2:
            return (catCell[0]+1,catCell[1]+1)
    else:
    #if human odd row/ machine even row
    #check r-1, c-1 ; r-1, c
	#check r, c-1 ; r, c+1
	#check r+1, c-1 ; r+1, c
        pyautogui.moveTo(getCellLocation((catCell[0]-1,catCell[1]-1)))#check topleft
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]-1,catCell[1]-1)))) == 2:
            return (catCell[0]-1,catCell[1]-1)

        pyautogui.moveTo(getCellLocation((catCell[0]-1,catCell[1])))#check topright
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]-1,catCell[1])))) == 2:
            return (catCell[0]-1,catCell[1])

        pyautogui.moveTo(getCellLocation((catCell[0],catCell[1]-1)))#check left
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0],catCell[1]-1)))) == 2:
            return (catCell[0],catCell[1]-1)

        pyautogui.moveTo(getCellLocation((catCell[0],catCell[1]+1)))#check right
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0],catCell[1]+1)))) == 2:
            return (catCell[0],catCell[1]+1)
	
        pyautogui.moveTo(getCellLocation((catCell[0]+1,catCell[1]-1)))#check bottomleft
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]+1,catCell[1]-1)))) == 2:
            return (catCell[0]+1,catCell[1]-1)
		
        pyautogui.moveTo(getCellLocation((catCell[0]+1,catCell[1])))#check bottomright
        if cellDict.get(scrnsht.getpixel(getCellLocation((catCell[0]+1,catCell[1])))) == 2:
            return (catCell[0]+1,catCell[1])

def updateBoard(cellTuple, entry):
    board[cellTuple[0]][cellTuple[1]] = entry

if __name__ == "__main__":#http://mypuzzle.org/circle-the-cat
    debug = True
    catCell = (5,5) #cat always starts in row 6 column 6
    print("Running Script")
	#create the dictionaries
    cellDict = {
                (204,255,0):0,#RGB value corresponding to an empty cell
                (114,133,1):1,#RGB value corresponding to a filled cell
                (0,0,0):2#RGB value corresponding to an occupied cell(cat is on it)
               }
    cellLocationDict = {
                }
	#Interpret the game state
    scrnsht = screenshot()
    board = zeros(121).reshape(11,11)
    if debug : print(board)
    resetLocation = findReset()
    findBoard()
    print(cellLocationDict)
	
	#Play the Game
    catCell = (5,5)#cat always starts in 6th row 6th column
    if board[1][2] == 0: #checks cell of row 2, column 3
        clickCell((1,2))
   #check which quadrant the cat is running to
    catCell = updateCat(catCell)
    print(catCell)
    updateBoard(catCell,2)
    print(board)
	
	