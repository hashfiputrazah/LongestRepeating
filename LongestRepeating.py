class Solution(object):
    def characterReplacement(self, s, k):
        """
        Given a string s and an integer k, return the length of the longest substring containing the same letter you can get
        after performing at most k character replacements.

        :param s: a string of uppercase English letters
        :param k: an integer representing the maximum number of character replacements allowed
        :return: an integer representing the length of the longest substring containing the same letter after
                 performing at most k character replacements
        """

        # initialize variables
        max_length = 0
        left = 0
        char_count = {}

        # iterate through the string
        for right in range(len(s)):
            # add current character to dictionary and update count
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # find the character with the highest count
            max_char_count = max(char_count.values())

            # calculate the number of characters that need to be replaced
            replace_count = (right - left + 1) - max_char_count

            # if we need to replace more characters than allowed, move left pointer forward and update dictionary
            while replace_count > k:
                char_count[s[left]] -= 1
                left += 1
                replace_count = (right - left + 1) - max(char_count.values())

            # update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length


# example cases
solution = Solution()
print(solution.characterReplacement("ABAB", 2))
print(solution.characterReplacement("AABABBA", 1))

# more cases
print(solution.characterReplacement("AAAAA", 2))
print(solution.characterReplacement("ABBBB", 2))
print(solution.characterReplacement("ABCD", 0))
print(solution.characterReplacement("ABCDABCD", 3))