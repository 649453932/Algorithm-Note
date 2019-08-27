class Solution(object):
    '''
    滑动窗口
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    输入: "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    '''

    def lengthOfLongestSubstring1(self, s):
        #维护一个队列
        res = 0
        que = []
        for i in range(len(s)):
            if s[i] not in que:
                que.append(s[i])
            else:
                if len(que) > res:
                    res = len(que)
                que = que[que.index(s[i]) + 1:]
                que.append(s[i])
        return max(res, len(que))

    def lengthOfLongestSubstring2(self, s):
        # 维护的是set，查询时间复杂度为O(1)
        res = 0
        que = set()
        index = 0
        for i in range(len(s)):
            if s[i] not in que:
                que.add(s[i])
            else:
                if len(que) > res:
                    res = len(que)
                while s[i] in que:
                    que.remove(s[index])
                    index += 1
                que.add(s[i])
        return max(res, len(que))
