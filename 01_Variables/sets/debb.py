#DEBUGGING EXCERCISES:
# Daniel and Florentino

myfamily = {
   "child1": {
       "name": "Emil",
       "year": 2004
   },
   "child2": {
       "name": "Tobias",
       "year": 2007
   }
}
# the problem was the loop was not used correctly lack of item method
for child, info in myfamily.items(): # loop through the dictionary
   print(child)
   for key, value in info.items(): # loop through the inner dictionary
       print("\t" + key + ":", value)
# the problem was the update method was not used correctly 
myfamily["child3"] = {"name": "Linus", "year": 2011} # update the inner dictionary
#myfamily["child3"].update({"name": "Linus", "year": 2011}) # update the inner dictionary



