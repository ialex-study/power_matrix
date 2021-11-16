def compose(matrix1, matrix2):
	res = [[0 for i in matrix1] for j in matrix1]
	trans_matrix = list(zip(*matrix2))
	for i in range(len(matrix1)):
		for j in range(len(matrix1)):
			res[i][j] = sum(map(lambda x: x[0] * x[1], zip(matrix1[i], trans_matrix[j])))
	return res

def get_result(matrix, power):
	res = [[i for i in j] for j in matrix]
	for i in range(power - 1):
		res = compose(res, matrix)
	return res

if __name__ == "__main__":
	print("Hello")
	size = int(input("Size--> "))
	matrix = [[0 for i in range(size)] for j in range(size)]
	for i in range(size):
		matrix[i] = list(map(int, input(f"{i + 1} line--> ").split()))

	power = int(input("Power--> "))
	for i in get_result(matrix, power):
		print(i)
