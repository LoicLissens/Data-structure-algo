def to_camel_case(text):
    return ''.join(word.capitalize() if i else word for i, word in enumerate(text.replace('-', ' ').replace('_', ' ').split()))