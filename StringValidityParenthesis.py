'Write a Python class to find validity of a string of Parenthesis (,),{,},[ and ].'
'These brackets must be close in the correct order'
'For example () and ()[]{} are valid but [), ({[)] and {{{ are invalid.'


class Python:
    def f(str):
        a = ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str
s = input("enter : ")
print(s, "-", "is valid"
      if Python.f(s) else "is invalid")
