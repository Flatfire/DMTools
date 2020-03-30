
def dmMenu(toolArr):
    #TODO Make the menu accept parameters as well as functions
    """
    Pass an array of functions, of the format:
        toolArr = [(function, str:description)]
        Function tuples can be added by appending to the array.
    """
    while True:
        print("List of tools:")
        for i in range(len(toolArr)):
            print("{}. {}".format(i+1, toolArr[i][1]))
        print()
        toolChoice = input("Please choose a tool number or type '?' for help: ")
        if toolChoice == '?':
            helpChoice = int(input("Select a tool number you'd like to know about: "))
            try:
                print()
                print(toolArr[helpChoice-1][1])
                print(toolArr[helpChoice-1][0].__doc__)
                input("Press 'Enter' to return to the menu.")
                for i in range():
                    print()
            except:
                print("Tool not found")
        else:
            print()
            try:
                toolChoice = int(toolChoice)
                toolArr[toolChoice-1][0]()
                print()
                input("Press 'Enter' to return to the menu.")
            except:
                print("Tool not found")