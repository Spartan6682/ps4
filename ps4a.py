# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #Create a function that will iterate through the available sequence and return a list of possible permutations:
    def get_permutations(sequence):
        permutations = []
        # Define the base case.
        if len(sequence) == 1:
            permutations.append(sequence)
            return permutations
        else:
            # Define the recursive case
            permutations = get_permutations(sequence[1:])
            return_permutations = []
            # generate permutations from the returned value
            for permutation in permutations:
                permutation_list = [x for x in permutation]
                for integer in range(len(sequence)):
                    temp_list = permutation_list[:]
                    temp_list.insert(integer, sequence[0])
                    return_string = ''.join(temp_list)
                    return_permutations.append(return_string)
            return return_permutations
    
    return(get_permutations(sequence))


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations(input('Please enter a string to evaluate for permutations: ')))