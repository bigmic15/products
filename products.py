# To read the products.csv
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'Name,Price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# User input 
while True:
	name = input('Please enter a product name: ')
	if name == 'quit':
		break
	price = input('Please enter its price: ')
	price = int(price)
	products.append([name, price])
print(products)	

# To print all the records
for p in products:
	print(p[0], 'is $', p[1])

# To write the products.csv file
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Name,Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')