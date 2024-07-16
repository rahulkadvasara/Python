# stock price
import statistics
stock_price = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_all():
    for k,v in stock_price.items():
        avg = statistics.mean(v)
        print(f"{k}==>{v}==>avg: {round(avg,2)}")

def add():
    s = input("Enter stock name: ")
    p = float(input(f'Enter price for {s}: '))
    if s in stock_price:
        stock_price[s].append(p)
    else:
        stock_price[s]=[p]
    print_all()

def main():
    while True:
        op = input("Enter operation(add, print,exit): ")
        op = op.lower()
        match op:
            case 'add':
                add()
            case 'print':
                print_all()
            case 'exit':
                break
            case _:
                print("Invalid input")
        

if __name__ == '__main__':
    main()