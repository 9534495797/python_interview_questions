def find_dup_char(input):
    x = filter(lambda x: input.count(x) >= 2, input)
    print(' '.join(set(x)))
 
 
# Driver Code
if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)