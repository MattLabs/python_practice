"""
Problem: 
	1) Print "hello, I'm a joke-maker, what's your name?" to the screen

	2) Take input from the keyboard, until enter is pressed.

	3) Print "Hello" + name + ".  Here is your customized list of jokes:"

	4) Read file: joke1.txt in, and put that text into a data structure.

	5) Replace the word "NAME" with the name the user entered in that data structure.  - hard part - ask if you need help.

	6) Print out the joke to the screen.

	7) Loop through more than one text file to read each one in, and print each one to the screen, replacing each instance of "NAME" with the users name.

	8) Make all of the individual components of this into functions that call one another.

Target Users: Me, Rich
Target System:GNU/ LINUX
Interface: Command Line
Functional Requirements:Print out a message
						Take input from keyboard
						Read in file (joke1.txt)
						Replace word with user entered word
						print to screen
						Make functions that call each other
Testing: Simple run test
"""

#1 print "hello, I'm a joke-maker, what's your name?"
print ("hello, I'm a joke-maker, what's your name?")

#2 Take input from keyboard until enter is pressed [save as "NAME"]
name = raw_input("Press Enter to continue: " + '\n')

#3  Print "Hello" + name + ". Here is your list of customized Jokes: " 
print ('\n')
print ("Hello " + name + ". Here is your list of customized jokes: " + '\n')

#4 Read File: joke1.txt in, and put that text into a data structure
"""joke1 = open(r'joke1.txt', "r")
j = joke1.read()
print (j)"""

#for line in open('joke1.txt'):
#    print(line + '\n')
#    break
    
"""joke1 = 'joke1.txt'
with open(joke1) as f:
	data = f.readlines()
	print(data)"""

"""f = open( "joke1.txt", "r" )
a = []
for line in f:
    a.append(line)"""
    

#5 Replace the word "NAME" with the name the user entered in that data structure
#6 print out the joke to the screen
#print(line + '\n')



#7 Loop through more than one text file to read each one in and print each one to the screen replacing each instance of "NAME" with the users name
"""print ("Here is another joke " + name + ":" )
f = open( "joke2.txt", "r" )
a = []
for line in f:
    a.append(line)
    print(line + '\n') """ 

"""
print ("Here is another joke " + name + ":" )
f = open( "joke3.txt", "r" )
a = []
for line in f:
    a.append(line)
    print(line + '\n')"""

i = 1
while i < 4:
    filename = r'./joke%d.txt' % i
    with open(filename, 'r') as f:
        print('Here is another joke: ' + name)
        print(f.read() + '\n')
    i = i +1

print ("No more jokes!")

#8 Make all the individual components of this into functions that call one another
