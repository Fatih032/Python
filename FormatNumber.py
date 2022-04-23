# format number
# sayıları biçimlendiren python kodu
def format_number(number):
    return "{:,}".format(number)
print(format_number(1000000))