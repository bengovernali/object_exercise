
class Person: 
    def __init__(self, name, email, phone): 
     self.name = name 
     self.email = email 
     self.phone = phone 
     self.friends = []
     self.greeting_count = 0
     self.unique_greetings = []

    def greet(self, other_person): 
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person not in self.unique_greetings:
            self.unique_greetings.append(other_person)
        

    def print_contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        print(len(self.unique_greetings))

sonny  = Person('Sonny', 'sonny@hotmail.com', '495-586-3456')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
sally = Person('Sally', 'sally@gmail.com', '495-876-2314')
matt = Person('Matt', 'matt@yahoo.com', '495-665-4352')

#sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(matt)
jordan.greet(sally)
jordan.num_unique_people_greeted()
#sonny.print_contact_info()
#jordan.add_friend(sonny)
#jordan.num_friends()
#print(sonny.greeting_count)



#print(sonny.email, sonny.phone)
#print(jordan.email, jordan.phone)


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)

    