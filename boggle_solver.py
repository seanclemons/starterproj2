'''
Sean Clemons
@03056571
'''
class Boggle:
  def __init__(self, grid, dictionary):
    #initialize grid, dictionary, and other attributes
    self.grid = [[char.upper() for char in row] for row in grid]
    self.dictionary = set(word.upper() for word in dictionary)
    self.prefixes = self.build_prefixes(self.dictionary)
    self.length = len(grid)
    self.solution = set()
    self.visited = [[False for i in range(self.length)] for i in range(self.length)]
    self.directions = [(-1,0) , (1,0) , (0,-1) , (0,1) , (-1,-1) , (-1,1) , (1,-1) , (1,1)]

  def build_prefixes(self, dictionary):
    #build a set of all possible prefixes from dictionary
    prefixes = set()
    for word in dictionary:
      word = word.upper()
      for i in range(len(word)):
        prefixes.add(word[:i+1])
    return prefixes

  def setGrid(self, grid):
    #set a new grid
    self.grid = [[char.upper() for char in row] for row in grid]
    self.length = len(grid)

  def setDictionary(self, dictionary):
    #Set new dictionary and rebuild prefixes
    self.dictionary = set(word.upper() for word in dictionary)
    self.prefixes = self.build_prefixes(self.dictionary)

  def isValid(self , word):
    #check if the word is in the dictionay and has 3+ letters
    return len(word) >= 3 and word in self.dictionary

  def isPrefix(self, prefix):
    #check if prefix is in the set of valid prefixes
    return prefix in self.prefixes

  def getSolution(self):
    #Get all valid words found in grid
    if self.length == 0 or len(self.grid[0]) == 0:
      return []

    for i in range(self.length):
      for j in range(self.length):
        self.dfs(i,j,'')

    return sorted(list(self.solution))

  def dfs(self, x, y, path):
    #depth first search to explore all possible words
    if not (0 <= x < self.length and 0 <= y < self.length) or self.visited[x][y]:
      return

    currentChar = self.grid[x][y]
    path += currentChar

    if not self.isPrefix(path):
      return
    
    self.visited[x][y] = True
    
    if self.isValid(path):
      self.solution.add(path)

    #explore all possible directions
    for dx , dy in self.directions:
      new_x , new_y = x + dx , y + dy
      self.dfs(new_x , new_y , path)
      
    #backtrack and mark the cell as unvisited 
    self.visited[x][y] = False

def main():
  grid = [['A', 'B', 'C', 'D'],
          ['E', 'F', 'G', 'H'], 
          ['I', 'J', 'K', 'L'], 
          ['A', 'B', 'C', 'D']]

  dictionary = ['ABEF', 'AFJIEB', 'DGKD', 'DGKA']

  mygame = Boggle(grid, dictionary)
  print(mygame.getSolution())

if __name__ == "__main__":
  main()
