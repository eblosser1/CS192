print("Welcome to the Team Manager")


def menu():
    print("===========Main Menu===========")
    print("1. Display Team Roster.")
    print("2. Add Member.")
    print("3. Remove Member.")
    print("4. Edit Member.")
    print("9. Exit Program.")


members = {}
menu_item = 0
while menu_item != 9:
    menu()
    menu_item = int(input("Selection> "))


class Member:
    name = ""
    number = 0
    jersey = 0

    def __init__(self, name, number, jersey):
        self.__name = name
        self.__number = number
        self.__jersey = jersey

    def setname(self, name):
        self.name = name

    def setnumber(self, number):
        self.number = number

    def setjersey(self, jersey):
        self.jersey = jersey

    def getname(self):
        return self.name

    def getnumber(self):
        return self.number

    def getjersey(self):
        return self.jersey

    def displayData(self):
        




def team_list():
    current = 0
    if len(member_list) > 0:
        while current < len(member_list):
            print(member_list[current])
            current = current + 1
    else:
        print("List is empty")


def add_member():
    name = input("Enter new member's name: ")
    member_list.append(name)


def remove_member():
    del_name = input("Enter member name to be removed: ")
    if del_name in member_list:
        item_number = member_list.index(del_name)
        del member_list[item_number]
    else:
        print(del_name, "was not found")


def edit_member():
    old_name = input("Enter the name of the member you want to edit: ")
    if old_name in member_list:
        item_number = member_list.index(old_name)
        new_name = input("Enter the new name of the member: ")
        member_list[item_number] = new_name
    else:
        print(old_name, "was not found")


menu_item = 0
member_list = []
while menu_item != 9:
    menu()
    menu_item = int(input("Selection> "))
    if menu_item == 1:
        team_list()
    elif menu_item == 2:
        add_member()
    elif menu_item == 3:
        remove_member()
    elif menu_item == 4:
        edit_member()
    elif menu_item == 9:
        print("Exiting Program...")
        break

