import unittest
import sys

sys.path.append("/home/codio/workspace/") #have to tell the unittest the PATH to find boggle_solver.py and the Boggle Class

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

  # ADD 4x4, 5x5, 6x6, 7x7...13x13, and LARGER Dictionaries
  def test_Normal_case_3x3(self):
    grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
    dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abc", "abdhi"];
    expected = [x.upper() for x in expected]
    self.assertEqual(expected.sort(), solution.sort())

  def test_4x4(self):
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"], ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "pry", "quart", "tar", "tarp", "ten", "wet"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
        
    expected = ["art", "ego", "gent", "get", "net", "new", "newt", "pry", "quart", "tar", "tarp", "ten", "wet"]
    expected = [word.upper() for word in expected]
        
    self.maxDiff = None
    self.assertCountEqual(solution, expected)

  def test_5x5(self):
    grid = [["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O"],
            ["P", "Qu", "R", "S", "T"],
            ["U", "V", "W", "X", "Y"]]

    dictionary = ["abc", "afkpu", "bglqu", "mno", "cde"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()

    expected = ["abc", "afkpu", "bglqu", "mno", "cde"]
    expected = [word.upper() for word in expected]

    self.maxDiff = None
    self.assertCountEqual(solution, expected)
  

class TestSuite_Simple_Edge_Cases(unittest.TestCase):
  #ADD MANY SIMPLE TEST CASES
  def test_Word_That_Take_The_Entire_Grid(self):
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["M", "N", "O", "P"]
    ]
    dictionary = ["ABCDEFGHIJKLM", "AEIM", "AFK", "BCDG", "FGHI", "OPMLKJIHG", "CDEFGHIJKL"]

    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    expected = ["ABCDEFGHIJKLM", "AEIM", "AFK", "BCDG", "FGHI", "OPMLKJIHG", "CDEFGHIJKL"]
    expected = [word.upper() for word in expected]

    self.maxDiff = None
    self.assertEqual(expected.sort(), solution.sort())


  def test_SquareGrid_case_1x1(self):
    grid = [["A"]];
    dictionary = ["a", "b", "c"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    self.assertEqual(expected.sort(), solution.sort())

  def test_EmptyGrid_case_0x0(self):
    grid = [[]];
    dictionary = ["hello", "there", "general", "kenobi"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    self.assertEqual(expected.sort(), solution.sort())

  def test_allSameLetters(self):
    grid = [["A","A"],["A","A"]]
    dictionary = ["a" , "aa", "aaa", "aaaa"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    expected = ["AA", "AAA", "AAAA"]
    self.assertEqual(expected.sort(), solution.sort())

class TestSuite_Complete_Coverage(unittest.TestCase):
  def test_ColpexGrid_4x4(self):
    grid = [
      ["T", "W", "Y", "R"],
      ["E", "N", "P", "H"],
      ["G", "Z", "Qu", "R"],
      ["O", "N", "T", "A"]
    ]
    dictionary = ["art", "ego", "gent" , "get", "new", "quart", "tarp", "ten", "wet"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    expected = ["ART", "EGO", "GENT", "GET", "NEW", "QUART", "TARP", "TEN", "WET"]
    self.assertEqual(expected.sort(), solution.sort())
  
  def test_LargeGrid(self):
        grid = [
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
            ["U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"],
            ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N"],
            ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"],
            ["Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"],
            ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"],
            ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]
        ]
        dictionary = ["abcdefg", "mnopqrst", "qrstuv", "vwxyz", "abcfghij", "klmnopqrst"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABCDEFG", "MNOPQRST", "QRSTUV", "VWXYZ", "ABCFGHIJ", "KLMNOPQRST"]
        self.assertEqual(expected.sort(), solution.sort())

class TestSuite_Qu_and_St(unittest.TestCase):
  def test_QuWords(self):
    grid = [["Q", "U", "A"], ["I","N","T"],["E", "R", "S"]]
    dictionary = ["quaint", "quiet", "quarts", "quest"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    expected = ["QUAINT", "QUIET", "QUARTS", "QUEST"]
    self.assertEqual(expected.sort(), solution.sort())

if __name__ == '__main__':
	unittest.main()
