filet = input("Select file ")
with open(filet, 'r') as f:
    file = f.read()
for line in file.splitlines():
    # Print each line
    string = line.strip()
    if string.endswith(")"):
        string = string + ";"
    if string.startswith("  "):
        string = "  " + string
    
    print(string)
    with open('output.txt', 'a') as f:
        f.write(string + '\n')

    

