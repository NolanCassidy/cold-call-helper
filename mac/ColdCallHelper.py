"""
ColdCallHelper.py is the main application which creates the GUI interface and keybindings
it also connects to the queue module and retrieve the data to display
run this if you wish to run the cold caller applicaion using python

Run using the command - python ColdCallHelper.py

created by Nolan Cassidy
Last Update:4/29/2019

Layout -
    Small GUI - opens at the top of screen in a wide but short window good for using with other apps like powerpoint open
        Label - Shows the first three students in the queue, more specifically nickname lastname for each or firstname latname if no nickname is present
        Menubar -
            File -
                Toggle Screen Size (s) - changes to the Big gui
                Help (h) - opens the help menu
                Quit (q) - exits out of the application with everythin saved
            Edit -
                Initialize New Roster  ⚠ - used for a new term or first time using program (WARNING erases all past data about times call/followups/markups/etc)
                Update Current Roster (u) - used when changes were made to roster.tsv like name changes or added/deleted students
            Export -
                1 - Select (1) - used when calling on first student
                2 - Select (2) - used when calling on second student
                3 - Select (3) - used when calling on third student
                1 - Followup (Ctr+1) - used to remeber to follow up with student
                2 - Followup (Ctr+2) - used to remeber to follow up with student
                3 - Followup (Ctr+3) - used to remeber to follow up with student
                1 - Problem (Shift+1) - used to remeber student was absent or caused a concern
                2 - Problem (Shift+2) - used to remeber student was absent or caused a concern
                3 - Problem (Shift+3) - used to remeber student was absent or caused a concern
    Big GUI - opens fullscreen and increases the text sizes
        Label - Shows the firstname lastname nickname and pronunciation
        Menubar - Same menubar as the small gui except for the options added below
            File -
                Toggle Pronunciation (p) - show/hide the pronounciation of the student names on the big gui
                Toggle Nickname (n) - show/hide the nickname of the students on the big gui

    *if the FERPA flag is true for a student in roster.tsv, the nickname will apear and nothing else so make sure once is present if the flag is checked or else blank names will apear

Class/Def Descriptions -

    Application class- sets small sreen size mode to on, turns on pronounciation/nickname when bigscreen is on, intializes class_Queue and helpPopup
        will attemp to load in the data from roster.tsv on intitialization but if missing the help menu will apear
        def __init__(master) - this is where all of the labels, menubar, key bindings, and almost all intialization of the Frame
            so if you wish to change the layout of the frame this is the place to look
        def first() - bind 1 or spacebar - used for calling on the first student
            call on queue to update the first positon then update the labels
        def second() - bind 2 - used for calling on the second student
            call on queue to update the second positon then update the labels
        def third() - bind 3 - used for calling on the third student
            call on queue to update the third positon then update the labels
        def firstProblem() - bind ctrl+1 or ctrl+spacebar - used to mark the student when there is a problem or absence
            calls on the queue to update the postion and mark in the datarepo
        def secondProblem() - bind ctrl+2 - used to make a problem mark the student when there is a problem or absence
            calls on the queue to update the postion and mark in the datarepo
        def thirdProblem() - bind ctrl+3 - used to make a problem mark the student when there is a problem or absence
            calls on the queue to update the postion and mark in the datarepo
        def firstFollowup() - bind Shift+1 or Shift+spacebar - used to make a problem mark student when you wish to remember a good question or to follow up
            calls on the queue updates the student labels and makes a followup mark in the datarepo
        def secondFollowup() - bind Shift+2 - used to make a problem mark student when you wish to remember a good question or to follow up
                calls on the queue updates the student labels and makes a followup mark in the datarepo
        def thirdFollowup() - bind Shift+3 - used to make a problem mark student when you wish to remember a good question or to follow up
                calls on the queue updates the student labels and makes a followup mark in the datarepo
        def updateLabels() - call this anytime the queue/data is changed becuase it updates the GUI labels to be up to date
            checks which screen mode then gets the top three student information need and updates the label
        def menuSmall() - sets the menu bar to the small gui options
        def smallScreen(master) - adjusts the frame size to the small gui dimmensions
            if you wish to change the default small gui size you will do that here
        def menuBig() - sets the menu bar to the big gui options
        def bigScreen(master) -  adjusts the frame size to the big gui dimmensions, make sure to call menuBig to update the menu as well
            if you wish to change the default big gui size you will do that here
        def parseBigData(data) - in big mode this parses the string to display the formatted text
            takes in a list of strings ['firstname lastname','pronounciation','nickname']
            returns the correct string to display on big gui based off name/pronounciation toggles
        def toggleScreen() - bind s - switches between the small/big gui
        def togglePronunciation() - bind p - only for big mode - show/hide pronounciation
        def toggleNickname() - bind n - only for big mode - show/hide Nickname
        def newRoster() - used for when there is a new term or starting up a class for the first time
            warning do not call this unless you are sure you want to erase all past student and class data
        def updateRoster() - bind u - used for when uou have made changes to roster.tsv
            make changes to the roster.tsv in a program like excel and the press update to see the name chages/added/deleted students
        def getDaily() - opens a new frame containing a text box to enter the date and a button to send it
        gef grabdate() - on button press above the daily_summary txt will be made
            when the button on the getDaily frame is pressed the text in the text box will be sent to the queue then to the repo where a summary txt for that day will be made in the foolder of the app
        gef getTotal() - this will generate a Total summary txt file
        def confirmation() - opens a window after running export to display 'success'/'failure'
        def helpMenu() - bind h - opens the help window which contains more informaion on using the program
        def quit() - bind q - completely exits out of the program but the data of the student and ordering of the queue will remain the same

    HelpPop class-
        def openHelp() - loads in a new tk window, sets the title of the frame to "Help", sizes/place location, and sets the help updateLabels

"""
import os
import sys
from tkinter import Tk, Frame, YES, Menu, Label,Button, LEFT, TOP, Toplevel, Entry
#from PIL import ImageTk, Image
#import random
#import repository
import class_Queue


class HelpPop:
    def openHelp(self):
        #Create new frame for help menu
        rootHelp = Tk()
        rootHelp.title("Help")
        #Set size of help frame and center it
        width = 650
        height = 550
        screenWidth = rootHelp.winfo_screenwidth()
        screenHeight = rootHelp.winfo_screenheight()
        x = (screenWidth / 2) - (width / 2)
        y = (screenHeight / 2) - (height / 2) + 50
        rootHelp.geometry("%dx%d+%d+%d" % (width, height, x, y))
        #Help Menu text
        l = Label(rootHelp, text="How to add, delete, and change students - \n\tEdit the roster.tsv file to initalize and update the any student \n\tinformation. Then follow steps below.\n\nInitialize New Roster ⚠ - \n\tWARNING this will delete/overwrite any existing data the application \n\thas kept track of. Use this when starting a new term once roster it is\n\tchanged in excel. \n\nUpdate Roster Data - \n\tUse this if you wish to preserve the student summarary data and \n\tadd/delete/change student data altered in the roster.tsv \n\nHow to use in Class - \n\tOnce the students names have been loaded you now can call on one of the\n\ttop 3 students. The specific keypresses can be found under the 'Selection'.\n\tThere are 3 Selection options for each student - \n\t\tNormal - Usually will be pressed when student is called on.\n\t\tProblem - Pressed when a studnet is absent or warrants a concern.\n\t\tFollowup -  Pressed when you wish to follow up with a student for\n\t\texample after a good question.\n\nExport Summary - \n\tThe program is constantly saving the count for calls,followups, and\n\tproblems. There is a daily/total option allowing you to see these counts\n\talong with the students other information such as email.\n",justify=LEFT)
        l.pack(expand=YES)

class Application:
    #initialize both small mode and pronounciation to be on
    smallMode = 1
    togglePron = 1
    toggleNick = 1
    #initializes the random queue of students
    students = class_Queue.class_Queue()
    #creates instance of the help menu
    helpPopup = HelpPop()
    #tries to import roster.tsv but if not there it opens the help menu for further instructions
    """
    try:
        students.update_roster_and_queue()
    except:
        helpPopup.openHelp()
        err="No files set up, open menu to help user."
    """
    if students.data_repo.begin() == "Ready":
        if not students.load_queue():
            #students.update_roster_and_queue()
            studets.fill_both_bags_from_roster()
            students.save_queue()
        #else:
        err = "No files set up, open menu to help user."

    #initializes the frame labels,buttons,menus,and bindings
    def __init__(self,master):
        #creates the main tk app
        self.master = master
        self.master.title("Cold Call Helper")
        #sets the gui to the small gui initally
        self.smallScreen(self.master)
        #sets the gui to the large gui initally
        #self.bigScreen(self.master)
        root = Frame(self.master)
        root.pack(expand=YES)
        self.day = ""

        #these are the menu bar options when the big gui is active
        self.bigBar = Menu(root)
        self.filemenu = Menu(self.bigBar, tearoff=0)
        self.filemenu.add_command(label="Toggle Screen Size (s)", command=self.toggleScreen)
        self.filemenu.add_command(label="Toggle Pronunciation (p)", command=self.togglePronunciation)
        self.filemenu.add_command(label="Toggle Nickname (n)", command=self.toggleNickname)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Help (h)", command=self.helpMenu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit (q)", command=self.quit)
        self.bigBar.add_cascade(label="Main", menu=self.filemenu)
        self.editmenu = Menu(self.bigBar, tearoff=0)
        self.editmenu.add_command(label="Update Current Roster (u)", command=self.updateRoster)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Initialize New Roster ⚠", command=self.newRoster)
        self.bigBar.add_cascade(label="Edit", menu=self.editmenu)
        self.exportmenu = Menu(self.bigBar, tearoff=0)
        self.exportmenu.add_command(label="Daily Summary", command=self.getDaily)
        self.exportmenu.add_command(label="Total Summary", command=self.getTotal)
        self.bigBar.add_cascade(label="Export", menu=self.exportmenu)
        self.selectionmenu = Menu(self.bigBar, tearoff=0)
        self.selectionmenu.add_command(label="1 - Select (1)", command=self.first)
        self.selectionmenu.add_command(label="2 - Select (2)", command=self.second)
        self.selectionmenu.add_command(label="3 - Select (3)", command=self.third)
        self.selectionmenu.add_separator()
        self.selectionmenu.add_command(label="1 - Followup (Ctr+1)", command=self.firstFollowup)
        self.selectionmenu.add_command(label="2 - Followup (Ctr+2)", command=self.secondFollowup)
        self.selectionmenu.add_command(label="3 - Followup (Ctr+3)", command=self.thirdFollowup)
        self.selectionmenu.add_separator()
        self.selectionmenu.add_command(label="1 - Problem (z)", command=self.firstProblem)
        self.selectionmenu.add_command(label="2 - Problem (x)", command=self.secondProblem)
        self.selectionmenu.add_command(label="3 - Problem (c)", command=self.thirdProblem)
        self.bigBar.add_cascade(label="Select", menu=self.selectionmenu)
        #these are the menu bar options when the small gui is active
        self.menuBar = Menu(root)
        self.master.config(menu=self.menuBar)
        self.filemenu = Menu(self.menuBar, tearoff=0)
        self.filemenu.add_command(label="Toggle Screen Size (s)", command=self.toggleScreen)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Help (h)", command=self.helpMenu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit (q)", command=self.quit)
        self.menuBar.add_cascade(label="Main", menu=self.filemenu)
        self.editmenu = Menu(self.menuBar, tearoff=0)
        self.editmenu.add_command(label="Update Current Roster (u)", command=self.updateRoster)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Initialize New Roster ⚠", command=self.newRoster)
        self.menuBar.add_cascade(label="Edit", menu=self.editmenu)
        self.exportmenu = Menu(self.menuBar, tearoff=0)
        self.exportmenu.add_command(label="Daily Summary", command=self.getDaily)
        self.exportmenu.add_command(label="Total Summary", command=self.getTotal)
        self.menuBar.add_cascade(label="Export", menu=self.exportmenu)
        self.selectionmenu = Menu(self.menuBar, tearoff=0)
        self.selectionmenu.add_command(label="1 - Select (1)", command=self.first)
        self.selectionmenu.add_command(label="2 - Select (2)", command=self.second)
        self.selectionmenu.add_command(label="3 - Select (3)", command=self.third)
        self.selectionmenu.add_separator()
        self.selectionmenu.add_command(label="1 - Followup (Ctr+1)", command=self.firstFollowup)
        self.selectionmenu.add_command(label="2 - Followup (Ctr+2)", command=self.secondFollowup)
        self.selectionmenu.add_command(label="3 - Followup (Ctr+3)", command=self.thirdFollowup)
        self.selectionmenu.add_separator()
        self.selectionmenu.add_command(label="1 - Problem (z)", command=self.firstProblem)
        self.selectionmenu.add_command(label="2 - Problem (x)", command=self.secondProblem)
        self.selectionmenu.add_command(label="3 - Problem (c)", command=self.thirdProblem)
        self.menuBar.add_cascade(label="Select", menu=self.selectionmenu)

        """
        # creates the buttons that can be used for calling on students
        self.button = Button(root, text="QUIT", fg="red", command=quit)
        self.button.pack(side=RIGHT)
        self.slogan = Button(root, text="3", command = self.third)
        self.slogan.pack(side=RIGHT)
        self.slogan = Button(root, text="2", command = self.second)
        self.slogan.pack(side=RIGHT)
        self.slogan = Button(root, text="1", command = self.first)
        self.slogan.pack(side=RIGHT)
        """

        #creates the label for the student names
        self.l1 = Label(root, text=("1: " + str(self.students.get_student_data_small(1))+'   '+
                                    "2: " + str(self.students.get_student_data_small(2))+'   '+
                                    "3: " + str(self.students.get_student_data_small(3))+'   '))
        self.l1.config(font="Verdana, 25",justify=LEFT)
        self.l1.pack(side=LEFT)

        #creates the key bindings
        master.bind('h', self.helpMenu)
        master.bind('p', self.togglePronunciation)
        master.bind('n', self.toggleNickname)
        master.bind('u', self.updateRoster)
        #Too dangerous to leave on because it could easily be pressed and overwrite the data
        #master.bind('x', self.newRoster)
        master.bind('s', self.toggleScreen)
        master.bind('q', self.quit)
        master.bind('1', self.first)
        master.bind('2', self.second)
        master.bind('3', self.third)
        master.bind('<Control-space>', self.firstFollowup)
        master.bind('<Control-Key-1>', self.firstFollowup)
        master.bind('<Control-Key-2>', self.secondFollowup)
        master.bind('<Control-Key-3>', self.thirdFollowup)
        master.bind('z', self.firstProblem)
        master.bind('z', self.firstProblem)
        master.bind('x', self.secondProblem)
        master.bind('c', self.thirdProblem)
        master.bind('<space>', self.first)

        if(self.students.get_student_data_small(1) == 'No roster is loaded'):
            self.helpPopup.openHelp()

    #removes and updates the 1st
    def first(self, event=None):
        self.students.advance_by_position(1)
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 2nd
    def second(self, event=None):
        self.students.advance_by_position(2)
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 3rd
    def third(self, event=None):
        self.students.advance_by_position(3)
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 1st
    def firstProblem(self, event=None):
        self.students.advance_by_position(1, "problem")
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 2nd
    def secondProblem(self, event=None):
        self.students.advance_by_position(2, "problem")
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 3rd
    def thirdProblem(self, event=None):
        self.students.advance_by_position(3, "problem")
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 1st
    def firstFollowup(self, event=None):
        self.students.advance_by_position(1, "followup")
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 2nd
    def secondFollowup(self, event=None):
        self.students.advance_by_position(2, "followup")
        self.students.save_queue()
        self.updateLabels()
        return

    #removes and updates the 3rd
    def thirdFollowup(self, event=None):
        #print("CALLED")
        self.students.advance_by_position(3, "followup")
        self.students.save_queue()
        self.updateLabels()
        return

    #sets the labels to the top 3 people in the queue, call this whenever the queue is updated
    def updateLabels(self):
        #checks wether to show small/large for the gui label/screen size
        if(self.smallMode==1):
            top1, top2, top3 = self.students.get_student_data_small(1), self.students.get_student_data_small(2), self.students.get_student_data_small(3)
            self.l1.config(text=("1: " + str(top1)+'   '+"2: " + str(top2)+'   '+"3: " + str(top3)+'   '),justify=LEFT,font="Verdana, 25")
            self.l1.pack(side=LEFT,pady=0)
        else:
            top1, top2, top3 = self.parseBigData(self.students.get_student_data_big(1)), self.parseBigData(self.students.get_student_data_big(2)), self.parseBigData(self.students.get_student_data_big(3))
            #print(top1, top2, top3)
            self.l1.config(text=("1: " + str(top1) + '   '+"\n\n2: " + str(top2) + '   '+"\n\n3: " + str(top3) + '   '),font="Verdana, 35",justify=LEFT)
            self.l1.pack(side=TOP,pady=50)

    #sets the menu bar for the small gui
    def menuSmall(self):
        self.master.config(menu=self.menuBar)

    #changes the frame size to the smaller layout
    def smallScreen(self,master):
        #calculations for the size and placement of the small frame
        width = self.master.winfo_screenwidth() - 30
        height = self.master.winfo_screenheight() // 5
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = (screenWidth / 2) - (width / 2) - 10
        y = 0
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        return

    #sets the menu bar for the big gui
    def menuBig(self):
        self.master.config(menu=self.bigBar)

    #changes the frame size to the bigger layout
    def bigScreen(self,master):
        #calculations for the size and placement of the big frame
        width = self.master.winfo_screenwidth() - 30
        height = self.master.winfo_screenheight() - 100
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = (screenWidth / 2) - (width / 2) - 10
        y = 0
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        return

    #will parse the big gui data and decides what to show the gui
    #if there is a nickname or pronounciation then they will be shown too
    def parseBigData(self,data):
        displayData = ""
        #checks if nickname is present
        #print("DATA2: "+str(data[2])+" toggle: "+str(self.toggleNick))
        if(data[2]!=""):
            if(self.toggleNick==1):
                displayData = str(data[0]) + ", '" + str(data[2]) + "'"
            else:
                displayData = str(data[0])
        else:
            displayData = str(data[0])
        #checks if pronounciation should be shown
        if(data[1]!=""):
            if(self.togglePron == 1):
                return displayData+ "\n\t"+"["+ str(data[1])+"]"
        return displayData + "\n\t"

    #toggles between small/big screen modes (keypress s, default=small)
    def toggleScreen(self, event=None):
        if(self.smallMode==1):
            self.smallMode=0
            self.bigScreen(self.master)
            self.menuBig()
        else:
            self.smallScreen(self.master)
            self.smallMode=1
            self.menuSmall()
        self.updateLabels()
        return

    #When on big screen mode this toggles the option to show pronounciation (default = on)
    def togglePronunciation(self, event=None):
        if(self.togglePron==1):
            self.togglePron=0
        else:
            self.togglePron=1
        self.updateLabels()
        return

    #When on big screen mode this toggles the option to show pronounciation (default = on)
    def toggleNickname(self, event=None):
        if(self.toggleNick==1):
            self.toggleNick=0
        else:
            self.toggleNick=1
        self.updateLabels()
        return

    #ran first time the pragam has ever been run to set up database
    def newRoster(self, event=None):
        try:
            #self.students.data_repo.newterm()
            self.students.start_new_term() # New function to replace old way that caused errors
            #self.students.fill_both_bags_from_roster()
            self.students.save_queue()
            self.updateLabels()
        except:
            err="Failed to set up the new roster."
        return

    #updates the roster for changes such as student names with out rewriting all the past recorded data
    def updateRoster(self, event=None):
        try:
            # this is for starting a new term (baseinfo.tsv and database.tsv dont exist yet)
            self.students.update_roster_and_queue()
            self.students.save_queue()
            self.updateLabels()
        except:
            err="Failed to update the roster"
        return

    #opens window for entering the date
    def getDaily(self):
        #Create new frame for help menu
        rootHelp = Tk()
        rootHelp.title("Export Daily")
        #Set size of help frame and center it
        width = 300
        height = 100
        screenWidth = rootHelp.winfo_screenwidth()
        screenHeight = rootHelp.winfo_screenheight()
        x = (screenWidth / 2) - (width / 2)
        y = (screenHeight / 2) - (height / 2) + 50
        rootHelp.geometry("%dx%d+%d+%d" % (width, height, x, y))
        #Help Menu text
        l = Label(rootHelp, text="Type in the date for the daily export\n'YYYY-MM-DD' ex - 2019-04-28",justify=LEFT)
        l.pack(expand=YES)

        self.e = Entry(rootHelp)
        self.e.pack(expand=YES)

        testbutton = Button(rootHelp, text = "Grab Date", command = self.grabdate)
        testbutton.pack(expand=YES)

    #sends date to
    def grabdate(self):
        day = self.e.get()
        check = self.students.passthru_generate_daily(day)
        self.confirmation(check)
        return

    #calls the export total summary function
    def getTotal(self):
        check = self.students.passthru_generate_term()
        self.confirmation(check)
        return

    #shows success/fail when trying to export data
    def confirmation(self,check):
        message = Tk()
        message.title("Export Attempt")
        width = 150
        height = 100
        screenWidth = message.winfo_screenwidth()
        screenHeight = message.winfo_screenheight()
        x = (screenWidth / 2) - (width / 2)
        y = (screenHeight / 2) - (height / 2)
        message.geometry("%dx%d+%d+%d" % (width, height, x, y))
        l = Label(message, text=check)
        l.pack(expand=YES)

    #opens the help menu frame
    def helpMenu(self, event=None):
        self.helpPopup.openHelp()
        return

    #exits/quits the programs
    def quit(self, event=None):
        sys.exit()

#creates the application
root = Tk()
app = Application(root)
root.mainloop()
