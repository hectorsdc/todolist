from item import *
import os


item_list = []
choice = 0

while choice != 4:
    print("\nWhat do you want to do?")
    print("1 - Add item")
    print("2 - Remove item")
    print("3 - Print all items")
    print("4 - Close")

    choice = int(input("\nEnter your choice: "))
    os.system('cls')
    
    match choice:
        case 1:
            print("")
            title = input("title: ")
            item = Item(title)
            item_list.append(item)
            x = input("do you want to write a description? y/n ")
            if(x == "y"):
                desc = input("description: ")
                item.desc = desc
                os.system('cls') 
            else:                                        
                os.system('cls')                    
        case 2:
            title = input("title of the item from the list you want to remove: ")
            for i in item_list:
                if(i.title == title):
                    item_list.remove(i)
            os.system('cls')
        case 3:
            print("")
            for i in item_list:                
                print(i)
            input("")
            os.system('cls')
        case 4:
            pass