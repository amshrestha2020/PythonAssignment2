'Write a function that takes camel-cased strings(ie ThisIsCamelCased)'
'And Converts them to snake case(ie this_is_camel_cased)'
'Modify the function by adding an argument, separator, so it will also convert to the kebab case(ie this-is-camel-case) as well'

def converter(text, separator = "_"):
    new_text = []
    for index, letter in enumerate(text):
        if letter.isupper():
            if not index == 0:
                new_text.append(separator)
            new_text.append(letter.lower())
        else:
            new_text.append(letter)
    return "".join(new_text)

name = "ThisIsCamelCased"

snake_case = converter(name)
kebab_case = converter(name, "-")

print("camel-cased strings :", name)
print("snake-cased strings :", snake_case)
print("kebab-cased strings :", kebab_case)