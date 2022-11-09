prodcuts = []
while True:
	name = input('請輸入商品名： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	price = int(price)
	# p = [name, price]
	prodcuts.append([name, price])
print(prodcuts)

for p in prodcuts:
	print(p[0], '的價格是', p[1])

	with open('prodcuts.csv', 'w') as f:
		f.write('商品,價格\n')
		for p in prodcuts:
			f.write(p[0] + ',' + str(p[1]) + '\n')