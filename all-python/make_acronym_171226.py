"""Acronym generator with str instances

This module has functions that change input sentence into acronym words.
Acronym is called '두문자어' in Korean and it's an abbreviated expression with first letter
of each word like

    'World Health Organization'   -->  'WHO'

This module supports several options for acronyms


Start Date: 2017/12/26
End Date  : 2017/12/26
"""


def generate_acronym(sentence, all_caps=True, ignore_words=[], glue=''):
    """Generate an acronym with given sentence

    :input:
        sentence: an str instance. MUST NEEDED.
        all_caps: Whether returned acronym is all capitalized. Defaults to True
        ignore_words: A sequence of str that's to be ignored in the returned string.
                      Defaults to None.
        glue: A seperator to concatenate first letters of words. Defaults to ''

    :return:
        A str instance.
    """
    words = sentence.split()

    # Maybe in a more readable way
    # answer = ''
    # if ignore_words:
        # words = [word for word in words if word not in ignore_words]
    # for word in words:
        # answer += word[0].upper() if all_caps else word[0]
    # return answer

    return glue.join(word[0].upper() if all_caps else word[0] for word in words
                     if word not in ignore_words)


print(generate_acronym('World Health organization', False))
print(generate_acronym('With us, the us', False, ['the']))
print(generate_acronym('With us, the us', False))
