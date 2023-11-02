first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
for last in last_names:
    for first in first_names:
        for middle in middle_names:
            if middle:
                print(f"{first} {middle} {last}")
            else:
                print(f"{first} {last}")

for j in range(1, 101):

    if j % 3 == 0 and j % 5 == 0:
        print(f"{j}: FIZZ BUZZ")

    elif j % 3 == 0:
        print(f"{j}: Fizz")

    elif j % 5 == 0:
        print(f"{j}: Buzz")

    else:
        print(j)
