def solution(number):
  container = []
  for each in range(number):
      if each % 3 == 0 or each % 5 == 0:
          container.append(each)
  return sum(container)