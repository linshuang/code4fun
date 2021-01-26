from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # sort
        combinations = []
        self.combine(candidates, combinations, [], target)
        return combinations

    def combine(self, candidates, combinations, combination, target):
        if target < 0:
            return

        for i in range(len(candidates)):
            cand = candidates[i]
            if cand > target:  # 递归终止
                break

            if cand == target:
                comb2 = combination.copy()
                comb2.append(cand)
                combinations.append(comb2)
                pass
            else:
                comb3 = combination.copy()
                comb3.append(cand)
                self.combine(candidates[i:], combinations, comb3, target - cand)
                pass
        pass


sol = Solution()
rlt = sol.combinationSum([2,3,6,7], 7)
rlt = sol.combinationSum([2,3,5], 8)
rlt = sol.combinationSum([2,3,5], 3)
rlt = sol.combinationSum([2,3,5], 5)
rlt = sol.combinationSum([2,3,5], 11)
rlt = sol.combinationSum([2,3,5], 6)
print(rlt)

