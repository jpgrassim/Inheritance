import personclass as pc

def main():

    person = pc.Person('Jorge', 'paso 100', '11111')

    customer = pc.Customer('Pedro', 'Paz 10', '22222', 132, True)

    customer1 = pc.Customer('Jose', 'Urquiza 200', '33333', 144, False)
    show_person_info(person)
    show_person_info(customer)
    show_person_info(customer1)

def show_person_info(individual):
    individual.print_person()
    print()

    
main()







