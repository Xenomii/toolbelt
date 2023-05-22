filename = input("Enter the name of the file: ")

with open(filename, 'r') as f:
    text = f.read()

text = text.replace('\t', ' ')  # Replace tabs with a single space

with open(filename, 'w') as f:
    f.write(text)

print(f"Successfully replaced tabs with spaces in {filename}.")

