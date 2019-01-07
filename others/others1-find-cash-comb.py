# -!- coding: utf-8 -!-

"""
《现金组合——多数之和》

给定n种现金，例如[1,2,5,10]，求用这些现金组合成的所有等于金额sum的组合
[1,1,1,1,1]
[1,2,1,1]
[1,2,2]
[5]
"""


def cash_comb(cash_valuess, target_value):
    """
    1. 排序所有现金额度，低到高
    2. 进入递归——找目标金额的组合=>固定一个金额得到剩余目标金额，继而再进入递归
    :param cash_valuess: [1,2,3,5]
    :param target_value: 10
    :return:
    """
    cash_valuess.sort()
    combs = find_comb(cash_valuess, target_value, 0)
    return combs


def find_comb(cash_values, target_value,last_cash_idx):
    """
    递归寻找符合target_value的组合：固定一个金额，得到剩余目标金额，用此金额进入递归
    :param cash_values:
    :param target_value:
    :param last_cash_idx:
    :return:
    """

    combs = []
    for i in range(last_cash_idx, len(cash_values)):  # 这里从last_cash_idx开始+有序使得结果总是从小至大排列结果是组合，而非排列
        cash_value = cash_values[i]
        left_value = target_value - cash_value
        if left_value < 0:  # 因为是排序过的，故可以快速终止
            break
        elif left_value == 0:  # 递归终止，无剩余的之
            combs.append([cash_value])
        else:  # 用剩余的金额进行递归
            sub_combs = find_comb(cash_values, left_value, i)
            for comb in sub_combs:  # 结果拼接至combs
                new_comb = [cash_value]
                new_comb.extend(comb)
                combs.append(new_comb)

    return combs


print(cash_comb([1, 2, 5, 10], 5))
print(cash_comb([1, 2, 3, 5, 10], 5))
print(cash_comb([1, 2, 3, 5, 10], 0))
print(cash_comb([1, 2, 3, 5, 10], 10))
print(cash_comb([1], 10))
print(cash_comb([1], 10))
