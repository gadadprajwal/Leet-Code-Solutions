class Solution:
    def findWords(self, words):
        
        # Create Sets with characters for each level of keyboard.
        level1 = {'q','w','e','r','t', 'y', 'u', 'i', 'o', 'p'}
        level2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        level3 = {'z','x','c', 'v', 'b' , 'n', 'm'}
        
        #To return
        ans = []
        
        #Check if each given word is the subset of sets we have defined for each level by using 'issubset' function.
        for word in words:
            low = set(word.lower())
            if low.issubset(level1) or low.issubset(level2) or low.issubset(level3):
                ans.append(word)
        return ans     
                    
        """
        :type words: List[str]
        :rtype: List[str]
        """
