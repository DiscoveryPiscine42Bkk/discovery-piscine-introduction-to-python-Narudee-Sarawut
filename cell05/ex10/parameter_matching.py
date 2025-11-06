import sys 
if len(sys.argv) == 2:
    keyword = sys.argv[1] 
    user_word = input("Enter a word: ")
    if user_word == keyword:
        print("Good job!", "\n")
    else:
        print("Nope, sorry...", "\n")
else:
    print("none", "\n")
