import unittest

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_cases(self):
        self.assertEqual(self.solution.characterReplacement("ABAB", 2), 4)
        self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)
        
    def test_more_cases(self):
        self.assertEqual(self.solution.characterReplacement("AAAAA", 2), 5)
        self.assertEqual(self.solution.characterReplacement("ABBBB", 2), 5)
        self.assertEqual(self.solution.characterReplacement("ABCD", 0), 1)
        self.assertEqual(self.solution.characterReplacement("ABCDABCD", 3), 8)
        
    def test_edge_cases(self):
        self.assertEqual(self.solution.characterReplacement("", 0), 0)
        self.assertEqual(self.solution.characterReplacement("A", 0), 1)
        self.assertEqual(self.solution.characterReplacement("A", 1), 1)
        self.assertEqual(self.solution.characterReplacement("A", 2), 1)
        self.assertEqual(self.solution.characterReplacement("AA", 0), 2)
        self.assertEqual(self.solution.characterReplacement("AA", 1), 2)
        self.assertEqual(self.solution.characterReplacement("AA", 2), 2)
        self.assertEqual(self.solution.characterReplacement("AAA", 0), 3)
        self.assertEqual(self.solution.characterReplacement("AAA", 1), 3)
        self.assertEqual(self.solution.characterReplacement("AAA", 2), 3)
        self.assertEqual(self.solution.characterReplacement("AAA", 3), 3)
        
if __name__ == '__main__':
    unittest.main()