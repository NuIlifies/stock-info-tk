from tkinter import *
from commands import commands

windowTitle = "[YOURTITLE]"
windowGeometry = "450x250"

"""
Usage: Write command name in key, invoke function in value, arguments are automatically passed within a list by passing through the self.args variable
 Please remember that the function is by default being invoked from within the class, meaning it should be invoked through self.x()
 IF USING COMMANDS.PY MODULE FOR COMMANDS: Please ensure that you remember to call the parent class "commands" 

i.e.:
 cmdList = {
    "foo":"commands.foo(self.args)"  
}
"""

cmdList = {
    'fetch':'self.out(commands.fetch(self.args), 1)'  
}

class gui:

    def __init__(self, master): vf
        master.columnconfigure(0, weight=1)

        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)

        # Intended to act as a pseudo-console for output
        self.output = Text(master)
        self.output.grid(row=0, column=0, columnspan=2,sticky="ew")
        # Get user input for commands
        self.inputBox = Entry(master)
        self.inputBox.grid(row=1, column=0, sticky="ew")
    
        self.submit = Button(master, text="→", command=self.processCommand)
        self.submit.grid(row=1, column=1, sticky="ew")

        #Bind enter key to yield same results as clicking submit button
        master.bind('<Return>', self.processCommand)

        self.out("NAME successfully loaded.", 1)


    def out(self, text, origin):
        # Origin 1 is from the application and will not be prefaced by >, origin 0 is from user and will be prefaced with > in order to clearly differentiate commands and output
        if origin == 1:
            self.output.insert(END, str(text + "\n"))
        else:
            self.output.insert(END, ">" + str(text + "\n"))

        self.output.yview(END)


    def processCommand(self, *event): #*event parameter added since master.bind also passes thru keystroke event to method
        # Gets contents of inputBox, stores to variable txt then clears box
        txt = self.inputBox.get()
        
        #separates the command and puts each word given in an individual list index
        command = txt.split()

        if not txt == "":
            self.inputBox.delete(0, 'end')
            self.out(txt, 0)

            self.args = []

            #make arguments separate list           
            if len(command) > 1:
                for i in range(len(command)):
                    #If the current wordi s the actual command word i.e. "config" then don't include it in the araguments list
                    if i == 0:    
                        pass
                    else:
                        self.args.append(command[i])
                
            #If the first item in the list (the main command) exists in the dictionary cmdList
            if command[0] not in cmdList:
                self.out("Invalid command! Type 'help' for a list of commands\n", 1)
            else:
                exec(cmdList[command[0]])
    
    def invalidCommandArgument(self, arg):
        self.out("Invalid argument(s) '{}'\n".format(str(arg)), 1)
        

        
# Main window parameters
if __name__=="__main__":
    root = Tk()
    root.geometry(windowGeometry)
    root.title(windowTitle)
    ui = gui(root)
    root.mainloop()
    



