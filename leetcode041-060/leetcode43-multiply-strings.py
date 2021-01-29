class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # 中间结果，一位乘，得到列表
        mid_rlt = []
        carrier = 0  # 进位
        for i in range(len(num1)-1, -1, -1):
            rlt_idx = len(num1) - i- 1
            mid_rlt.append([0 for k in range(rlt_idx)])
            for j in range(len(num2)-1, -1, -1):
                v = int(num1[i]) * int(num2[j]) + carrier
                v1 = v % 10
                carrier = int(v / 10)
                mid_rlt[rlt_idx].append(v1)
            if carrier!=0:
                mid_rlt[rlt_idx].append(carrier)
            carrier = 0

        # 中间结果(二维表)相加
        rlt = ""
        carrier = 0
        for j in range(len(num1)+ len(num2)+ 1):
            v = carrier
            for i in range(len(mid_rlt)):
                if j < len(mid_rlt[i]):
                    v += mid_rlt[i][j]
            rlt = str(v % 10) + rlt
            carrier = int(v/10)
        if carrier != 0:
            rlt = str(carrier) + rlt

        while rlt[0] == '0':
            rlt = rlt[1:]
        return rlt


sol = Solution()
val = sol.multiply("2", "3")
print(val)
val = sol.multiply("123", "456")
print(val)