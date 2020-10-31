# -*- coding: utf-8 -*-

from random import *
import math

##################################################################################################
def main():
    print("Welcome")
    initializer = True
    while (initializer == True):
        choice = menuScreen()
        if (choice == "enter"):
            #overwrite the previous list
            teamNames = enterTeamNames()
        elif (choice == "create"):
            #read and copy names to an array
            teamsList = readNamesFromTextFile()
            #find class size by checking length of the teamsList array
            classSize = findClassSize(teamsList)
            #just randomize the names n times, where n is size of class
            teamsList = randomizeNames(teamsList,classSize)
            #find out how big the user wants the groups to be
            groupSize = findGroupSize()
            #generate combinations without repeat with a simple .append and pop
            combinations = generateCombinations(classSize,groupSize,teamsList)
            #ask user how many groups they want and touch up the groups to the specifications
            #still in progress
            #combinations = askNumberOfGroups(combinations,groupSize)
            #print the combinations
            #needs to be modefied if top function gets implimented
            initializer = printTeamGroups(combinations,groupSize,initializer)
        elif (choice == "delete"):
            #read and copy names to an array
            teamsList = readNamesFromTextFile()
            #print all the names for display
            printNames(teamsList)
            #delete the name from the array
            teamsList = deleteNames(teamsList)
            #overwrite the text file
            overwriteTextFile(teamsList)
        elif (choice == "print"):
            #read and copy names to an array
            teamsList = readNamesFromTextFile()
            #simply print the names from list
            printNames(teamsList)
        elif (choice == "add"):
            #read and copy names to an array
            teamsList = readNamesFromTextFile()
            #append the name to the list of teams
            teamsList = addNames(teamsList)
            #overwrite the text file
            overwriteTextFile(teamsList)
        elif (choice == "help"):
            #display help
            initilizer = displayHelp(initializer)
        elif (choice == "quit"):
            #stop the loop
            initializer = False      
##################################################################################################
def menuScreen():
    print("Please select one of the folowing:\n")
    print("Enter:  Enter team names(s)        Add:    Add a team name(s)")
    print("Print:  Print name(s) from list       Delete: Delete team name(s)")
    print("Create: Create random groups          Help: Display help screen")
    print("Quit:   Quit \n")
    
    choice = input("Choice: ")
    choice = choice.lower()
    
    while (choice != 'enter' and choice != 'create' and choice != 'delete' and choice != 'print'
           and choice != 'quit' and choice != 'add'and choice != 'help'):
        print("Invalid Coice\n")
        print("Enter:  Enter team names(s)        Add:    Add a team name(s)")
        print("Print:  Print name(s) from list       Delete: Delete team name(s)")
        print("Create: Create random groups          Help: Display help screen")
        print("Quit:   Quit\n")
        
        choice = input("Choice: ")
        choice.lower()
    return choice
##################################################################################################
def displayHelp(initilizer):
    print('Type full words')
    print("Capitolization does not matter\n")
    
    pause = input('Press any key to continue or type "Quit" to quit ')
    print("")
    
    if (pause.lower() == "Quit"):
        initializer = False
##################################################################################################
def enterTeamNames():
    #automatically create a new text file named teamNames.txt in the folder
    #where this file is located as WRITE ONLY
    file = open("teamNames.txt","w")

    #create empty list
    teams = []

    print("Enter 0 to quit\n")
    #variable to store input in
    name = input("Enter Name: ")
    
    while (name != '0'):
        #append the list with an added name
        teams.append(name)
        name = input("Enter Name: ")

    length = len(teams)
    index = 0
    
    while (index < length):
        teamName = teams[index]
        file.write(teamName+' \n')
        index += 1

    #close the opened file
    file.close()

    return teams
##################################################################################################
def readNamesFromTextFile():
    teamsList = []
    index = 0

    with open ('teamNames.txt','r') as file:
        for line in file:
            line = line.strip()
            teamsList.append(line)

    #close the opened file
    file.close()

    return teamsList
##################################################################################################
def printNames(teamsList):
    size = len(teamsList)
    
    print("There are: ", size, "team(s) in your class")
    teamsList.sort()
    
    for i in range (0,size):
        print(teamsList[i])
    
    print("")
##################################################################################################
def overwriteTextFile(teamsList):
    file = open("teamNames.txt","w")

    size = len(teamsList)
    
    for index in range (0,size):
        teamName = teamsList[index]
        file.write(teamName+' \n')

    file.close()
##################################################################################################
def addNames(teamsList):
    print ("Enter 0 to quit\n")
    name = input("Add name: ")
    
    while (name!='0'):
        teamsList.append(name)
        
        name = input("Add name: ")
        
    return teamsList
##################################################################################################
def deleteNames(teamsList):
    print ("Enter 0 to quit")
    if (len(teamsList) == 0):
        print('Oops, there are no names in your list...')
        print('Going back to main menu')
        name = "0"
    else:
        name = input("Delete name: ")
    
    while (name!='0'):
        if name in teamsList:
            teamsList.remove(name)

            print(name,"Deleted\n")
            name = input("Delete name: ")
        elif (len(teamsList) == 0):
            print('Oops, there are no names in your list...')
            print('Going back to main menu')
            name = "0"
        else:
            print("Name not found!")
            name = input("Delete name: ")
        
    return teamsList
##################################################################################################
def findClassSize(teamsList):
    classSize = len(teamsList)
    
    return classSize
##################################################################################################
def findGroupSize():
    groupSize = eval(input("How big are the groups? : "))

    return groupSize
##################################################################################################
def randomizeNames(teamsList,classSize):
    i = classSize-1
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        teamsList[j], teamsList[i] = teamsList[i], teamsList[j]
    return teamsList
##################################################################################################
def generateCombinations(classSize,groupSize,teamsList):
    i = classSize-1
    #rearange the names baised on how big the class is
    for k in range (0,classSize):
        while i > 1:
            i = i - 1
            j = randrange(i)  # 0 <= j <= i-1
            teamsList[j], teamsList[i] = teamsList[i], teamsList[j]

    #counter for comparing to group size
    counter = 0
    #index of individual groups
    groupIndex = 0
    #new list of lists to store groups in
    combinations = []
    combinations.append([])
    
    #keep checking the size of the teams list because first name is always popped
    while (len(teamsList) != 0):
        team = teamsList[0]
        
        individualGroup = combinations[groupIndex]
        individualGroup.append(team)
        counter += 1
        #name is now in a new variable so pop it
        teamsList.pop(0)
        if counter == groupSize and len(teamsList) != 0:
            counter = 0
            combinations.append([])
            groupIndex += 1

            
    return combinations
##################################################################################################
def askNumberOfGroups(combinations,groupSize):
    print("There are",len(combinations),"possible")
    groupsWanted = eval(input("How many groups do you want?: "))
    repeat = True
    while (repeat == True):
        
        if (groupsWanted < len(combinations)):
            print("Do you want me to try rearanging groups?")
            answer = input('The groups will be uneven: ')
            if (answer.lower() == 'yes'):
                combinations = rearangeGroups(combinations,groupsWanted,groupSize)
            else:
                repeat = False
        elif (groupsWanted < len(combinations)):
            print("Do you want me to try rearanging groups?")
            answer = input('The groups will be uneven: ')
            if (answer.lower() == 'yes'):
                combinations = rearangeGroups(combinations,groupsWanted,groupSize)
            else:
                repeat = False
        else:
            repeat = False
            
    return combinations
##################################################################################################
def rearangeGroups(combinations,groupsWanted,groupSize):
    numberOfGroups = len(combinations)
    
    while (len(combinations)<groupsWanted):
        combinations.append([])
        for i in range (0,groupSize):
            print("")
            
##################################################################################################
def printTeamGroups(combinations,groupSize,initializer):
    print(combinations)
    numberOfGroups = len(combinations)
    
    for x in range (0,numberOfGroups):
        group = combinations[x]
        print ("\nGroup: #",(x+1))
        groupSize = len(group)
        
        for y in range (0,groupSize):
            print(group[y])
            
    pause = input('Press any key to continue or type "Quit" to quit ')
    print("")
    
    if (pause.lower() == "Quit"):
        initializer = False
    return initializer
##################################################################################################
main()