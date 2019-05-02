"""
Name: class_Queue.py
Author: Andrew Evelhoch
Last Update:4/29/2019
Simple implementation of a bag-style queue that serves up each item in the bag in a random order before reshuffling and
serving it in a random order again. Because there is peeking into the bag, there must be two lists to make sure that the
'front-facing' bag always has at least a top 3 to peek at.

Interfaces:
Function name               Class       What data
    From:
fill_bags_from_roster       Data Repo   List of all student IDs in the class
fill_back_bag_from_roster   Data Repo   List of all student IDs in the class
remove_id_from_roster       Data Repo   ID to remove from the queue
insert_id_into_roster       Data Repo   ID to add to the queue
advance_by_position         GUI         Position of student to remove from front of queue (1-indexed)
    To:
get_student_data_small      GUI         String containing name of student
get_student_data_big        GUI         List of three strings: [ Full name, Nickname, Pronounciation ]
"""
import random
import repository
import termsum
import dailysum


class class_Queue:
    def __init__(self):
        self.front_bag = []  # The 'front' bag that the top 3 students are viewed from. It should always be full.
        self.back_bag = []  # The 'back' bag. Once it empties into the front bag, it should be refilled and shuffled.
        self.front_students = [[None,None,None,None],[None,None,None,None],[None,None,None,None]]
        self.data_repo = repository.databoard()

    def start_new_term(self): # New function to add additional functionality and keep queue consistent with database.tsv
        self.data_repo.newterm()
        self.front_bag = []
        self.back_bag = []
        self.fill_both_bags_from_roster()

    def fill_both_bags_from_roster(self):
        # Fills both bags with the students in the class and randomizes them. Only called when queue is first set-up.
        for student in self.data_repo.newqueue():
            self.front_bag.append(student)
            self.back_bag.append(student)
        random.shuffle(self.front_bag)
        random.shuffle(self.back_bag)
        self.update_student_data()
        pass

    def TEST_fill_both_bags_from_roster(self):
        # Dummy testing function that fills bag with ID's 1 to num (should be greater than 3)
        for student in self.DUMMY_roster:
            self.front_bag.append(student)
            self.back_bag.append(student)
        random.shuffle(self.front_bag)
        random.shuffle(self.back_bag)
        self.update_student_data()

    def fill_back_bag_from_roster(self):
        # Fills back bag with students in the class and randomizes it
        for student in self.data_repo.newqueue():
            self.back_bag.append(student)
        pass

    def TEST_fill_back_bag_from_roster(self):
        # Dummy testing function to refill the bag with ID's 1 to num
        for student in self.DUMMY_roster:
            self.back_bag.append(student)
        pass

    def TEST_print_bags(self):
        # Test function that prints both bags
        #print("front",self.front_bag)
        #print("back",self.back_bag)
        return

    def check_back_empty(self):
        # Returns true if back bag is empty, false otherwise
        if len(self.back_bag) == 0:
            return True
        else:
            return False

    def push_from_back_front(self):
        # Pushes the front item of the back bag into the last (empty) space of the front bag
        # If that was the last item in the back bag, refill it and re-randomize it, ensuring no local repeats
        self.front_bag.append(self.back_bag.pop(0))
        if self.check_back_empty():
            self.fill_back_bag_from_roster()
            random.shuffle(self.back_bag)
            # check for dupes: back bag 1 cant be in front back 2, back bag 2 cant be front back 1
            if len(self.front_bag) > 5 and len(self.back_bag) > 5:
                front_pos_last = self.front_bag[-1]
                front_pos_second_last = self.front_bag[-2]
                no_repeats = False
                while not no_repeats:
                    back_pos_first = self.back_bag[0]
                    back_pos_second = self.back_bag[1]
                    if back_pos_first != front_pos_last and back_pos_first != front_pos_second_last:
                        if back_pos_second != front_pos_last:
                            no_repeats = True
                        else: random.shuffle(self.back_bag)
                    else: random.shuffle(self.back_bag)

    def update_student_data(self):
        # Gets the data of the student for each of the first 3 students in the bag by ID from the data repo
        ids = self.front_bag[0:3]
        students = []
        for id in ids:
            students.append(self.data_repo.display(id))
        for x in range(0, 3):
            for y in range(0, 4):
                self.front_students[x][y] = students[x][y]

    def get_student_data_small(self,position):
        # Returns a string with the students in position position's nickname (if available) or first name and last name
        position -= 1
        return_me = ""
        if self.front_students[position][3] != '':
            if self.front_students[position][1] != '':
                return_me = str(self.front_students[position][3]) + " " + str(self.front_students[position][1])
            else:
                return_me = str(self.front_students[position][3])
        else:
            return_me = str(self.front_students[position][0]) + " " + str(self.front_students[position][1])
        if return_me == "None None":
            return "No roster is loaded"
        else:
            return return_me

    def get_student_data_big(self,position):
        # Returns a list of strings for the student in position with first/last name, nickname and pronounciation
        position -= 1
        return_me = []
        if self.front_students[position][0] == '':
            return_me.append(self.front_students[position][3])
        else:
            return_me.append(str(self.front_students[position][0]) + " " + str(self.front_students[position][1]))
        return_me.append(str(self.front_students[position][2]))
        return_me.append(str(self.front_students[position][3]))
        if return_me == ['None None', 'None', 'None']:
            return "No roster is loaded"
        else:
            return return_me

    def advance_by_position(self, position, comment = ""):
        # When passed a position from 1 to 3, removes that student from the queue and advances the bags
        self.data_repo.feedback(str(self.front_bag[position - 1]), comment)
        output = self.front_bag.pop(position - 1)
        self.push_from_back_front()
        self.update_student_data()
        pass

    def remove_id_from_roster(self, student):
        # When a student is removed from the roster, this function searches the queue and removes them
        first_remove = True
        student = int(student) # added this line
        while student in self.front_bag:
            self.front_bag.remove(student)
            if first_remove:
                first_remove = False
            else:
                self.push_from_back_front()
        while student in self.back_bag:
            self.back_bag.remove(student)
        pass

    def insert_id_into_roster(self, student):
        # When a student is added to the roster, this function adds it to the queue
        self.front_bag.insert(random.randint(0, len(self.front_bag)), student)
        self.back_bag.insert(random.randint(0, len(self.back_bag)), student)

    def save_queue(self):
        # Saves the queue to 'queue.dat' can be loaded later
        file = open("queue.dat","w")
        writeMe = ""
        for num in self.front_bag:
            writeMe += str(num)
            writeMe += ","
        writeMe = writeMe[:-1]
        writeMe += "\n"
        for num in self.back_bag:
            writeMe += str(num)
            writeMe += ","
        writeMe = writeMe[:-1]
        writeMe += "\n"
        file.write(writeMe)
        file.close()
        pass

    def load_queue(self):
        # Loads the queue from 'queue.dat' Returns True if it worked, False if it doesnt
        try:
            with open("queue.dat") as file:
                self.front_bag = []
                firstLine = True
                self.back_bag = []
                for line in file:
                    line = line[:-1]
                    line = line.split(",")
                    for ID in line:
                        if firstLine == True:
                            self.front_bag.append(int(ID))
                        else:
                            self.back_bag.append(int(ID))
                    firstLine = False
        except:
            return False
        self.update_student_data()
        return True

    def update_roster_and_queue(self):
        # Updates the queue by adding or removing IDs from students added or removed to the roster when editing
        old_list = self.data_repo.newqueue()
        remove_list = []
        add_list = []
        if self.data_repo.editterm() == "roster successfully updated":
            new_list = self.data_repo.newqueue()
            for student in old_list:
                if student not in new_list:
                    remove_list.append(student)
            for student in new_list:
                if student not in old_list:
                    add_list.append(student)
        #print("adding:",add_list,"removing",remove_list)
        for student in remove_list:
            self.remove_id_from_roster(student)
        for student in add_list:
            self.insert_id_into_roster(student)
        self.update_student_data()
        pass

    # (Kylie) only modification: made a call to calendar() from repository.py
    def passthru_generate_daily(self, day = ""):
        # Generate a text file daily summary of all participation records for students
        if day is "":
            return "Failed! Incorrect Date"
        #print("DAY- "+str(day))
        info = self.data_repo.generatedaily(day)
        if info == "Invalid date":
            return "Failed! Incorrect Date"
        #print(info)
        try:
            ds = dailysum.daily_sum(info,day)
            ds.create_txt_file()
        except:
            return "Failed! Incorrect Date"
        return "Success!"

    def passthru_generate_term(self):
        # Generate a text file term summary of all participation records for students
        ts = termsum.term_sum(self.data_repo.generatetotal())
        ts.create_txt_file()
        return "Success!"


"""
if __name__ == '__main__':
    w = "poo"
    Q = class_Queue()
    while w != "Q":
        w = input("what is your wish:")
        if w == " ":
            Q.TEST_print_bags()
        elif w == "FIRSTRUN":
            Q.data_repo.newterm() # this is for starting a new term (baseinfo.tsv and database.tsv dont exist yet)
            Q.fill_both_bags_from_roster()
        elif w == "RELOAD":
            if Q.data_repo.begin() == "Ready":
                Q.data_repo.startup() # this is load existing class from file
                if not Q.load_queue():
                    Q.fill_both_bags_from_roster()
            else:
                #print("File does not exist. Use 'new term' instead.")
        elif w == "GETDATA":
            w = input("whats the ID")
            #print(Q.data_repo.display(w))
        elif w == "GETSMALL":
            w = input("which position?")
            w = int(w)
            #print(Q.get_student_data_small(w))
        elif w == "GETBIG":
            w = input("which position?")
            w = int(w)
            #print(Q.get_student_data_big(w))
        elif w == "EDIT":
            Q.update_roster_and_queue()
        elif w == "1":
            w = input("Any comment?")
            Q.data_repo.feedback(Q.front_bag[0],w)
            Q.advance_by_position(1)
            Q.save_queue()
        elif w == "2":
            w = input("Any comment?")
            Q.data_repo.feedback(Q.front_bag[1], w)
            Q.advance_by_position(2)
            Q.save_queue()
        elif w == "3":
            w = input("Any comment?")
            Q.data_repo.feedback(Q.front_bag[2], w)
            Q.advance_by_position(3)
            Q.save_queue()
        elif w == "Q":
            Q.save_queue()
            #print("bye")

        elif w == "SAVE":
            Q.save_queue()
        elif w == "LOAD":
            #print(Q.load_queue())
        elif w == "FILL":
            Q.fill_both_bags_from_roster()
        elif w == "fill":
            Q.TEST_fill_both_bags_from_roster()
        elif w == "del":
            w = input("which ID?")
            w = int(w)
            Q.remove_id_from_roster(w)
        elif w == "add":
            w = input("which ID?")
            w = int(w)
            Q.insert_id_into_roster(w)
        elif w == "update":
            Q.update_student_data()
        else:
            #print("I dunno lol")
        pass
"""
