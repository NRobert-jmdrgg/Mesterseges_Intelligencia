

import math

def minimax(index, currDepth, isMax, scores, maxDepth):
  if currDepth == maxDepth:
    return scores[index]
  if isMax:
    return max(
      minimax(index * 2, currDepth + 1, not isMax, scores, maxDepth),
      minimax(index * 2 + 1, currDepth + 1, not isMax, scores, maxDepth)
    )
  else:
    return min(
      minimax(index * 2, currDepth + 1, not isMax, scores, maxDepth),
      minimax(index * 2 + 1, currDepth + 1, not isMax, scores, maxDepth)
    )

def main():
  scores = [5, 2, 33, 3, 6 ,9, 8, 33]
  d = math.log(len(scores), 2)
  print(minimax(0, 0, True, scores, d))

if __name__ == '__main__':
  main()