class Person: 

    def __init__(self, name, address, phone):
        self.name = name
        self.add = address
        self.phone = phone
    
    def print_person(self):
        print('Customer name: ', self.name)
        print('Address: ', self.add)
        print('Phone: ', self.phone)
        print()
    
class Customer(Person):

    def __init__(self, name, address, phone, cust, mailing):

        Person.__init__(self, name, address, phone)

        self.cust = cust
        self.mailing = mailing

    def print_person(self):
        print('Customer Name: ', self.name)
        print('Address: ', self.add)
        print('Phone: ', self.phone)
        print('Customer ID: ', self.cust)
        if self.mailing == True:
            print('Member status: Active')
        else:
            print('Not a member')