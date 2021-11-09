class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.marker = False
        k = 0
        for i in range(len(matrix)):
            if len(self.matrix[0]) == len(self.matrix[i]):
                k += 1
        if k == len(self.matrix):
            self.marker = True
        else:
            print("matrix is incorrect")

    def trans(self):
        if self.marker:
            n = len(self.matrix)
            m = len(self.matrix[0])
            for i in range(m):
                for j in range(n):
                    print(self.matrix[j][i], end = ' ')
                print()


matrix1 = Matrix([[0, 1, 2], [4, 2, 6], [7, 3, 9], [0, 2, 1]])
matrix1.trans()
