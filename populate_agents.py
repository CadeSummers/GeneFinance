#import class agent
from agent import Agent
from sys import exit

#function which returns populated agents
def populate(population_size):
    

    #validity check
    if population_size < 1:

        print("Turns out size DOES matter...")
        print("Please input a valid size")
        exit()

    #create list of population size with an agent in each
    agents = [Agent() for i in range(population_size)]
    
    return agents

agents = populate(10)

for agent in agents:
    print(agent)
    

