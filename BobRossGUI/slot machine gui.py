__author__ = 'stKy1219Lo7351'
from SymbolRange import *
from tkinter import *
import tkinter.messagebox

Money = [100]
Photos = [1,2,3]



def main():
    GUI().mainloop()

class GUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Bob Ross presents: Happy little accidents")
        self.grid()
        self._label = Label(self, text = "Current balance: " + str(Money[0]))
        self._label.grid(column = 0, row = 0)

        self._label1 = Label(self, text = "")
        self._label1.grid(column = 0, row = 1, sticky = W)
        self._label2 = Label(self, text = "")
        self._label2.grid(column = 1, row = 1,sticky = W)
        self._label3 = Label(self, text = "")
        self._label3.grid(column = 2, row = 1, sticky = W)


        file1 = "Paintbrush.gif"
        file2 = "Paintbrush.gif"
        file3 = "Paintbrush.gif"

        self._image1 = PhotoImage(file = file1)
        self._label4 = Label(self, image =self._image1)
        self._label4.grid(column = 0, row = 3)
        self._image2 = PhotoImage(file = file2)
        self._label5 = Label(self, image =self._image2)
        self._label5.grid(column = 1, row = 3)
        self._image3 = PhotoImage(file = file3)
        self._label6 = Label(self, image =self._image3)
        self._label6.grid(column = 2, row = 3)

        self._button1 = Button(self, text = "$1", command = self._Slots1)
        self._button1.grid(column = 0, row = 4, sticky = W)
        self._button5 = Button(self, text = "$5", command = self._Slots5)
        self._button5.grid(column = 1, row = 4,sticky = W)
        self._buttonMax = Button(self, text = "Max", command = self._SlotsM)
        self._buttonMax.grid(column = 2, row = 4,sticky = W)

    def _Slots1(self):
        TotalBalance1 = Money[0]
        result = Symbols()
        result.getSymbol()
        for index in range(3):
            if result.__str__()[index] == "7":
                Photos[index] = ("steveRossone.gif")
            elif result.__str__()[index] == "9":
                Photos[index]= ("SteveRosstwo.gif")
            elif result.__str__()[index] == "J":
                Photos[index] = ("Steverossthree.gif")
            elif result.__str__()[index] == "Q":
                Photos[index] = ("Steverossfour.gif")
            else:
                Photos[index] = ("bobross.gif")

        self._image1["file"] = Photos[0]
        self._image2["file"] = Photos[1]
        self._image3["file"] = Photos[2]

        TotalBalance = balance()
        TotalBalance.Changedbalance(TotalBalance1)
        TotalBalance.setBalance(-1*1)

        self._label1["text"] = result.__str__()[0]
        self._label2["text"] = result.__str__()[1]
        self._label3["text"] = result.__str__()[2]

        if result.__str__().count("7") == 3:
            TotalBalance.setBalance(1*10)
        elif result.__str__().count("9") == 3:
            TotalBalance.setBalance(1*20)
        elif result.__str__().count("J") == 3:
            TotalBalance.setBalance(1*30)
        elif result.__str__().count("Q") == 3:
            TotalBalance.setBalance(1*40)
        elif result.__str__().count("K") == 3:
            TotalBalance.setBalance(1*50)
        else:
            TotalBalance.setBalance(0)

        if result.__str__().count("7") == 2:
            TotalBalance.setBalance(1*.50)
        elif result.__str__().count("9") == 2:
            TotalBalance.setBalance(1*.50)
        elif result.__str__().count("J") == 2:
            TotalBalance.setBalance(1*.50)
        elif result.__str__().count("Q") == 2:
            TotalBalance.setBalance(1*.50)
        elif result.__str__().count("K") == 2:
            TotalBalance.setBalance(1*.50)

        Money[0] = (float(TotalBalance.__str__()))
        self._label["text"] = "Current balance: $" + str(round(Money[0],2)) + "0"
        if Money[0] == 0 or Money[0] < 0:
            tkinter.messagebox.showinfo(message="You lost, sorry.", parent = self)
            exit()
        else:
            repeat = tkinter.messagebox.askyesno("Do you want to bet again?")
            if repeat == True:
                self._label1["text"] = ""
                self._label2["text"] = ""
                self._label3["text"] = ""
                self._image1["file"] = "Paintbrush.gif"
                self._image2["file"] = "Paintbrush.gif"
                self._image3["file"] = "Paintbrush.gif"
                self._label["text"] = "Current balance: $" + str(Money[0]) + "0"
            else:
                exit()


    def _Slots5(self):
        TotalBalance1 = Money[0]
        result = Symbols()
        result.getSymbol()
        TotalBalance = balance()
        TotalBalance.Changedbalance(TotalBalance1)
        TotalBalance.setBalance(-1*1)

        self._label1["text"] = result.__str__()[0]
        self._label2["text"] = result.__str__()[1]
        self._label3["text"] = result.__str__()[2]

        for index in range(3):
            if result.__str__()[index] == "7":
                Photos[index] = ("steveRossone.gif")
            elif result.__str__()[index] == "9":
                Photos[index]= ("SteveRosstwo.gif")
            elif result.__str__()[index] == "J":
                Photos[index] = ("Steverossthree.gif")
            elif result.__str__()[index] == "Q":
                Photos[index] = ("Steverossfour.gif")
            else:
                Photos[index] = ("bobross.gif")

        self._image1["file"] = Photos[0]
        self._image2["file"] = Photos[1]
        self._image3["file"] = Photos[2]

        if result.__str__().count("7") == 3:
            TotalBalance.setBalance(5*10)
        elif result.__str__().count("9") == 3:
            TotalBalance.setBalance(5*20)
        elif result.__str__().count("J") == 3:
            TotalBalance.setBalance(5*30)
        elif result.__str__().count("Q") == 3:
            TotalBalance.setBalance(5*40)
        elif result.__str__().count("K") == 3:
            TotalBalance.setBalance(5*50)
        else:
            TotalBalance.setBalance(0)

        if result.__str__().count("7") == 2:
            TotalBalance.setBalance(5*.50)
        elif result.__str__().count("9") == 2:
            TotalBalance.setBalance(5*.50)
        elif result.__str__().count("J") == 2:
            TotalBalance.setBalance(5*.50)
        elif result.__str__().count("Q") == 2:
            TotalBalance.setBalance(5*.50)
        elif result.__str__().count("K") == 2:
            TotalBalance.setBalance(5*.50)

        Money[0] = (float(TotalBalance.__str__()))
        self._label["text"] = "Current balance: $" + str(round(Money[0], 2)) + "0"
        if Money[0] == 0 or Money[0] < 0:
            tkinter.messagebox.showinfo(message="You lost, sorry.", parent = self)
            exit()
        else:
            repeat = tkinter.messagebox.askyesno("Do you want to bet again?")
            if repeat == True:
                self._label1["text"] = ""
                self._label2["text"] = ""
                self._label3["text"] = ""
                self._image1["file"] = "Paintbrush.gif"
                self._image2["file"] = "Paintbrush.gif"
                self._image3["file"] = "Paintbrush.gif"
                self._label["text"] = "Current balance: $" + str(Money[0]) + "0"
            else:
                exit()

    def _SlotsM(self):
        TotalBalance1 = Money[0]
        result = Symbols()
        result.getSymbol()
        TotalBalance = balance()
        TotalBalance.Changedbalance(TotalBalance1)
        TotalBalance.setBalance(-1*TotalBalance1)

        self._label1["text"] = result.__str__()[0]
        self._label2["text"] = result.__str__()[1]
        self._label3["text"] = result.__str__()[2]

        for index in range(3):
            if result.__str__()[index] == "7":
                Photos[index] = ("steveRossone.gif")
            elif result.__str__()[index] == "9":
                Photos[index]= ("SteveRosstwo.gif")
            elif result.__str__()[index] == "J":
                Photos[index] = ("Steverossthree.gif")
            elif result.__str__()[index] == "Q":
                Photos[index] = ("Steverossfour.gif")
            else:
                Photos[index] = ("bobross.gif")

        self._image1["file"] = Photos[0]
        self._image2["file"] = Photos[1]
        self._image3["file"] = Photos[2]

        if result.__str__().count("7") == 3:
            TotalBalance.setBalance(TotalBalance1*10)
        elif result.__str__().count("9") == 3:
            TotalBalance.setBalance(TotalBalance1*20)
        elif result.__str__().count("J") == 3:
            TotalBalance.setBalance(TotalBalance1*30)
        elif result.__str__().count("Q") == 3:
            TotalBalance.setBalance(TotalBalance1*40)
        elif result.__str__().count("K") == 3:
            TotalBalance.setBalance(TotalBalance1*50)
        else:
            TotalBalance.setBalance(0)

        if result.__str__().count("7") == 2:
            TotalBalance.setBalance(TotalBalance1*.50)
        elif result.__str__().count("9") == 2:
            TotalBalance.setBalance(TotalBalance1*.50)
        elif result.__str__().count("J") == 2:
            TotalBalance.setBalance(TotalBalance1*.50)
        elif result.__str__().count("Q") == 2:
            TotalBalance.setBalance(TotalBalance1*.50)
        elif result.__str__().count("K") == 2:
            TotalBalance.setBalance(TotalBalance1*.50)
        Money[0] = (float(TotalBalance.__str__()))
        self._label["text"] = "Current balance: $" + str(round(Money[0],2)) + "0"
        if Money[0] == 0 or Money[0] < 0:
            tkinter.messagebox.showinfo(message="You lost, sorry.", parent = self)
            exit()
        else:
            repeat = tkinter.messagebox.askyesno("Do you want to bet again?")
            if repeat == True:
                self._label1["text"] = ""
                self._label2["text"] = ""
                self._label3["text"] = ""
                self._image1["file"] = "Paintbrush.gif"
                self._image2["file"] = "Paintbrush.gif"
                self._image3["file"] = "Paintbrush.gif"
                self._label["text"] = "Current balance: $" + str(Money[0]) + "0"
            else:
                exit()

main()