prodcuts = []
while True:
	name = input('請輸入商品名： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	# p = [name, price]
	prodcuts.append([name, price])
print(prodcuts)

for p in prodcuts:
	print(p[0], '的價格是', p[1])