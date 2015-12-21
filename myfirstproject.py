x=raw_input("hey , What's your Name?\n")
print "It's good to see you",x
y=int(input(" Please enter your age\n"))
if y>=18:
  print "you are a adult ",x,"now you are responsible for your decisions"
elif y>=0 or y<=17:
  print "you are a teen ",x
else:
  print "please enter a valid age"


