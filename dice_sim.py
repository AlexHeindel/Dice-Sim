import random


#Die class
class Die():

	def __init__(self):

		self.entries = []
		self.num_spread = [0,0,0,0,0,0]

	def roll(self):
		'''
		Gets a random die roll and adds it to die registry
		'''
		temp = random.randint(1,6)
		self.entries.append(temp)
		self.num_spread[temp-1] += 1

	def __str__(self):
		
		return str_list(self.entries)

	def __len__(self):

		return len(self.entries)

	def access_entry(self, index):
		'''
		accesses entry in die registry
		'''
		return self.entries[index]

	def access_spread(self):
		'''
		returns the list of the number of each value
		'''
		return self.num_spread


def get_num():
	'''
	Gets a positive number from user and error checks
	'''
	while True:
		try:
			result = int(input("\tInput positive integer: "))

		except:
			print("\tNot an integer, try again")

		else:
			if result <= 0:
				print("\tMust be a positive integer, try again")
			else:
				print("\tValid choice")
				return result
				break

def str_list(list):
	'''
	returns list as one line string
	'''
	temp = ""
	for item in list:
		temp += f"{item} "

	return temp


if __name__ == "__main__":

	num_range = "1 2 3 4 5 6"
	sum_range = "2 3 4 5 6 7 8 9 10 11 12"


	#Ask user for number of dice
	#Will just use two dice for now

	die1 = Die()
	die2 = Die()
	sums = []
	sums_spread = [0,0,0,0,0,0,0,0,0,0,0]

	#Ask for number of runs

	print("Choose how many trials to run")
	runs = get_num()

	#loop over all runs and get sums

	for num in range(0, runs):

		die1.roll()
		die2.roll()
		sums.append(die1.access_entry(num) + die2.access_entry(num))
		sums_spread[sums[num] - 2] += 1

	#output stuff

	#print(die1)
	#print(die2)

	#print("\nSums:\n" + str_list(sums))

	print("\nSums spread\n" + sum_range + "\n" + str_list(sums_spread))

	spread1 = die1.access_spread()
	print("\nSpread 1\n" + num_range + "\n" + str_list(spread1))
	spread2 = die2.access_spread()
	print("\nSpread 2\n" + num_range + "\n" + str_list(spread2))

	#Output csv file with columns (order, dice output, dice sum)

	file = open("data1.csv", 'w+')
	file.write(str_list(sums))
	file.close()
