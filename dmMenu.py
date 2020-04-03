
def dmMenu(toolArr):

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
                if len(toolArr[toolChoice-1]) == 3:
                    args = toolArr[toolChoice-1][2]
                    toolArr[toolChoice-1][0](*args)
                else:
                    toolArr[toolChoice-1][0]()
                print()
                #TODO Drop back to start properly
                input("Press 'Enter' to return to the menu.")
            except:
                print("Tool not found")