class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        distance_word = {i:num for num,i in enumerate(list(keyboard))}    
        word_list = list(word)
        total_step = 0
        if len(word_list) == 0 : 
            return 0 
        elif len(word_list) == 1: 
            return distance_word[word_list[0]]
        else: 
            first_step = distance_word[word_list[0]]
            total_step += first_step
            
        for i in word_list[1:]:
            next_step = distance_word[i]
            total_step += abs((first_step - next_step))
            first_step = next_step

        return total_step

            

        


