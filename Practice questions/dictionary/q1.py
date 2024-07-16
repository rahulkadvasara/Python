# country population

population = {
    'china':143,
    'india':136,
    'usa':32,
    'pakistan':21
}

def print_all():
    for k,v in population.items():
        print(f"{k}==>{v}")

def add():
    country = input("Enter country name: ")
    country = country.lower()
    if country in population:
        print(f"{country} is already exist in our dataset.")
        return
    p=float(input(f"Enter population for {country}: "))
    population[country]=p
    print_all()

def remove():
    country = input("Enter country name: ")
    country = country.lower()
    if country not in population:
        print(f"{country} does not exist in our dataset.")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name: ")
    country = country.lower()
    if country not in population:
        print(f"{country} does not exist in our dataset.")
        return
    print(f"{country} population is {population[country]}.")

def main():
    while True:
        op = input("Enter operation(add,remove,query,print or exit): ")
        op = op.lower()
        if op == 'print':
            print_all()
        elif op == 'add':
            add()
        elif op == 'remove':
            remove()
        elif op == 'query':
            query()
        elif op == 'exit':
            break
        else:
            print("Invalid input")

if __name__ == '__main__':
    main()
