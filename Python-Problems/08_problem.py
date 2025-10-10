'''
Consider the following:

A string,s , of length n where s = c2c1c3...cn-1.
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, ti , consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui  are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti , then do not include the character in string ui.
'''

def process_string_chunks(string, k):
    """
    Split string into chunks and remove duplicate characters from each chunk.
    
    Args:
        string: Input string to process
        k: Size of each chunk (must divide string length evenly)
    """
    string_length = len(string)
    num_chunks = string_length // k
    
    for chunk_index in range(num_chunks):
        # Extract substring of length k
        start_pos = chunk_index * k
        end_pos = start_pos + k
        substring = string[start_pos:end_pos]
        
        # Create result by removing duplicate characters
        result = ""
        seen_chars = set()
        
        for char in substring:
            if char not in seen_chars:
                result += char
                seen_chars.add(char)
        
        print(result)


# Example usage
input_string = "abacabad"
k = 4
process_string_chunks(input_string, k)