import hashlib
from tkinter import *
import pyperclip

hashingFunctionsDict = {
    "SHA 1" : hashlib.sha1,
    "SHA 224" : hashlib.sha224,
    "SHA 256" : hashlib.sha256,
    "SHA 384" : hashlib.sha384,
    "SHA 512" : hashlib.sha512,
    "SHA3 224" : hashlib.sha3_224,
    "SHA3 256" : hashlib.sha3_256,
    "SHA3 384" : hashlib.sha3_384,
    "SHA3 512" : hashlib.sha3_512,
}


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hash Generator")
        self.resizable(0,0)
        self.geometry("800x400")

        self.text = StringVar()
        self.algoVar = StringVar()
        self.algoVar.set("SHA 1")

        self.text.set("Output")
        self.__createLayout()

    def __createLayout(self):
        self.textBox = Text(
            self    
        )
        self.textBox.place(x=0,y=0,relwidth=1, relheight=0.8)

        self.optionsFrame = Frame(self)
        self.optionsFrame.place(x=0, relwidth=1, rely=0.8)
        self.output = Label(self.optionsFrame, textvariable=self.text)
        self.output.pack()

        self.algoFrame = Frame(self.optionsFrame)
        self.algoFrame.pack()
        self.algoLabel = Label(self.algoFrame, text="Algorithm")
        self.algoLabel.pack(side="left")

        self.list = OptionMenu(self.algoFrame, self.algoVar, *hashingFunctionsDict.keys())
        self.list.pack(side='left')

        self.buttonFrame = Frame(self.optionsFrame)
        self.buttonFrame.pack()

        self.encrypt = Button(self.buttonFrame, text='Encrypt', command=self.__encrypt)
        self.encrypt.pack(side="left")
        self.copy = Button(self.buttonFrame, text='Copy Output', command=self.__copy,)
        self.copy.pack(side="left")

    def __encrypt(self):
        data = self.textBox.get("1.0", "end-1c")
        algorithm = hashingFunctionsDict[self.algoVar.get()]
        enryptString = algorithm(data.encode()).hexdigest()
        self.text.set(enryptString)

    def __copy(self):
        pyperclip.copy(self.text.get())
if __name__ == '__main__':
    window = Window()
    window.mainloop()