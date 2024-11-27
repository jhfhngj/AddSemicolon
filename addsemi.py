filet = input("Select file ")
with open(filet, 'r') as f:
    file = f.read()
for line in file.splitlines():
    # Print each line
    string = line.rstrip() # Strip
    if string.endswith(")"): # Scan for need of semicolon
        string = string + ";" # Add semicolon
    #if string.startswith("  "): Wiped because of rstrip
     #   string = "  " + string
    
    print(string)	# Testing phase code, may be used for debugging
    with open('output.txt', 'a') as f:	# Write
        f.write(string + '\n')	# Newline 

    

