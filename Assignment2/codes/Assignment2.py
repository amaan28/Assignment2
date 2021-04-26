import random
n=500000
Toss_odd=0        #Number of experiments ended in odd number of tosses. 
for i in range(n) :
  C=1             #Variable that keeps account of the of the outcome of each toss. 0->HEADS and 1->tails.
  Toss=0          #Number of tosses in each experiment.
  while C!=0 :
    C=random.randint(0,1)
    Toss+=1
  if (Toss%2)!=0 :
    Toss_odd+=1
print(f"If Pr(E) is the probability that the experiment ends in odd number of tosses,then,\n\nSIMULATION\n\t Pr(E) = {Toss_odd/n}\nTHEORY\n\t Pr(E) = 0.666667")
