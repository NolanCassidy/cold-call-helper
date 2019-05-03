**Project title**

Cold Call Helper is a program to help an instructor randomly call on students in a fair way. (randomly but equally)

**Screenshots**
![coldcall6](https://user-images.githubusercontent.com/22786772/57169506-02d05e00-6dbc-11e9-87d7-a78dbd981737.png)
![coldcall1](https://user-images.githubusercontent.com/22786772/57169507-02d05e00-6dbc-11e9-9bc1-32e47ea9ed1e.png)
<img width="647" alt="coldcall2" src="https://user-images.githubusercontent.com/22786772/57169508-02d05e00-6dbc-11e9-9e34-595ee222c919.png">
<img width="380" alt="coldcall3" src="https://user-images.githubusercontent.com/22786772/57169509-02d05e00-6dbc-11e9-9cb6-be52c8ca7cde.png">
<img width="448" alt="coldcall4" src="https://user-images.githubusercontent.com/22786772/57169510-02d05e00-6dbc-11e9-9dd7-24d7e75e58a9.png">
![coldcall5](https://user-images.githubusercontent.com/22786772/57169511-0368f480-6dbc-11e9-8405-79980da98ba7.png)


**Tech/framework used**

**Built with**

-   Python 3

-   Tk

**Features**

-   Display top three random student names

    -   Press 1,2,3 to select and move onto next student

-   Small & Large GUI options for bigger text size, student pronunciation, and
    nickname.

-   Extra selections for if the student needs a follow-up or was a
    problem/absent

-   Daily/Term summary options outputted into txt files

-   Saves information and queue ordering when closing the program

-   Update the information of students from a tsv file editable in excel

**Important Files**

Show what the library does as concisely as possible, developers should be able
to figure out **how** your project solves their problem by looking at the code
example. Make sure the API you are showing off is obvious, and that your code is
short and concise.

**Installation**

1.  If you do not have python version 3 installed on your computer, do so first.

    1.  Visit https://www.python.org/downloads/ to find a download for your
        operating system

2.  Unzip ColdCall.zip into an easily accessible folder on your computer.

3.  Edit roster.tsv located inside the Directory with current student
    information. Read the User Documentation to see the proper format for the
    student information.

4.  Open your computer’s console.

    1.  On Windows, you can do this by going to run and typing in ‘cmd’ to open
        command prompt.

    2.  On Mac press Control + Option + Shift + T to open the terminal window

    3.  On linux, press Control + Shift + T to open a terminal window

5.  Navigate to the ColdCall folder using cd.

    1.  If you need help navigating your console, read the following tips:

    2.  Type ‘cd \<directory name\>’ to go into a directory and ‘cd ..’ to go up
        one directory level to navigate.

    3.  Type ‘ls’ on Mac or Linux and ‘dir’ on Windows to look at the
        directories under the directory you are in.

6.  Now cd into either the Mac folder or the Windows folder, depending on which
    operating system you are on.

7.  Type ‘python3 ColdCallHelper.py’ and press enter to start up the Cold Call
    Helper application.

8.  The application should now be running, but if this is the first time ever,
    and if your ‘roster.tsv’ file is already set up, press ‘Initialize Roster’
    to import the student data and start using the program.

**How to use?**

Before using the Cold Call Helper, you will need to create a ‘roster.tsv’ file
with the data from your students in it. You can do this two ways, either in a
simple text editor like notepad, or in Microsoft Excel.

When the application is launched for the first time, the Help Menu and Small GUI
will display. The Help Menu will be in the center of the monitor, and will
explain the functions of every command available to the Cold Call Helper
program. This Help Menu can also be accessed at any time through the menu bar by
going to “File” and clicking “Help”. The Small GUI will appear at the top of the
screen, and display the top three student names inside the queue. Initially, the
queue will be blank, and the Small GUI will display this by saying “No roster is
loaded” for every queue spot.

To import a roster into the Cold Caller, go to the menu bar and click “Edit”,
and then “Initialize New Roster”. WARNING: THIS WILL ERASE ALL PREVIOUS ROSTER
DATA.

To update a current roster in the Cold Caller, first ensure that the new
roster.tsv file has replaced the old one in the directory. Then, go to the menu
bar and click “Edit”, and then “Update Current Roster”.

Note that the Followup keys are designed for students in the queue that need
additional help with the material, and they will be marked with a Followup mark
in the daily report. Additionally, the Problem keys are designed for students in
the queue that are either inattentive or absent, and a Problem mark will appear
on their profile in the daily report.

In order to change to Full Screen Mode, go to the menu bar, go to “Main”, and
click “Toggle Screen Size”. This will switch the window from Small GUI mode to
Full Screen Mode. “Toggle Screen Size” is also used to change from Full Screen
Mode to Small GUI mode as well. Notice that the function for phonetic
pronunciation of student names is ONLY for the Full Screen Mode. The Help Menu
can also be opened by pressing “Help” in “Main” on the menu bar.

**Motivation**

Cold Call Helper was created for Anthony Hornoff’s Spring 2019 Software

Methodology class (CIS 422). The first class project was to develop this

software, based on a System Requirement Specification (written by the

professor), perform project management over the whole project, and write all

the documentation that a commercial product would need.

**Contributions**

Cold Call Helper was written by Nolan Cassidy, Andrew Evelhoch, Jake Gianola, Kyle Kincaid, Kylie Quan

Date last updated: 4/29/2019

MIT © [Nolan Cassidy](https://github.com/NolanCassidy)
