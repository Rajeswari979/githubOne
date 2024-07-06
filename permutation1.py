def get_permutations (string, i = 0):

    if i == len(string):
        print("".join(string))
    for j in range(i, len(string)):
        words=[c for c in string]
        words[i], words[j] = words[j], words[i]
        print("eaxmple",words[i],words[j])
        get_permutations (words, i + 1)

get_permutations("raj")