def is_palyndrome(word):
    if word == word[::-1]:
        print(f'The word -  {word} - is palyndrom!')
    else:
        print(f'The word -  {word} - is not palyndrom!')

is_palyndrome('казак')