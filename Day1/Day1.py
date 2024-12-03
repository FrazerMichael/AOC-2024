leftList = []
rightList = []

with open("Day1-Data.txt") as f:
    for line in f:
        left, right = line.split("  ")
        leftList.append(int(left))
        rightList.append(int(right))

def part1 (list1, list2):

    sortedLeftList = sorted(list1)
    sortedRightList = sorted(list2)

    temp = []

    for n in range(len(sortedLeftList)):
        
        temp.append(abs(sortedLeftList[n] - sortedRightList[n]))


    return sum(temp)


def part2 (list1, list2):

    temp = []

    for each in list1:
        counter = 0
        for n in list2:
            if each == n:
                counter += 1
        
        temp.append(each * counter)
    
    return sum(temp)


print(part1(leftList, rightList))
print(part2(leftList, rightList))

