import pandas as pd
nfa = {}
n = int(input("No. of states : ")) #Enter total no. of states
t = int(input("No. of transitions : ")) #Enter total no. of transitions/paths
for i in range(n):
  state = input("state name : ") #Enter state name eg: A, B, C, q1, q2 ..etc
  nfa[state] = {} #Creating a nested dictionary
  for j in range(t):
    path = input("path : ") #Enter path eg : a or b in {a,b} 0 or 1 in {0,1}
    print("Enter end state from state {} travelling through path {} : ".format(state,path))
    reaching_state = [x for x in input().split()] #Enter all the end states that
    nfa[state][path] = reaching_state #Assigning the end states to the paths in dictionary

print("\nNFA :- \n")
print(nfa) #Printing NFA
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]

new_states_list = [] #holds all the new states created in dfa
dfa = {} #dfa dictionary/table or the output structure we needed
keys_list = list(list(nfa.keys())[0])
#conatins all the states in nfa plus the states created in dfa are also appended further
path_list = list(nfa[keys_list[0]].keys()) #list of all the paths eg: [a,b] or [0,1]
###################################################

dfa[keys_list[0]] = {} #creating a nested dictionary in dfa

for y in range(t):
  var = "".join(nfa[keys_list[0]][path_list[y]])
#creating a single string from all the elements of the list which is a new state
  dfa[keys_list[0]][path_list[y]] = var #assigning the state in DFA table
  if var not in keys_list: #if the state is newly created
   new_states_list.append(var) #then append it to the new_states_list
   keys_list.append(var) #as well as to the keys_list which contains all the


##################################################
# Computing the other rows of

while len(new_states_list) != 0: #consition is true only if the new_states_list is
    dfa[new_states_list[0]] = {}
#taking the first element of the new_states_list and examining it
    for _ in range(len(new_states_list[0])):
      for i in range(len(path_list)):
        temp = [] #creating a temporay list
        for j in range(len(new_states_list[0])):
          
          temp += nfa[new_states_list[0][j]][path_list[i]] 
        s = ""
        s = s.join(temp)
#creating a single string(new state) from all the elements of the list
        if s not in keys_list: #if the state is newly created
         new_states_list.append(s) #then append it to the new_states_list
         keys_list.append(s)
#as well as to the keys_list which contains all the states
        dfa[new_states_list[0]][path_list[i]] = s #assigning the new state in the DFA table
    new_states_list.remove(new_states_list[0])

print("\nDFA :- \n")
print(dfa) #Printing the DFA created
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
  for i in x:
    if i in nfa_final_state:
     dfa_final_states.append(x)
     break
print("\nFinal states of the DFA are : ",dfa_final_states) #Printing 
#Removing the first element in the new_states_list
