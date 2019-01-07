# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/restore-ip-addresses/description/
《复原IP地址》

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s):
        """
        使用递归：每次递归确定第n个地址段的所有可能，在第4个地址段结束递归
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.restore(s, 4, '', result)
        return result

    def restore(self, s, seg_no, cur_ip, ip_list):
        """
        递归主体
        :param s: 字符串
        :param seg_no: 当前ip片段的idx
        :param cur_ip: 当前ip，用于传递当前以及restore好的ip
        :param ip_list: 最终结果存放列表
        :return:
        """
        if seg_no == 1:  # 地址的第4段进行终止
            if int(s) > 255 or (s[0] == '0' and len(s) > 1):  # 大于255或者0开头的非0值
                return None
            else:  # 合法的第4段地址
                cur_ip += ('.' + s)  # 拼接处最终结果
                ip_list.append(cur_ip[1:])
                return s
        # 尝试确定当前段，确定之后以此进入递归确定下一段ip
        for i in range(0, len(s) - seg_no + 1):
            ip_seg = s[0:i + 1]
            if int(ip_seg) > 255 or (s[0] == '0' and i > 0):
                break
            self.restore(s[i + 1:], seg_no - 1, cur_ip + '.' + ip_seg, ip_list)
            if s[0] == '0':
                break


sol = Solution()
print(sol.restoreIpAddresses("25525511135"))
print(sol.restoreIpAddresses("0000"))
print(sol.restoreIpAddresses("01000"))
