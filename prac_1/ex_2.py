def alpha_counter_max(list, id=0, dict=None):
    if dict == None:
        dict = {}
    if id < len(list):
        if list[id][0] not in dict.keys():
            dict[list[id][0]] = len(list[id])
        elif dict.get(list[id][0]) < len(list[id]):
                dict[list[id][0]] = len(list[id])
        alpha_counter_max(list, id+1, dict)
    return dict

if __name__ == '__main__':
    list = ["aaaaaaa", "bbb", "b", "b", "aaa", "ccccccccc", "aaaaaa", "qqqqqqqqqqqqqqqqq", "q"]
    print(alpha_counter_max(list))