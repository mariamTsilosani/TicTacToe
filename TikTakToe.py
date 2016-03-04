from Tkinter import *

class Application(Frame):

	"""Initializing the Frame"""
	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()

		self.player = 1;
		self.tie = 0;

		self.create_widgets()
		
		
		global Matrix;
		Matrix = [[0 for x in range(3)] for x in range(3)] 
		print Matrix[0][0]
	"""Creating the widgets for the board"""

	def create_widgets(self):

		self.welcomePhoto = PhotoImage(file="welcomeToTicTacToeCropped.GIF")
		self.header = Label(self,font = "Times 16 bold", fg = "dark green")
		self.header.grid(row = 3, column = 5, columnspan = 5)
		self.header.config(image = self.welcomePhoto, width = 400, height = 40)
		self.lineTwo = Label(self)

		self.lineTwo["text"] = "Please enter your names bellow"
		self.lineTwo.grid(row = 5, column = 5, columnspan = 5, pady = 15)

		self.enterLabel = Label(self)
		self.enterLabel["text"] = "Enter First Player's Name:"
		self.enterLabel.grid(row = 6, column = 5, columnspan = 5)

		self.enter = Entry(self,  width = 10)
		self.enter.grid(row = 7, column = 5, columnspan = 5, pady = 15)

		self.submit = Button(self, text = "Submit", width = 6, height = 1, command = self.names)
		self.submit.grid(row = 9, column = 7)
		

		self.turn = Label(self)
		self.turn.grid(row = 10, column = 5, columnspan = 5)

		self.playerOne = Label(self)
		self.playerOne["text"] = "Player One"
		self.playerOne.grid(row = 11, column = 5, columnspan = 5)

		self.playerTwo = Label(self)
		self.playerTwo["text"] = "Player Two"
		self.playerTwo.grid(row = 12, column = 5, columnspan = 5, pady = 15)
		


		"""self.create_more_widgets()"""
		"""self.boxDisable()"""
	def removeBoard(self):
		self.header.destroy()
		self.lineTwo.destroy()
		self.enterLabel.destroy()
		self.enter.destroy()
		self.submit.destroy()
		self.turn.destroy()
		self.playerOne.grid(row = 6, column = 10, columnspan = 15)
		self.playerTwo.grid(row = 7, column = 10, columnspan = 15)
		self.playerOne.config(pady = 10)
		self.playerTwo.config(pady = 10)

	"""Setting Player's Names"""
	def names(self):
		
		name = self.enter.get()
		self.enter.delete(0, END)

		if(self.player == 1):
			self.playerOne["text"] = name;
			self.player = 2
			self.enterLabel["text"] = "Enter Second Player's Name:"

		elif(self.player == 2):
			self.playerTwo["text"] = name;
			self.player = 3
			self.enter.config(state=DISABLED)
			self.submit.config(text="START")
			self.enterLabel["text"] = "Enjoy The GAME"
			self.player = 3

		elif(self.player == 3):
			self.removeBoard()
			self.create_more_widgets()


	def create_more_widgets(self):
		self.whosTurn = 1;
		self.simbol = "X";
		
		"""self.photoO = PhotoImage(file="x.GIF")
		self.rand = Button(self)
		self.rand.grid(row = 0, column = 5, columnspan = 5)
		self.rand.config(image = self.photoO, width = 25, height = 25)
		"""
		self.sidePadding = Label(self, text = " ")
		self.sidePadding.grid(row = 3, column = 1)
		self.sidePadding.config(padx = 55)

		self.topPadding = Label(self, text = " ")
		self.topPadding.grid(row = 2, column = 1)
		self.topPadding.config(pady = 10)

		self.box1 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(1, 0, 0))
		self.box1.grid(row = 3, column = 10, columnspan = 5)

		self.box2 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(2, 0, 1))
		self.box2.grid(row = 3, column = 15, columnspan = 5)

		self.box3 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(3, 0, 2))
		self.box3.grid(row = 3, column = 20, columnspan = 5)

		self.box4 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(4, 1, 0))
		self.box4.grid(row = 4, column = 10, columnspan = 5)

		self.box5 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(5, 1, 1))
		self.box5.grid(row = 4, column = 15, columnspan = 5)

		self.box6 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(6, 1, 2))
		self.box6.grid(row = 4, column = 20, columnspan = 5)

		self.box7 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(7, 2, 0))
		self.box7.grid(row = 5, column = 10, columnspan = 5)

		self.box8 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(8, 2, 1))
		self.box8.grid(row = 5, column = 15, columnspan = 5)

		self.box9 = Button(self, width = 6, height = 3, command=lambda: self.OnButtonClick(9, 2, 2))
		self.box9.grid(row = 5, column = 20, columnspan = 5)
		#self.box9["text"] = "X"
		

		self.boxEnable()
		self.playerOne.config(fg = "red")

		
	"""Changing The Buttons On Click"""
	def OnButtonClick(self, button_id, x, y):

		if(self.whosTurn == 1):
			self.simbol = "X";
		elif(self.whosTurn == 2):
			self.simbol = "O";

		Matrix[x][y] = self.simbol

		if(button_id == 1):
			self.box1["text"] = self.simbol;
			self.box1.config(state=DISABLED)
		elif(button_id == 2):
			self.box2["text"] = self.simbol;
			self.box2.config(state=DISABLED)
		elif(button_id == 3):
			self.box3["text"] = self.simbol;
			self.box3.config(state=DISABLED)
		elif(button_id == 4):
			self.box4["text"] = self.simbol;
			self.box4.config(state=DISABLED)
		elif(button_id == 5):
			self.box5["text"] = self.simbol;
			self.box5.config(state=DISABLED)
		elif(button_id == 6):
			self.box6["text"] = self.simbol;
			self.box6.config(state=DISABLED)
		elif(button_id == 7):
			self.box7["text"] = self.simbol;
			self.box7.config(state=DISABLED)
		elif(button_id == 8):
			self.box8["text"] = self.simbol;
			self.box8.config(state=DISABLED)
		elif(button_id == 9):
			self.box9["text"] = self.simbol;
			self.box9.config(state=DISABLED)


		self.checkWin()
		if(self.tie == 9):
			self.playerOne.config(fg = "red")
			self.playerOne["text"] = "It's a tie"
			self.playerTwo.grid_forget()
			self.replay = Button(self, text = "replay", width = 6, height = 1, command = self.gameReplay)
			self.replay.grid(row = 7, column = 10, columnspan = 15)
		elif(self.whosTurn == 1):
			self.whosTurn = 2;
			self.playerOne.config(fg = "black")
			self.playerTwo.config(fg = "red")
		elif(self.whosTurn == 2):
			self.simbol = "O";
			self.whosTurn = 1;
			self.playerOne.config(fg = "red")
			self.playerTwo.config(fg = "black")

	def boxDisable(self):
		self.box1.config(state=DISABLED)
		self.box2.config(state=DISABLED)
		self.box3.config(state=DISABLED)
		self.box4.config(state=DISABLED)
		self.box5.config(state=DISABLED)
		self.box6.config(state=DISABLED)
		self.box7.config(state=DISABLED)
		self.box8.config(state=DISABLED)
		self.box9.config(state=DISABLED)

	def boxEnable(self):
		self.box1.config(state=NORMAL)
		self.box2.config(state=NORMAL)
		self.box3.config(state=NORMAL)
		self.box4.config(state=NORMAL)
		self.box5.config(state=NORMAL)
		self.box6.config(state=NORMAL)
		self.box7.config(state=NORMAL)
		self.box8.config(state=NORMAL)
		self.box9.config(state=NORMAL)
	def declareWin(self):
		self.tie = 0
		if(self.whosTurn == 1):
			self.playerOne.config(fg = "red")
			self.playerOne["text"] = self.playerOne.cget("text") + " IS THE WINNER!!!"
			self.playerTwo.grid_forget()
			self.replay = Button(self, text = "replay", width = 6, height = 1, command = self.gameReplay)
			self.replay.grid(row = 7, column = 10, columnspan = 15)
		elif(self.whosTurn == 2):
			self.playerOne.config(fg = "red")
			self.playerOne["text"] = self.playerTwo.cget("text") + " IS THE WINNER!!!"
			self.playerTwo.grid_forget()
			self.replay = Button(self, text = "replay", width = 6, height = 1, command = self.gameReplay)
			self.replay.grid(row = 7, column = 10, columnspan = 15)
	def gameReplay(self):
		self.box1.destroy()
		self.box2.destroy()
		self.box3.destroy()
		self.box4.destroy()
		self.box5.destroy()
		self.box6.destroy()
		self.box7.destroy()
		self.box8.destroy()
		self.box9.destroy()
		self.replay.destroy()
		self.playerOne.destroy()
		self.playerTwo.destroy()
		self.sidePadding.destroy()
		self.topPadding.destroy()
		self.whosTurn = 1
		self.tie = 0
		self.player = 1
		Matrix[0][0] = 0
		Matrix[0][1] = 0
		Matrix[0][2] = 0
		Matrix[1][0] = 0
		Matrix[1][1] = 0
		Matrix[1][2] = 0
		Matrix[2][0] = 0
		Matrix[2][1] = 0
		Matrix[2][2] = 0
		self.create_widgets()

	def checkWin(self):
		self.tie = self.tie + 1
		if(Matrix[0][0] == Matrix[1][0] and Matrix[0][0] == Matrix[2][0] and Matrix[0][0] != 0):
			self.box1.config(bg = "red")
			self.box4.config(bg = "red")
			self.box7.config(bg = "red")
			self.boxDisable()
			self.declareWin()
		elif(Matrix[0][1] == Matrix[1][1] and Matrix[0][1] == Matrix[2][1] and Matrix[0][1] != 0):
			self.box2.config(bg = "red")
			self.box5.config(bg = "red")
			self.box8.config(bg = "red")
			self.boxDisable()
			self.declareWin()
		elif(Matrix[0][2] == Matrix[1][2] and Matrix[0][2] == Matrix[2][2] and Matrix[0][2] != 0):
			self.box3.config(bg = "red")
			self.box6.config(bg = "red")
			self.box9.config(bg = "red")
			self.boxDisable()
			self.declareWin()
		elif(Matrix[0][0] == Matrix[0][1] and Matrix[0][0] == Matrix[0][2] and Matrix[0][0] != 0):
			self.box1.config(bg = "red")
			self.box2.config(bg = "red")
			self.box3.config(bg = "red")
			self.boxDisable()
			self.declareWin()
		elif(Matrix[1][0] == Matrix[1][1] and Matrix[1][0] == Matrix[1][2] and Matrix[1][0] != 0):
			self.box4.config(bg = "red")
			self.box5.config(bg = "red")
			self.box6.config(bg = "red")
			self.boxDisable()
			self.declareWin()
		elif(Matrix[2][0] == Matrix[2][1] and Matrix[2][0] == Matrix[2][2] and Matrix[2][0] != 0):
			self.box7.config(bg = "red")
			self.box8.config(bg = "red")
			self.box9.config(bg = "red")
			self.boxDisable()
			self.declareWin()
		elif(Matrix[0][0] == Matrix[1][1] and Matrix[0][0] == Matrix[2][2] and Matrix[0][0] != 0):
			self.box1.config(bg = "red")
			self.box5.config(bg = "red")
			self.box9.config(bg = "red")
			self.boxDisable()
			self.declareWin()
		elif(Matrix[2][0] == Matrix[1][1] and Matrix[2][0] == Matrix[0][2] and Matrix[2][0] != 0):
			self.box7.config(bg = "red")
			self.box5.config(bg = "red")
			self.box3.config(bg = "red")
			self.boxDisable()
			self.declareWin()

root = Tk()
root.title("TikTakToe")
root.geometry("400x300")
app = Application(root)

root.mainloop()