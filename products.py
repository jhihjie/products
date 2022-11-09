import os 

prodcuts = []
if os.path.isfile('prodcuts.csv'):
	print('yeah! 找到檔案了')
	with open('prodcuts.csv', 'r') as f:
		for line in f: # line 自行定義變數
			if '商品,價格' in line:
				continue # 繼續，跳到下一迴的意思
			name, price = line.strip().split(',')
			prodcuts.append([name, price])
		print(prodcuts)

else:
	print('找不到檔案…')



# 讀取檔案



# 讓使用者輸入
while True:
	name = input('請輸入商品名： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	price = int(price)
	# p = [name, price]
	prodcuts.append([name, price])
print(prodcuts)

# 印出所有購買記錄
for p in prodcuts:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('prodcuts.csv', 'w') as f:
		f.write('商品,價格\n')
		for p in prodcuts:
			f.write(p[0] + ',' + str(p[1]) + '\n')