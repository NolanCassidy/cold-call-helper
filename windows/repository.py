import csv
import datetime
import os

# information repository code
# created by Kevin Kincaid

#Last Update:4/29/2019

#upadate (April 25,2019, 8:01 PM) (Version 8)
#fixed begin() function so program works if files not yet created
#made it so newroster doesn't overwrite stuff if it fails
#added calendar function and fixed issues with dates
# IMPORTANT- the queue must have a way to activate all public function




#update (April 24, 2019, 11:33 AM) (Version 7)
#added error proofing
#stopped the program from ignoring preferred names when FAFSA flag is not there

#update (April 21, 2019, 4:35 PM) (Version 6) (hopefully final)
#fixed newterm/editterm functionality
#added documentation
#fixed errors to check on first time running the program

#update (April 19, 2019, 10:51 PM)
#addressed the system for FERPA capability
#added preferred name options
#made more resilient when reading from Roster
#create file to pass to queue based on the FERPA
#(roster testing in progress, and I am not sure how to tell the queue about the changes I made)

#update (April 18, 2019, 2:30 PM)
#updated to have the system keep track of individual days, and group daily reports by that
#added in 'newterm' function where you import the first roster

#update(April 18, 2019, 9:00 AM): changed to add unique identifiers and use them in place of duck IDs


#databoard class - public functions
#   begin() - starts the program at the beginning of a session
#           returns "No file currently created" if files are missing or damaged
#           returns "Ready" if ready

#   newterm() - loads in information from 'roster.tsv' as a new class
#           returns "No file currently created" if file is missing
#           returns "empty roster file given" if file is empty
#           returns "roster successfully loaded"

#   editterm() - edits current class to fit 'roster.tsv'
#           returns "No file currently created" if file is missing
#           returns "empty roster file given" if file is empty
#           returns "roster successfully updated" if successful
#           format: each row of tsv file is [duck ID, firstname, lastname, FERPA, email, phoenetic, preferred]



#   newqueue() - create a list for the queue
#           returns list of unique ids



#   feedback(identifier,info) - note feedback about a specific student's answer
#           input format: use unique id and "followup", "problem", or "normal"

#   display(identifier) - get display information from a student
#           returns [first name, last name, phoenetic, preferredname]
#           return["","","",preferredname]
#           return "invalid indentifier"

#
#   calendar()
#           returns a list where each string is an active day

#   generatedaily() - create daily report
#           returns list of all student info
#           format [duck ID, firstname, lastname, times called today, problems today, follow up today, phoenetic pronunciation, email, preferred name]

#   generatetotal() - create total report
#           returns list of all student info
#           format [duck ID, firstname, lastname, times called, problems with answer, follow up needed, phoenetic pronunciation, email, preferred name]



#duck ID 0
#firstname 1
#lastname 2
#times called 3
#problems with answer 4
#follow up needed 5
#called today 6
#problems today 7
#follow up today 8
#phoenetic pronunciation 9
#FERPA 10
#email 11
#unique identifier 12
#preferred name 13

#class made for loading, editing, and passing data for individual students
class databoard:
    lineset = []
    uniqueid = 1000
    kepttrack = []
    active = "False"

    #starts the program at the beginning of a session
    def begin(self):
        try:
            fh = open('database.tsv', 'r')
        except FileNotFoundError:
            return "No file currently created"
        try:
            fh = open('baseinfo.tsv', 'r')
        except FileNotFoundError:
            return "No file currently created"


        with open("baseinfo.tsv") as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter="\t")
            x = 1
            for line in tsvreader:
                if(x == 1):
                    self.uniqueid = int(line[0])
                elif(x == 3):
                    self.active = line[0]
                x += 1 #Something like thiS??????????

        if(self.active == "False"):
            return "No file currently created"
        else:
            self.startup()
            return "Ready"


    #generates a unique id for any new students
    def genid(self):
        self.uniqueid += 1
        return str(self.uniqueid)

    #save current info contained in lineset to a tsv file
    def save(self):
        #print("")
        #print("saved")
        with open('baseinfo.tsv','wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow([self.uniqueid])
            tsv_writer.writerow([self.active])
            tsv_writer.writerow(self.kepttrack)

        with open('database.tsv', 'wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            for line in self.lineset:
                tsv_writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[9],line[10],line[11],line[12],line[13]])
                tsv_writer.writerow(line[6])
                tsv_writer.writerow(line[7])
                tsv_writer.writerow(line[8])
                #print(line)



    #process of editing term
    def editterm(self):
        prevlist = self.newqueue()
        newset = []
        nextlist = []

        try:
            fh = open('roster.tsv', 'r')
        except FileNotFoundError:
            return "No file currently created"
        check = 1
        with open('roster.tsv') as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter='\t')
            x = 1
            missed = []
            for j in range(len(self.kepttrack)):
                missed.append(0)

            for line in tsvreader:
                if(x == 1):
                    newstudent =  True
                    for piece in range(len(self.lineset)):
                        if(line[0]==self.lineset[piece][0]):
                            prefer = ""
                            phoe = ""
                            if(len(line) == 7):
                                if(line[6] != ""):
                                    prefer = line[6]
                            if(line[3] == "TRUE"):
                                if(len(line)==7):
                                    prefer = line[6]
                                    if(prefer==""):
                                        prefer = "unnamed"
                                else:
                                    prefer = "unnamed"
                            if(len(line) >= 6):
                                phoe = line[5]
                            pause = self.lineset[piece]
                            newset.append([line[0],line[1],line[2],pause[3],pause[4],pause[5],pause[6],pause[7],pause[8],phoe,line[3],line[4],pause[12],prefer])

                            newstudent = False
                    if(newstudent):
                        prefer = ""
                        phoe = ""
                        if(len(line) == 7):
                            if(line[6] != ""):
                                prefer = line[6]
                        if(line[3] == "TRUE"):
                            if(len(line)==7):
                                prefer = line[6]
                                if(prefer==""):
                                    prefer = "unnamed"
                            else:
                                prefer = "unnamed"
                        if(len(line) >= 6):
                            phoe = line[5]
                        temp = self.genid()

                        newset.append([line[0],line[1],line[2],0,0,0,missed,missed,missed,phoe,line[3],line[4],temp,prefer])
                        nextlist.append(temp)
                    x += 1
                else:
                    x -= 1
                check += 1
        if(check == 1):
            return "empty roster file given"
        #for number in prevlist:
            #if(number != "kept"):
                ##print(number)
                #tell queue to deletestudent(number)
        #for number in nextlist:
            #tell queue to addstudent(number)
            ##print(number)

        self.lineset = newset.copy()
        self.save()
        return "roster successfully updated"

    #sets up information from a formatted roster
    # ID firstname lastname FERPA email phoenetic preferred
    def newterm(self):
        try:
            fh = open('roster.tsv', 'r')
        except FileNotFoundError:
            return "No roster file currently created"
        check = 1
        self.lineset = []
        with open("roster.tsv") as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter="\t")
            x = 1
            for line in tsvreader:
                if(x == 1):
                    #print(line)
                    prefer = ""
                    phoe = ""
                    if(len(line) == 7):
                        prefer = line[6]
                    if(line[3] == "TRUE"):
                        if(len(line)==7):
                            prefer = line[6]
                            if(prefer==""):
                                prefer = "unnamed"
                        else:
                            prefer = "unnamed"
                    if(len(line) >= 6):
                        #print("true")
                        phoe = line[5]

                    self.lineset.append([line[0],line[1],line[2],0,0,0,[0],[0],[0],phoe,line[3],line[4],self.genid(),prefer])
                    x += 1
                else:
                    x -= 1
                check += 1
        if(check == 1):
            return "empty roster file given"

        self.active = "True"
        self.save()
        self.kepttrack = []
        self.kepttrack.append(str(datetime.date.today()))
        return "roster successfully loaded"

    #load information from a tsv file into lineset
    def startup(self):
        #print("")
        #print("loaded")
        newday = False
        with open("baseinfo.tsv") as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter="\t")
            x = 1
            for line in tsvreader:
                if(x == 1):
                    self.uniqueid = int(line[0])
                elif(x == 3):
                    self.active = line[0]
                elif(x == 5):
                    for i in line:
                        self.kepttrack.append(i)
                    if(self.kepttrack == []):
                        self.kepttrack.append(str(datetime.date.today()))
                    if(str(datetime.date.today()) !=  self.kepttrack[len(self.kepttrack)-1]):
                        #print(datetime.date.today())
                        #print(self.kepttrack[len(self.kepttrack)-1])
                        self.kepttrack.append(str(datetime.date.today()))
                        newday = True
                x += 1
        with open("database.tsv") as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter="\t")
            y = 0
            x = 1
            for line in tsvreader:
                if(x == 9):
                    y+=1
                    x = 1

                if(x == 1):
                    #print (line)

                    self.lineset.append([line[0],line[1],line[2],int(line[3]),int(line[4]),int(line[5]),0,0,0,line[6],line[7],line[8],line[9],line[10]])
                    #self.lineset.append([line[0],line[1],line[2],int(line[3]),int(line[4]),int(line[5]),int(line[6]),int(line[7]),int(line[8]),line[9],line[10],line[11]])

                elif(x == 3):
                    holdback = []
                    #print (line)
                    for i in line:
                        holdback.append(int(i))
                    if(newday):
                        holdback.append(0)
                    self.lineset[y][6] = holdback

                elif(x == 5):
                    holdback = []
                    #print (line)
                    for i in line:
                       holdback.append(int(i))
                    if(newday):
                        holdback.append(0)
                    self.lineset[y][7] = holdback

                elif(x == 7):
                    holdback = []
                    #print (line)
                    for i in line:
                        holdback.append(int(i))
                    if(newday):
                        holdback.append(0)
                    self.lineset[y][8] = holdback

                x += 1



    #given a student name and information, updates their information based on how they answered the question
    def feedback(self,identifier,info):
        for line in self.lineset:
            if(identifier == line[12]):
                if(info == "followup"):
                    line[5] += 1
                    line[8][len(line[8])-1] += 1
                elif(info == "problem"):
                    line[4] += 1
                    line[7][len(line[7])-1] += 1
                line[3] += 1
                line[6][len(line[6])-1] += 1
                self.save()



    #replaces a field of a specified student with new information
    def edit(self, identifier, newinfo, field):
        for line in self.lineset:
            if(line[12] == identifier):
                if((field == 1)or(field == 2)or(field == 9)or(field == 10)or(field == 11)):
                    line[field] = newinfo


    #returns a list of all student identifiers
    def newqueue(self):
        queuelist = []
        for line in self.lineset:
            queuelist.append(line[12])
        return queuelist


    #returns the name of a specific student
    def display(self, identifier):
        for line in self.lineset:
            if(line[12] == str(identifier)): # Changed this???
                #print("hit")
                #print([line[1],line[2],line[9],line[13]])
                #print(line[10])
                #firstname lastname phoenetic pronunciation preferred name
                if(line[10] == 'FALSE'):
                    return[line[1],line[2],line[9],line[13]]
                else:
                    return["","","",line[13]]
        return "invalid indentifier"


    #returns a list of lists, where each row contains data for a student's performance for a given day
    #currently formatted by "year-month-day"
    def generatedaily(self,day):
        # date is formatted by "year-month-day"

        dailylist = []
        p = 0
        found = "none"

        for k in self.kepttrack:
            if(str(k) == day):
                late = p
                found = "yes"
            p += 1
        #print("found: "+found)
        if(found == "none"):
            return "Invalid date"
        for line in self.lineset:
            dailylist.append([line[0],line[1],line[2],line[6][late],line[7][late],line[8][late],line[9],line[11],line[13]])
        return dailylist
        #return format (entry in list):
        #[ID  firstname  lastname   times called today   problems today   follow up today   phoenetic pronunciation   email   preferred name]

    #ID  firstname  lastname   times called today   problems today   follow up today   phoenetic pronunciation   email   preferred name


    #returns a list of lists, where each row contains data for a student's performance for the whole term
    #returns a list containing data for each student's performance for the term
    def generatetotal(self):
        termlist = []
        for line in self.lineset:
            termlist.append([line[0],line[1],line[2],line[3],line[4],line[5],line[9],line[11],line[13]])
        return termlist

    #ID   firstname   lastname   times called    problems with answer   follow up needed   phoenetic pronunciation   email   preferred name

    #returns a list where each string is an active day
    def calendar(self):
        daysoflives = []
        for i in self.kepttrack:
            daysoflives.append(str(i))
        return daysoflives







#baseline = ["ID","firstname","lastname"]
#Current = databoard()
#if(Current.begin() == "No file currently created"):
#    Current.newterm()

#Current.newterm()
#Current.startup()
#Current.editterm()
#Current.save()
#Current.edit("1003","definitely not batman",9)
#Current.save()
#Current.feedback("1003","problem")
#Current.feedback("1002","followup")
#showoff = Current.generatedaily("2019-04-17")

#for l in showoff:
 #   #print(l)

##print(Current.display('1002'))
##print(Current.genid())


##print(Current.calendar())
##print(Current.generatedaily(Current.calendar()[0]))
