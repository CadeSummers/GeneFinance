#File to initialize an "Agent" which simulates an investor in a market, choosing random factors and choosing to commit or withdraw
from random import randint

#TODO from some module import list of factors, factors likely dicts
#temporary "mock list" to illustrate how this would work
mock_list = ["Factor 1", "Factor 2", "Factor 3", "Factor 4", "Factor 5"]

#define class "Agent"
class Agent:

    #initialization of count (to keep track of ids)
    count = 0

    def __init__(self):

        #initialize list of focus factors, used in get_factors() method
        self.focus_factors = []

        #initialize agent behavior
        self.behavior = "Random"

        #Creation of id
        self.id = id(self)

    #define representation of class
    def __repr__(self):

        return "Instance of an Agent class with ID: " + str(self.id)

    #return when printed other than a memory address
    def __str__(self):

        #returns statement with relevant information
        statement = "ID: " + str(self.id) + "\nBehavior: " + str(self.behavior) + "\nFocus Factors: " + str(self.focus_factors)

        return statement


    #grabs a given number (in this mock case: 3) factors which our agent will choose to focus on
    def get_factors(self):

        #list of random numbers to serve as indices of list we will select from
        nums = [randint(0, len(mock_list) - 1), randint(0, len(mock_list) - 1), randint(0, len(mock_list)) - 1]

        #initial list for factors this agent will focus on
        focus_factors = []

        #for each index (num) in nums we will append the associated factor
        for num in nums:
            focus_factors.append(mock_list[num])

        return focus_factors


        

agent = Agent()

for i in range(10):
    print("Iteration :", i)
    temp_agent = agent
    print(temp_agent.get_factors())
