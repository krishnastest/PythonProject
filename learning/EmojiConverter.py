message = input("> ")


def emoji_converter():
    global output
    words = message.split(" ")
    emojis = {
        ":)": "đ",
        ":(": "âšī¸"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter())
# print(output)
