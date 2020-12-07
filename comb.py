#__author__ = "Ashlyn Hanks"
#__copyright__ = "Copyright 2020"
#__credits__ = []
#__license__ = "GPLv3"
#__version__ = "0.0.0"
#__maintainer__ = "Ashlyn Hanks"
#__email__ = "ahanks@highpoint.edu"
#__status__ = "Development"

print("Welcome, today we will be playing with combinations and permutations.\n")
order = input("Does order matter? If yes please type 1, if no please type 2:\n")
order = int(order)
if order == 1:
    print("You have decided that order matters, thus we will be performing a permutation")
    data = input("Please enter a string of numbers to be permutated:\n")
   
    from itertools import permutations 
    l = list(permutations(data)) 
    print(l)     

if order == 2:
    print("You have decided that order does not matter, thus we will be performing a combination")
    data2 = input("Please enter a string of numbers to be combined:\n")
    
    from itertools import combinations 
    n = len(data2)
    m = list(combinations(data2, n))
    print(m)