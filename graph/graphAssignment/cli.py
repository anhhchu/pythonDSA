import argparse
import familytree 
from familytree import FamilyTree

family = familytree.main()
family



global args
def main(args=None):
    parser = argparse.ArgumentParser(prog='familytree', description='Command line interface for the family tree application')
    subparsers = parser.add_subparsers()
    args = None
    add_subcommand_add(args, subparsers)
    add_subcommand_edit(subparsers)
    add_subcommand_remove(subparsers)

    args = parser.parse_args(args)
    #print(args)
    args.func(args)

def add_subcommand_add(args, subparsers):
    parser_add = subparsers.add_parser('add', help='add a new family tree member')
    parser_add.add_argument('-i', '--id', required=True, help='family member\'s id')
    parser_add.add_argument('-n', '--name', required=True, help='family member\'s name')
    parser_add.add_argument('-g', '--gender', required=True, help='family member\'s gender')
    parser_add.add_argument('-a', '--age', required=True, help='family member\'s age')
    parser_add.set_defaults(func=add_family_member(args))

def add_subcommand_edit(subparsers):
    parser_edit = subparsers.add_parser('edit', help='edit an existing family tree member')
    parser_edit.add_argument('-i', '--id', required=True, help='family member\'s id')
    parser_edit.set_defaults(func=modify_family_member(args))

def add_subcommand_remove(subparsers):
    parser_remove = subparsers.add_parser('remove', help='remove a family member from the tree')
    parser_remove.add_argument('-n', '--name', required=True, help='name of family member')
    parser_remove.set_defaults(func=remove_family_member)


def add_family_member(args):
    #flag = input("Do you want to add relationship for this person? Y/N: ")
    #if flag == 'N': 
    FamilyTree.add_family_member(args.id, args.name, args.gender, args.age)
    
    else:
        print("Please enter a valid relationship this person has")
        print("*** Valid relationships: married, divorced, parent, offspring, adopted, sibling")
        relationship = input("Relationship: ")
        print("Please enter the id of the person that relationship is to")
        existing_person_id = input("id: ")
        FamilyTree.add_family_member(args.id, args.name, args.gender, args.age, existing_person_id, relationship)
    #return (relationship, relative_id)


def edit_family_member(args):
    print("Please select the attribute you wish to edit:")
    print("*** Valid attributes: name, gender, age, upate relationship, add relationship, remove relationship")
    attribute = input("Attribute: ")

def remove_family_member(args):
    print(args.name, " has been removed")

if __name__ == "__main__":
    main()
