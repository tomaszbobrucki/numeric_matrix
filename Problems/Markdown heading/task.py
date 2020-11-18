def heading(phrase, quant=1):
    if quant <= 1:
        return "#" + " " + phrase
    elif 6 > quant > 1:
        return "#" * quant + " " + phrase
    else:
        return "#" * 6 + " " + phrase


# print(heading("A", 10))
