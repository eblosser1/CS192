class Member:
    name = ""
    number = 0
    jersey = 0
2
    def __init__(self, name, number, jersey):
        self.name = name
        self.number = number
        self.jersey = jersey

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def set_jersey(self, jersey):
        self.jersey = jersey

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_jersey(self):
        return self.jersey

    def display_data(self):
        print("")
        print("Member information: ")
        print("------------------------")
        print("Name:", self.name)
        print("Phone Number:", self.number)
        print("Jersey Number:", self.jersey)


def menu():
    print("===========Main Menu===========")
    print("1. Display Team Roster.")
    print("2. Add Member.")
    print("3. Remove Member.")
    print("4. Edit Member.")
    print("9. Exit Program.")
    return int(input("Selection> "))


def team_list(members):
    if len(members) == 0:
        print("No current members in memory.")
    else:
        for x in members.keys():
            members[x].display_data()


def add_member(members):
    new_name = input("Enter member name to be added: ")
    new_number = int(input("Phone number: "))
    new_jersey = int(input("Jersey number: "))
    members[new_name] = Member(new_name, new_number, new_jersey)
    return members


def remove_member(members):
    del_name = input("Enter member name to be removed: ")
    if del_name in members:
        del members[del_name]
    else:
        print("Member not found in list.")
    return members


def edit_member(members):
    old_name = input("Enter the name of the member you want to edit: ")
    if old_name in members:
        new_name = input("Enter the new name of the member: ")
        new_number = int(input("Enter member's new phone number: "))
        new_jersey = int(input("Enter member's new jersey number: "))
        members[new_name] = Member(new_name, new_number, new_jersey)
        del members[old_name]
    else:
        print("Member not found in list.")
    return members


print("Welcome to the Team Manager")
members = {}
menu_selection = menu()
while menu_selection != 9:
    if menu_selection == 1:
        team_list(members)
    elif menu_selection == 2:
        members = add_member(members)
    elif menu_selection == 3:
        members = remove_member(members)
    elif menu_selection == 4:
        members = edit_member(members)
    menu_selection = menu()
print("Exiting Program...")


