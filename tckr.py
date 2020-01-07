def ticker(text, width, tick):
    end_char = tick % (width + len(text))
    part_text = text[max(0, end_char - width):end_char]
    return " " * (width - end_char) + part_text + " " * (end_char - len(text))

print(ticker("Hello there", 6, 16))

# "      " -> 0
# "     H" -> 1
# "    He" -> 2
# "   Hel" -> 3
# "  Hell" -> 4
# " Hello" -> 5
# "Hello " -> 6
# "ello t" -> 7
# "llo th" -> 8
# "lo the" -> 9
# "o ther" -> 10
# " there" -> 11
# "there " -> 12
# "here  " -> 13
# "ere   " -> 14
# "re    " -> 15
# "e     " -> 16
# "      " -> 17 -> 0
# "     H" -> 18 -> 1

#
