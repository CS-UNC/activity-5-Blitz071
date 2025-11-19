def more_than_20(file):
    long_words = []
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) > 20:
                    long_words.append(word)
    return long_words

def has_no_e(word):
    return 'e' not in word.lower()

def uses_only(word, available_letters):
    for char in word.lower():
        if char not in available_letters.lower():
            return False
    return True

def all_uses_only(file, available_letters):
    result = []
    
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if uses_only(word, available_letters):
                    result.append(word)
    
    return result
