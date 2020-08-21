'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if not "th" in word:
        return 0;
    else:
        return 1 + count_th(word[word.index("th") + 2: len(word)]);