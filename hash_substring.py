# python3
# Maksims Jakuševs 221rdb376

def read_input():
    
    in_type = input()

    if "i" in in_type.lower():
        pattern = input()
        text = input()
    elif "f" in in_type.lower():
        file_name = '06'
        path = "tests/" + file_name
        with open(path, 'r') as file:
            pattern = file.readline()
            text = file.readline()

    
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    instance_indices = []
    pattern_length = len(pattern)
    pattern_hash = get_text_hash(pattern)
    
    for i in range(0, len(text)):
        if get_text_hash(text[i:i + pattern_length]) == pattern_hash:
            if text[i:i + pattern_length] == pattern:
                instance_indices.append(i)
    return instance_indices

def get_text_hash(text: str) -> int:
    multiplier = 23
    modulo = 137
    hash = 0
    for char in text:
        hash = (hash * multiplier + ord(char)) % modulo
    return hash


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))