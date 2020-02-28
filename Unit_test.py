import unittest

class Solution:

    def clockwise(self, matrix):

        # base case

        if len(matrix) == 0 or len(matrix[0]) == 0:

            return []

        # create the new matrix

        new_matrix = [[] for _ in range(len(matrix[0]))]

        row, col = len(matrix[0]), len(matrix)-1

        for i in range(0, row):

            for j in range(col, -1, -1):

               new_matrix[i].append(matrix[j][i])

        return new_matrix

class Unit_test(unittest.TestCase):

    def setUp(self):

        self.converter = Solution()

        # Create the test case

    def test_the_clockwise_result(self):

        # Assume
        converter = Solution()

        test_matrix1 = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [10, 11, 12],
                       [13, 14, 15]]

        result_matrix1 = [[13, 10, 7, 4, 1],
                         [14, 11, 8, 5, 2],
                         [15, 12, 9, 6, 3]]

        # Create a variable to accept the result
        # Action
        result = converter.clockwise(test_matrix1)

        # Assert
        # AssertEqual function to compare the actual result and expected result
        return self.assertEqual(result, result_matrix1)

# if __name__ == "__main__":
#
#     unittest.main()

#     matrix0 = []
#
#     matrix1 = [[1]]
#
#     matrix2 = [[1,2],
#                [3,4]]
#
#     matrix3 = [[1,2,3],
#                 [4,5,6],
#                 [7,8,9],
#                 [10,11,12],
#                 [13,14,15]]
# #
#     matrix4 = [[1,2,3,4,5],
#                [6,7,8,9,10],
#                [11,12,13,14,15]]
#
#     print(s.clockwise(matrix0))
#     print(s.clockwise(matrix1))
#     print(s.clockwise(matrix2))
#     print(s.clockwise(matrix3))
#     print(s.clockwise(matrix4))

class Solution_2:

    def remove_continuous(self, array):

        result = []

        first, second = 0, 1
        while first < len(array) and second < len(array):
            if array[first] != array[second]:
                result.append(array[first])
                first += 1
                second += 1

            else:
                first += 1
                second += 1

class Unit_test2(unittest.TestCase):

    # initialize the Class

    def setUp(self):
        self.converter = Solution_2()

    # Create the test case

    def test_case(self):
        converter = Solution_2()

        test_array = [1,2,2,1,3,3,3,2]

        correct_result = [2]

    # Create a variable to accept the result

        result = converter.remove_continuous(test_array)

    # AssertEqual function to compare the actual result and expected result

        return self.assertEqual(result, correct_result)

if __name__ == "__main__":

    unittest.main()
