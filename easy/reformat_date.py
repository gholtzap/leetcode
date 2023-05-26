#Solution 1

class Solution:
    def reformatDate(self, date: str) -> str:

        # Day Month Year
        # "20th Oct 2052"
        # ----------
        # "2052-10-20"

        day,month,year,output = "","","",""

        months = {
            "Jan":"01",
            "Feb":"02",
            "Mar":"03",
            "Apr":"04",
            "May":"05",
            "Jun":"06",
            "Jul":"07",
            "Aug":"08",
            "Sep":"09",
            "Oct":"10",
            "Nov":"11",
            "Dec":"12",
        }

        date = date.split(' ')

        # Find the year
        year = date[2]

        # Find the month
        month = months[date[1]]

        # Find the day

        day = date[0][:-2]

        #print(day)
        #if len(date[0]) == 4:
        #   day = date[0][0:2]
        #if len(date[0]) == 3:
         #   day = "0"+date[0][0:1]

        if len(day) == 1:
            day = "0"+day

        output+=year+"-"+month+"-"+day

        return output



# Solution 2

class Solution:
    def reformatDate(self, date: str) -> str:

        # Day Month Year
        # "20th Oct 2052"
        # ----------
        # "2052-10-20"

        day,month,year,output = "","","",""

        months = {
            "Jan":"01",
            "Feb":"02",
            "Mar":"03",
            "Apr":"04",
            "May":"05",
            "Jun":"06",
            "Jul":"07",
            "Aug":"08",
            "Sep":"09",
            "Oct":"10",
            "Nov":"11",
            "Dec":"12",
        }

        date = date.split(' ')

        # Find the year
        year = date[2]

        # Find the month
        month = months[date[1]]

        # Find the day

        day = date[0][:-2]

        #print(day)
        #if len(date[0]) == 4:
        #   day = date[0][0:2]
        #if len(date[0]) == 3:
         #   day = "0"+date[0][0:1]

        if len(day) == 1:
            day = "0"+day

        output+=year+"-"+month+"-"+day

        return output


# Solution 3

class Solution:
    def reformatDate(self, date: str) -> str:

        # Day Month Year
        # {"1st"} {"Jan"} {1910}


        # Convert to:
        # YYYY-MM-DD

        day,month,year = "","",""
        output = ""

        months = {
            "Jan":"01",
            "Feb":"02",
            "Mar":"03",
            "Apr":"04",
            "May":"05",
            "Jun":"06",
            "Jul":"07",
            "Aug":"08",
            "Sep":"09",
            "Oct":"10",
            "Nov":"11",
            "Dec":"12",
        }

        date = date.split(' ')
        print(date)

        # Find the year
        year = date[2]

        # Find the month

        month = months[date[1]]

        # Find the day
        
        for x in date[0]:
            print(x,ord(x))
            if ord(x) >=48 and ord(x) <= 57:
                day+=x
            else:
                break

        #print(year)
        #print(month)
        print(day)

        if len(day) < 2:
            day = "0"+day

        output+=year+"-"+month+"-"+day

        return output