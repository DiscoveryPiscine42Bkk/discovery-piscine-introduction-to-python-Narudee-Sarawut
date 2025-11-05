table = 1
while table <= 10:
    print(f"\nMultiplication table for {table}:")  
    multiplier = 1
    while multiplier <= 10:
        result = table * multiplier
        print(f"{table} x {multiplier} = {result}")
        multiplier += 1
    table += 1
