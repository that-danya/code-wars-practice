def find_outlier(integers):
    counter = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            counter += 1
    if counter >= 2:
        for each in integers:
            if each % 2 != 0:
                return each
    else:
        for each in integers:
            if each % 2 == 0:
                return each