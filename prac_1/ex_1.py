def sum(list, i = 0, res = 0):
    if i < len(list):
        return sum(list, i + 1, res + list[i])
    else:
        return res
if __name__ == '__main__':
    print(sum([1, 2, 3, 4, 5, 6]))