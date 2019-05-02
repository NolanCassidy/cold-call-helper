import class_Queue
"""
Last Update:4/29/2019
created by Kylie

Creates a summary from a given set of student day. This will format the data with headers for each of the variables and save the output as a .txt file in the local directory.
"""
class daily_sum:
    def __init__(self, day_info,day):
        #self.cq = class_Queue.class_Queue()

        # Request student info from repository through the queue.
        #self.info = self.cq.passthru_generate_daily()
        self.info = day_info
        self.daily_sum = []
        self.day=day
        # Extract only the data needed for daily summary.
        for i in self.info:
            student = []
            student.append(i[3]) # total times called
            student.append(i[4]) # problems with answer
            student.append(i[5]) # follow up needed
            student.append(i[1]) # first name
            student.append(i[2]) # last name
            student.append(i[0]) # UO ID
            student.append(i[7]) # email address
            student.append(i[6]) # phonetic spelling
            self.daily_sum.append(student)

    def create_txt_file(self):
        # Write txt file.
        file = open('Daily_Summary_{}.txt'.format(str(self.day).replace("/","_")), 'w')

        # Headers for txt file.
        headers = ["Total Times Called:", "Problem:",
                   "Follow Up:", "First Name:", "Last Name:",
                   "UO ID:", "Email Address:", "Phonetic Spelling:\n"]

        # Get distance between fields in txt file.
        max_sizes  = [len(headers[0]), len(headers[1]), len(headers[2]),
                      len(headers[3]), len(headers[4]), len(headers[5]),
                      len(headers[6])]

        # Change value in max_sizes list if length of the string rep of a
        # value in daily_sum list exceeds it.
        for i in range(len(self.daily_sum)):
            for j in range(len(self.daily_sum[i]) - 1):
                if (len(str(self.daily_sum[i][j])) > max_sizes[j]):
                    max_sizes[j] = len(str(self.daily_sum[i][j]))

        # Increment value in max_sizes list by 4 if length of the string rep
        # of a value in headers list exceeds it.
        for i in range(len(headers)):
            if (i < len(headers)-1):
                word_size = len(str(headers[i]))
                if (max_sizes[i] == word_size):
                    max_sizes[i] = max_sizes[i] + 4

        # Increment value in max_sizes list by 4 if length of the string rep
        # of a value in daily_sum list exceeds it.
        for i in range(len(self.daily_sum)):
            for j in range(len(self.daily_sum[i])):
                if (j < len(self.daily_sum[i])-1):
                    word_size = len(str(self.daily_sum[i][j]))
                    if (max_sizes[j] == word_size):
                        max_sizes[j] = max_sizes[j] + 4

        # Write headers to txt file.
        for i in range(len(headers)):
            if (i < len(headers) - 1):
                word_size = len(str(headers[i]))
                if (max_sizes[i] == word_size):
                    spaces = " " * 4
                else:
                    dif = max_sizes[i] - word_size
                    spaces = " " * dif
                file.write(headers[i] + spaces)
            else:
                file.write(headers[i])

        # Write student info to txt file.
        for i in range(len(self.daily_sum)):
            for j in range(len(self.daily_sum[i])):
                if (j < len(self.daily_sum[i])-1):
                    word_size = len(str(self.daily_sum[i][j]))
                    dif = max_sizes[j] - word_size
                    spaces = " " * dif
                    file.write(str(self.daily_sum[i][j]) + spaces)
                else:
                    file.write(str(self.daily_sum[i][j]) + '\n')

        file.close()

if __name__ == '__main__':
    r = daily_sum()
    r.create_txt_file()
