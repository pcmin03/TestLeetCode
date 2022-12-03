class Solution:
    def frequencySort(self, s: str) -> str:
        list_s = list(s) 
        if len(list_s) == 1: 
            return s
        
        from collections import Counter
        list_s.sort()
        count_s = Counter(list_s)
        count_s=sorted(count_s.items(), key=lambda pair: pair[1], reverse=True)
        singl_word,multi_word = [], []
        
        for k,val in count_s: 
            if val == 1:
                singl_word.append(k)
            else:
                multi_word.append(k*val)
        result = multi_word+singl_word
        result = ''.join(result)
        return result 
            