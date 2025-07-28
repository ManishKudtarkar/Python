class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        # Create a mapping of character to their order index
        order_index = {char: index for index, char in enumerate(order)}
        
        # Separate characters from s into an ordered part and an extra part
        ordered_chars = []
        extra_chars = []
        
        for char in s:
            if char in order_index:
                ordered_chars.append(char)
            else:
                extra_chars.append(char)
        
        # Sort ordered chars based on their appearance in order
        ordered_chars.sort(key=lambda x: order_index[x])
        
        # Combine ordered characters with extra characters
        return ''.join(ordered_chars) + ''.join(extra_chars)
