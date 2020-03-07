
class Matrix(object):
    def __init__(self, matrix_string):
        """Convert values from Str into int"""
        self.array_list = [[int(x) for x in line.split()]
                           for line in matrix_string.splitlines()]

    def row(self, index):
        return self.array_list[index-1]

    def column(self, index):
        return [x[index-1] for x in self.array_list]
