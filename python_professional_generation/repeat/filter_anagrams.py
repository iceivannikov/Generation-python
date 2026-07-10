def filter_anagrams(word, words):
    result = []
    target = sorted(word)
    for wrd in words:
        if sorted(wrd) == target:
            result.append(wrd)
    return result

if __name__ == "__main__":
    print(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
    print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort','mortmortmortmort', 'remortvolremort']))
    print(filter_anagrams('стекло', []))