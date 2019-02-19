import os

# To read a file
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'Name,Price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# User input 
def user_input(products):
    while True:
        name = input('Please enter a product name: ')
        if name == 'quit':
            break
        price = input('Please enter its price: ')
        price = int(price)
        products.append([name, price])
    print(products)    
    return products

# To print all the records
def print_products(products):
    for p in products:
        print(p[0], 'is $', p[1])

# To write a file
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('Name,Price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # To check for existence of the file
        products = read_file(filename)
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()