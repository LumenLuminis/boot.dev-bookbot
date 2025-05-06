def count_words(text):
    return len(text.split())

def character_counts(text):
    input = text.lower()
    chars = {}
    for char in input:
        if char not in chars:
            chars[char]=0
        try:
            chars[char]+=1
        except:
            pass
    return dict(sorted(chars.items(), key=lambda item: item[1],reverse=True))

def sort_dict(text: str):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            chars[char] = chars.get(char,0) + 1
    list_of_tuples = chars.items()
    sorted_list = list(list_of_tuples) #.sort(reverse = True, key = lambda item: item[1])
    sorted_list.sort(reverse=True, key=lambda item:item[1])
    return sorted_list

def pretty_print(path, text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    counts = sort_dict(text)
    for tuples in counts:
        print(str(tuples[0])+": "+ str(tuples[1]))
    print("============= END ===============")
