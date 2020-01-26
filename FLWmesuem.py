# Bohmasterflex
# 1/23/2020
# Frank LLoyd Wright
# I will be attempting to make a cash register application that takes into account how many people are present for a tour
# and then gives a total amount of money owed. Also eventually we will want skus with hard coded prices.
# we wll want an EOD report on how many people participated and how much money was accquired from these transactions.
# Extensive use of try except will be likely.
# Roll tide


# get amount of people
def howMany():
    while True:
        try:
            people = int(input("Please enter in how many people in total there are: "))
            break
        except:
            print("Please enter in whole numbers only!")
            continue    
    return people


# Going to gather amounts of adults and elderly(seperate prices) and compare that to peopleto ensure numbers add up.
# need to figure out how to handle negative values
# Unsure how to utilize while loop here
# Need to figure out how to convert for group(doesnt matter if everyone is an adult will be $5/person regardless)
# Gather inputs before loop: use loop if folks != people
def demographicstracking(people):
    folks = 0
    while not folks == people:
        try:
            adults = int(input("How many adults are there?: "))
            senior_citizens = int(input("How many senior citizens are there?: "))
            kids = int(input("How many kids are there?: "))
            
            #handling negative amounts
            if adults < 0:
                print("please only enter positive whole values!")
                continue
            if kids < 0:
                print("please only enter positive whole values!")
                continue
            if senior_citizens < 0:
                print("please only enter positive whole values!")
                continue
        except:
            print("please enter in whole numbers only!")
            continue
        folks = adults + senior_citizens + kids
        if folks < people:
            print("Please check your math! the amount of people you entered",folks,"is less than your intial value of",people)
            continue
           
        elif folks > people:
            print("Please check your math! the amount of people entered:",folks,"is more than",people)
            continue
            
        elif folks == people:
            pass
    # if statement and for loop? to compare adults + senior_citizens + kids to people

""" Will need to figure out how to call this function conditionally: 
 something like if user input is EOD then print all that jazz
 This function will generate a report in a txt document and will be used to print out: 
 you sold this much to these people etc
 Will need to remember/research how to open document/ write to it/ then close it 
def EODreport():"""

def main():
   people =  howMany()
   demographicstracking(people)
main()
