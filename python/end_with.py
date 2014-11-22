'''
  print solution('abcde', 'cde')  #True
  print solution('abc','cd')      #False
'''


def solution(string, ending):
    return True if string[-len(ending):] == ending else False
