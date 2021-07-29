def table(num):
	range=int(input("Enter range of table: "))
	while range>=1:
		print(num,"*",range," = ",num*range)
		range=range-1
def main():
	table(5,12)
if __name__=="__main__":
	main()
