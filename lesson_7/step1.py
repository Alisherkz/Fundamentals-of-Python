class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list

    def __add__(self, other):
        return [[self.m_list[i][j] + other.m_list[i][j] for j in range(len(self.m_list))]
                for i in range(len(self.m_list))]

    def __str__(self):
        return "Matrix:\n" + "\n".join("\t".join(map(str, m_line)) for m_line in self.m_list)


ob1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(ob1)
ob2 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(ob2)
ob3 = Matrix(ob1 + ob2)
print(ob3)
