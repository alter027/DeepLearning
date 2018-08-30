def recursive(n,a,b):
	if n == 0: return
	recursive(n-1,a,3-a-b)
	# A, B = chr(65+a), chr(65+b)
	print('from',A,"move to",B,'--',n,'th disk')
	recursive(n-1,3-a-b,b)

def non_recursive(n):
	lst = [['A','C','B'],['A','B','C']]
	m = 2**n - 1
	for i in range(1,m+1):
		tmp, cnt = 1, 0
		while not tmp&i: 
			tmp <<= 1
			cnt += 1
		tri = (i//(tmp*2)) % 3
		# print(i,tmp,tri)
		A, B = lst[(cnt^n+1)%2][tri], lst[(cnt^n+1)%2][(tri+1)%3]
		print('from',A,"move to",B,'--',cnt+1,'th disk')

def main():
	print('At first, all the disks are placed on rod A.')
	print('We have rod A, B, C')
	print('Our target is to move the entire stack to rod C.')
	n = int(input('How many disks are there? '))
	# print('------- recursive version-------')
	# recursive(n,0,2)
	# print('------- non-recursive version-------')
	non_recursive(n)

if __name__ == "__main__":
	main()