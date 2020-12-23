import pickle
class Person:
    def __init__(self, id, name, gender, age=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.rels = {} # dict of relationship of this person to others. Eg: 001.rels =  {1: [002], 2:[003]}
        self.weight_map = {1:'married', -1:'divorced', 0:'parent', 2:'offspring', -2:'adopted', 3:'sibling'} 

    def update_rel(self, weight, other_id):
        if weight not in self.rels: 
            self.rels[weight] = [other_id]
        else:
            self.rels[weight].append(other_id)

    def del_rel(self, weight, other_id):
        if weight in self.rels:
            if len(self.rels[weight]) > 1:
                self.rels[weight].remove(other_id)
            else:
                self.rels.pop(weight,'None')

    def has_rel(self, other_id):
        relationship = None
        for k, v in self.rels.items(): 
            #print(k,v)
            if other_id in v:
                relationship = self.weight_map[k]
                break
        
        return relationship

    @property
    def direct_relatives(self): # get the list of direct relatives of one person
        relatives = []
        if 0 in self.rels: # parents
            relatives += self.rels[0] 
        if 2 in self.rels: # offsprings
            relatives += self.rels[2] 
        if 3 in self.rels: # siblings
            relatives += self.rels[3] 
        return relatives

    def __repr__(self):
        rels = {}
        for weight in self.rels: 
            rel = self.weight_map[weight]
            rels[rel] = self.rels[weight]
        return "{id}, {name}, {gender}, {age}, {rels}".format(id=self.id, name=self.name, gender=self.gender, age=self.age, rels=rels)

class Graph:
    def __init__(self):
        self.rel_map = {'married': 1, 'divorced': -1, 'parent': 0, 'offspring':2, 'adopted': -2, 'sibling': 3} 
        self.persons = {} # {001: Person(001), 002: Person(002)} a dict of id mapped to Person object
        #self.edges = Relationship()
    
    def _map_relationship(self, relationship):
        weight = self.rel_map[relationship]
        # if relationship = parent, reciprocal relationship is offspring
        if weight == 0: weight2 = self.rel_map['offspring'] 
        # if relationship = offspring or adopted, reciprocal relationship is parent
        elif weight == 2 or weight == -2: weight2 = self.rel_map['parent'] 
        else: weight2 = weight
        return (weight, weight2)


    def add_person(self, id, name, gender, age=None):
        if id not in self.persons:
            self.persons[id] = Person(id, name, gender, age) 
  
    def add_relationship(self, new_person_id, existing_person_id, relationship):
        '''
        new_person: id of the newly-added person
        existing_person: id of the existing person
        relationship: relationship of new_person to existing_person
        
        output examples:
            002, 001, 'married': new_person is married to existing person 002,
            003, 001, 'offspring': new person is offspring of the existing person 001
        
        self.persons = {001: Person(001), 002: Person(002), 003: Person(003)}
        '''

        # new_person have just been added to self.persons, check whether existing person is already there
      
        new_person = self.persons[new_person_id]
        existing_person = self.persons[existing_person_id]

        # Add relationship to each Person object 
        weight, weight2 = self._map_relationship(relationship)

        existing_person.update_rel(weight, new_person_id)
        new_person.update_rel(weight2, existing_person_id)

        # if relationship is offspring or adopted, add offspring relationship to the other parent and sibling relationship to other siblings 
        
        if weight == 2 or weight == -2: 
            partner_id, children_id = None, []
            if 1 in existing_person.rels: partner_id = existing_person.rels[1][0] # access the id of the partner
            elif -1 in existing_person.rels: partner_id = existing_person.rels[-1][0]
            
            if 2 in existing_person.rels: children_id += existing_person.rels[2]
            if -2 in existing_person.rels: children_id += existing_person.rels[-2]
            
            if partner_id: 
                partner  = self.persons[partner_id] # access partner object
                partner.update_rel(weight, new_person_id) # add new offspring to partner object
                new_person.update_rel(0, partner_id) # add parent to offspring

            for child_id in children_id: 
                if child_id != new_person_id:
                    child = self.persons[child_id] # access individual child object
                    child.update_rel(3, new_person_id)  # add new sibling to all other chidren
                    new_person.update_rel(3, child_id) # add siblings to new person

 
    def remove_person(self, id):
        person = self.persons[id]
        # remove relationships
        # e.g. if remove 003 rels = {0:[001,002], 3:[004]}, have to remove 003 in weight 2 or weight -2 of 001 and 002, and in weight 3 of 004
        for weight in person.rels:
            for rel_id in person.rels[weight]:
                relative = self.persons[rel_id]
                # remove person id in relative's relationships 
                if weight == 0 and (2 in relative.rels or -2 in relative.rels): 
                    relative.del_rel(2,id)
                    relative.del_rel(-2,id)
                elif weight == 2 or weight == -2:
                    relative.del_rel(0,id)
                else:
                    relative.del_rel(weight, id)

        #remove all relationships of the person from the family, but keep the person in Tree
        person.rels.clear()


    def delete_relationship(self, id, relative_id):
        '''
        remove relationship between person id and relative_id 
        relationship is pertaining to id

        e.g. remove 'offspring' 003 from 001: delete_relationship(001, 003, 'offspring')
        weight = 2 (offspring)
        remove 003 from weight 2 of 001.rels
        remove 001 from weight 0 of 003.rels

        output: 003.rels = {0:{002}, 3:{004}}, 001.rels = {1:{002}, 2:{004}}
        '''
        
        person = self.persons[id]
        relative = self.persons[relative_id]
        #print(person.name, relative.name)

        relationship = person.has_rel(relative_id)
        if relationship is None:
            msg = "No relationship exists between {person} and {relative}".format(person=person.name, relative=relative.name)
            return msg
        else:
            weight = self.rel_map[relationship]
            if weight == 0 and (2 in relative.rels or -2 in relative.rels): 
                relative.del_rel(2,id)
                relative.del_rel(-2,id)
            elif weight == 2 or weight == -2:
                relative.del_rel(0,id)
            else:
                relative.del_rel(weight, id)

            person.del_rel(weight,relative_id)
            msg = '{rel} relationship removed between {person} and {relative}'.format(rel=relationship,person=person.name, relative=relative.name)
            return msg

class FamilyTree(Graph): 
    
    def __init__(self):
        super().__init__()

    def _add_relationship(self, id, existing_person_id, relationship):
        '''
        This method has assertions pertaining to Family Tree class and not Graph class
        '''
        person = self.persons[id]
        try: 
            assert existing_person_id in self.persons, "Person {id} not yet in family, add the person to proceed".format(id=existing_person_id)
            existing_person = self.persons[existing_person_id] 
        except AssertionError as msg:
            return msg
        
        rel = person.has_rel(existing_person_id)
        if rel is not None: 
            msg = '{rel} relationship already exists between {person} and {existing_person}'.format(person=person.name, rel=rel, existing_person=existing_person.name)
            return msg
        
        else:
            if relationship == 'married':
                try:
                    assert existing_person_id != id, "{person} cannot marry to self".format(person=person.name)
                    assert id not in existing_person.direct_relatives, "{person} cannot marry to direct relative {existing_person}".format(person=person.name, existing_person=existing_person.name)
                    assert id not in person.direct_relatives, "{existing_person} cannot marry to direct relative {person}".format(person=person.name, existing_person=existing_person.name)
                    assert 1 not in existing_person.rels, "{existing_person} is already married".format(existing_person=existing_person.name)
                    assert 1 not in person.rels, "{person} is already married".format(person=person.name)
                    assert person.gender != existing_person.gender, "Same sex marriage not allowed btw {person} and {existing_person}".format(person=person.name, existing_person=existing_person.name)
                    self.add_relationship(id, existing_person_id, relationship)

                except AssertionError as msg:
                    return msg

            else: 
                self.add_relationship(id, existing_person_id, relationship)
            
            msg = "{person} is {relationship} to {existing_person}".format(person=person.name, relationship=relationship, existing_person=existing_person.name)
            return msg

    def add_family_member(self, id, name, gender, age=None, existing_person_id=None, relationship=None):
        """
        Add family member information (id, name, gender, age) and relationship to exising person, if applicable
        
        Assertions for valid relationships:
        - married to self
        - married between siblings/parents/offsprings
        - married to multiple persons 
        - same-sex marriage, probably not allowed in 18th century England
        """
        self.add_person(id, name, gender, age)
        print("* add {name} to family *".format(name=name))

        if existing_person_id:
            msg = self._add_relationship(id, existing_person_id, relationship)
            print(msg)
            
  
    def remove_family_member(self, id):
        person = self.persons[id]
        self.remove_person(id)
        print('{id} {person} removed'.format(id=person.id, person=person.name))

    def modify_family_member(self, attribute, id, value=None, relative_id=None):
        
        person = self.persons[id]
        msg = "{value} updated for {person}".format(value=value, person=person.name)
        if attribute == 'name':
            person.name = value
        elif attribute == 'gender':
            person.gender = value
        elif attribute == 'age':
            person.age = value
        elif attribute == 'delete relationship': 
            msg = self.delete_relationship(id,relative_id)
        elif attribute == 'update relationship':
            #assert relative_id, "Provide relative_id and old relationship to proceed"
            # remove relationship, then add new relationship
            
            msg = self.delete_relationship(id, relative_id)
            msg = self._add_relationship(id, relative_id, value)

        elif attribute == "add relationship":
            #assert relative_id, "Provide relative_id to proceed"
            #relative = self.persons[relative_id]
            msg = self._add_relationship(id, relative_id, value)
            #print("{person} is {value} to {relative}".format(person=person.name, value=value, relative=relative.name))

        return msg


 
    def __repr__(self):
        persons = "\nFAMILY TREE OF WUTHERING HEIGHTS EXTENDED FAMILY\n"
        for id in self.persons:
            persons += "{person}\n".format(person = self.persons[id].__repr__())
        return persons


def save_WH_family():
    family = FamilyTree()
    
    family.add_family_member('001', 'Patrick Earnshaw', 'M',None)
    family.add_family_member('002', 'Hannah Earnshaw', 'F', None, '001', 'married')
    family.add_family_member('003', 'Catherine Earnshaw', 'F', None, '001', 'offspring')
    family.add_family_member('004', 'Hindley Earnshaw', 'M', None, '001', 'offspring')
    family.add_family_member('005', 'Andrew Linton', 'M', None)
    family.add_family_member('006', 'Dolores Linton', 'F', None, '005', 'divorced')
    family.add_family_member('007', 'Isabella Linton', 'F', None, '005', 'offspring')
    family.add_family_member('008', 'Edgar Linton', 'M', None, '005', 'offspring')
    family.add_family_member('009', 'Heathcliff Linton', 'M', None, '005', 'adopted')
    family.modify_family_member('add relationship','009', 'adopted', '005')
    family.add_family_member('010', 'Frances Byler', 'F', None, '004', 'married')
    family.add_family_member('011', 'Hareton Earnshaw', 'M', None, '004', 'adopted')
    family.modify_family_member('add relationship','003', 'married', '008')
    family.add_family_member('012', 'Cathy Linton', 'F', None, '003', 'offspring')
    family.add_family_member('013', 'Linton Heathcliff', 'M', None, '007', 'offspring')
    family.modify_family_member('add relationship','013', 'offspring', '009')
    family.modify_family_member('add relationship','012', 'married', '011')
    family.modify_family_member('add relationship','012', 'divorced', '013')

    #print(family.modify_family_member('update relationship','013', 'parent', '012'))
    #print(family.modify_family_member('update relationship','002', 'offspring', '001')) # update from married to divorced for Cathy
    #family.modify_family_member('update relationship','012', 'married', '013') # update from married to divorced for Cathy
    
    # Check the family information
    print (family)

    # save the family information to file
    
    afile = open(r'WHfamily.pkl', 'wb')
    pickle.dump(family, afile)
    afile.close()
    return family
    
#save_WH_family()


def main():
    # Load the saved Family Tree from file, if file doesn't exist, call the function to create family
    try: 
        file = open(r'WHfamily.pkl', 'rb')
        family = pickle.load(file)
        file.close()
        print("Fetch Family from file")
        print(family)
    except Exception:
        family = save_WH_family()

    # CLI interface
    run = input("Make changes to Family Tree? y/n: ")
    action = 'quit'
    if run == 'y':
        action = input("Enter *add|edit|remove to modify person, or *print to print tree, or *quit to stop: ")

    while action!="quit":     
        if action == 'add': 
            print("** Enter person's info separated by '-' ")
            id, name, gender, age = input("enter id-name-gender-age: ").split("-")
            while id in family.persons:
                print("id already exists")
                id, name, gender, age = input("enter id-name-gender-age: ").split("-")

            flag = input("Do you want to add relationship for this person? y/n: ")
            if flag == 'n': 
                family.add_family_member(id, name, gender, age)   
            else:
                print("Please enter a valid relationship this person has")
                print("*** Valid relationships: married, divorced, parent, offspring, adopted, sibling")
                relationship = input("Relationship: ")
                existing_person_id = input("Please enter the id of the person that relationship is to: ")
                family.add_family_member(id, name, gender, age, existing_person_id, relationship)

        elif action == 'edit':
            id = input("Please enter a person id you wish to edit: ")
            while id not in family.persons:
                print("Person {id} not yet in family, add the person to proceed".format(id=id))
                id = input("Please enter a person id you wish to edit: ")

            print("Please select the attribute you wish to edit:")
            print("*** Valid attributes: name, gender, age, update (relationship), add (relationship), delete (relationship)")
            attribute = input("Attribute: ")

            if attribute == "add" or attribute == "update":
                attribute += " relationship"

                relative_id = input("Please enter the id of the relative to modify relationship: ")
                print("*** Enter Valid relationships: married, divorced, parent, offspring, adopted, sibling")
                value = input("Relationship: ")
                
                while value not in family.rel_map:
                    print("Relationship entered is not valid")
                    value = input("Reenter *relationship: ")
                    msg = family.modify_family_member(attribute, id, value, relative_id)

                msg = family.modify_family_member(attribute, id, value, relative_id)

            elif attribute == "delete":
                attribute += " relationship"
                relative_id = input("Please enter the id of the relative to delete relationship: ")
                msg = family.modify_family_member(attribute,id,None,relative_id)

            elif attribute == 'name' or attribute == 'gender' or attribute == 'age':
                # update other attributes
                value = input("Enter new value for person: ")
                msg = family.modify_family_member(attribute, id, value)
            
            else:
                msg = 'Invalid Choice!'
            print(msg)

        elif action == 'remove':
            id = input("Please enter a person id to remove: ")
            if id not in family.persons:
                print("Person {id} id not in family".format(id=id))
                id = input("Please enter a person id to remove: ")
            family.remove_family_member(id)
            
        elif action == 'print':
            print(family)

    
        else:
            print("Invalid Choice!")

        action = input("Enter *add|edit|remove to modify person, or *print to print tree, or *quit to stop: ")

    print("** UPDATED FAMILY")
    print(family)

    print("** Save family to file")
    afile = open(r'WHfamily.pkl', 'wb')
    pickle.dump(family, afile)
    afile.close()

if __name__ == "__main__":
    main()
