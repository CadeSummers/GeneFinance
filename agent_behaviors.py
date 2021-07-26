#imports 
from random import randint

#list of (20 or so) types of investor behaviors, to serve as keys to a dict which contains values simulating the method of the investors execution on data
behaviors = {
    "Young", #Takes on more risk than Elder
    "Elder", #Takes on less risk overall
    "Risky", #Takes on the most risk
    "Risk-Averse", #Takes on very least risk
    "Median", #Takes middle route between all agents with random factors pushing either way slightly. This behavior can be representative of control investors along with mean.
    "Mean", #Takes average route between all agents with random factors pushing eitehr way slightly.
    "Conformist", #Takes whatever action the majority / largest section of the market is doing
    "Contrarian", #Takes whatever action the minority / smallest section of the market is doing
    "Adversarial", #More extreme contrarian, does the respective "opposite" of whatever the most of the market is doing
    "Random", #Behavior is completely randomized
    "Martingale", #Continually executes the martingale strategy
    "Short-hold", #Buy low, sell high, akin to daytraders
    "Long-hold", #Buy high, sell higher, akin to position traders
    "Swing", #Medium hold price, takes advantage of market volatility
    "Scalping", #Prefer quiet, liquid markets
    "Self-Destructive", #Trades when the shouldn't, virtually tries to maximize losses, more of a test case than real case
    "Single Stock", #singular investments
    "Aggregate", #diverse investments
    "Pairs", #invests in similar investments which correlate with each other, all of which correlates with each other closely   
    "Value" #executes basic value investment strategy
}

print(len(behaviors))