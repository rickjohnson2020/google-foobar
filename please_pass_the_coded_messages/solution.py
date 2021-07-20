from itertools import permutations


def solution(L):
    
    lst = list()
    
    for i in range(len(L)):
        i = i + 1
        all_possible_nums = permutations(L, i)
        for tup in all_possible_nums:
            mapped_list = list(map(str, tup))
            combined_str = ''.join(mapped_list)
            combined_int = int(combined_str)

            if combined_int % 3 == 0:
                lst.append(combined_int)
            else:
                pass

    if not lst:
        return 0

    else:
        max_num = 0
        for num in lst:
            if num > max_num:
                max_num = num

        return max_num
