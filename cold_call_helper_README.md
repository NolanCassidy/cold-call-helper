**Project title**

Cold Call Helper is a program to help an instructor randomly call on students

in a fair way.

**Screenshots**

![https://lh4.googleusercontent.com/77r7CITnsevw_fN6ttt9JJLvY7z6KN2U0emk72Hz7-VmIca0l5Z4xlHAMqMzGAE_Oxt2hKImUC14IUSp7dSAWL6BJ0FW1AYvNY0juOt8pkODXjEygPukkere8fn8QQTYDiI0AF8E](media/d808431b9b1f85b2377e74fd1b16ad57.png)

![https://lh5.googleusercontent.com/yljzN8dn2D9XNUOoI2PboJa9rmAwqPxzeRSmnsA58Cg0o2Atu0bcjguZ3gwn9Jm-AcVNdgHYSg3QzUHBkU134dwa4lOh9WxcpnqUH4CdS5tYU1wO9fX37ageWR4VMIbx7EQuYhYk](media/55c3170b91bbd82b74357a2ee3821771.png)

![https://lh6.googleusercontent.com/ZzSdTkvEPXdRV3QRi0hk23v_uENi1RRFVU65jcCLzmDws7jmbxodSwS8SOqKcOacrshydynYu5E0KnzIz3FRNDDsHdKssh8LbBssyubdOSHH4qag2-Mtr9NmDSz9gF1EevoY6zJF](media/7f151f906e0514ac0a9d78f30a087909.png)

![https://lh4.googleusercontent.com/so3njk6M28mE48t6dH3HduQuwq5WEr0g7EJ5EOGVvbnQxYVD6MopaDF2NrrXEswnZsLFtCH6jdp0JzeWk8hH5Ibz_1VcCnFDV-a8K6NL88Jt9TtDjIetz0RjZA9qlK3uOG-NclGr](media/b126bf41307c7225b3c172a9689dfb61.png)

![](media/0c352f964334cf1aec61022680901759.png)

![](media/45ee35d51c256d8f6d901ba652680679.png)

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

Cold Call Helper was written by Nolan Cassidy, Andrew Evelhoch, Jake Gianola,

Kyle Kincaid, Kylie Quan

Date last updated: 4/29/2019

MIT © [Nolan Cassidy](https://github.com/NolanCassidy)
