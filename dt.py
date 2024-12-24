import datetime  as tt

letter = """Dear <|Name|>,
You are selected!
<|Date|>"""
b = input("enter your name ")
dd = tt.date()
a = letter.replace("<|Name|>" , b ).replace( "<|Date|>" , dd)
print(b)