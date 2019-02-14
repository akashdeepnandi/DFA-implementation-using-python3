# Program starts
states = []
statesT = []
symbols = []
s1 = " S \t"
fst = []
choice = 'n'
st =''
while choice=='n' or choice=='N':
    
    print("**************Welcome to DFA program implementation**************\n")
    print("****************Important Note****************\n")
    print("\n**Please be careful with the inputs, as the output of the program depends highly on input\n\n**Please read carefully before giving the input\n")

    n1 = int(input("No. of states: ")) 

    print("\nEnter states: \n")
    for x in range(n1):
        st = input("State "+ str(x+1) +": ")
        states.append(st)
        statesT.append([st])
        print()

    ist = input("Initial state: ") 
    n3 = int(input("\nNumber of final states: "))
    if n3 == 1:
        fst = input("\nFinal State: ")
    else:
        for x in range(n3):
            fst.append(input("\nFinal state "+str(x+1)+": "))

    n2 = int(input("\nNo. input symbols: "))
    print("\nEnter symbols: \n")
    for x in range(n2):
        symbols.append(input("Symbol "+ str(x+1) + ": "))
        print()


    print("Constructiong DFA: ---> \n")

    for x in range(n1):
        for y in range(n2):
            statesT[x].append(input("For symbol '" + symbols[y] + "' state '"+ statesT[x][0] + "' goes to: "))
            print()

    print("DFA Matrix: \n")
    # displaying the matrix
    for x in symbols:
        s1 += " "+x+" \t"

    print(s1 + "\t [S stands for state]")

    print("---\t"+"---\t"*len(symbols))

    for x in statesT:
        s2 = ""
        for y in x:
            s2 += " "+y+" \t"
        print(s2)

    print("\nInitial State: "+ist)
    print("\nFinal States: "+(", ".join(fst)))

    print("\n\n#### Congratulations! If you see the table matches your DFA then,\nyour DFA is constructed properly\n\nIf it does not restart the program and input correct inputs\n")
    choice = input("#### Do you want to proceed or restart? y = proceed | n = restart : ")


print("\nNow let us evaluate a input string using symbols : -- [" + (", ".join(symbols)) +"] given as input before!!!\n\nTo see if the input string belongs to the constructed languange\n")

while choice=='y' or choice=='Y' :
    string = input("Input string: ")

    # Final state search
    cst = ist
    for i in string:
        insy = symbols.index(i) + 1
        inst = states.index(cst)
        cst = statesT[inst][insy]


    print("\n\n\n###################### OUTPUT ########################\n\n")

    if cst in fst:
        print("#### String belongs to the languange defined ####\n\n")
    else:
        print("#### String does not belong to the languange defined ####\n\n")
    choice = input("Do you want test another string or exit? y = yes | e = exit: ")
    print("\n")

print("Existing Program.....")