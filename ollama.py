import re
with open("lorem.txt", "r") as file:
    lorem_text = file.read()
    sentences = re.split(r'(?<=[.!?]) +', lorem_text)

with open("sentences.txt", "w") as file:
    for sentence in sentences:
        file.write(sentence + "\n")