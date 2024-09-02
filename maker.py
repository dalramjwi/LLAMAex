import lorem
lorem_text = [lorem.text() for _ in range(1000)]
lorem_text = "\n\n".join(lorem_text)
with open("lorem.txt","w") as file:
    file.write(lorem_text)