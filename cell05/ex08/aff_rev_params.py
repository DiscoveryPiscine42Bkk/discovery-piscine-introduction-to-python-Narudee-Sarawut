import sys 
params = sys.argv[1:]
if len(params) < 2:
    print("none", "\n")
else:
    for p in reversed(params):
        print(p)
