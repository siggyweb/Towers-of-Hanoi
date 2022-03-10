from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


#Set up the Game
num_discs = int(input("\nHow many disks do you want to play with?\n"))

while num_discs < 3:
  num_discs = int(input("Enter a number greater than or equal to 3\n"))
for i in range(num_discs,0,-1):
  left_stack.push(i)

#Use game theory to calculate perfect run for the game under these conditions.
num_optimal_moves = (2 ** num_discs) - 1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

#Get User Input
def get_input():
  choices = []
  for stack in stacks:
    name = stack.name
    choices.append(name[0].upper())
  while True:
    for i in range(0,len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter,name))
    user_input = input("").upper()
    if user_input in choices:
      for i in range(0,len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
    
#Play the Game

num_user_moves = 0
while right_stack.get_size() != num_discs:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.get_size == None:
      print("\n\nInvalid Move. Try Again")
    elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}.".format(num_user_moves,num_optimal_moves))


    
