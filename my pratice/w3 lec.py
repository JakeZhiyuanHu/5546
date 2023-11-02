d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")
    # Unpacking
    key, value = key_value_tuple
    print(f"KEY: {key} VALUE: {value}")



sum_of_evens = 0
for i in range(1,101):
    print(f'Loop is on {i}')
    if i % 2 == 1:      # i is odd
        continue
    print(f'    summing the value of {i}')
    sum_of_evens = sum_of_evens + i
print(f'Sum of evens is {sum_of_evens}')


def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

tic = "WES.AX"
qan_tic()

data = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]

not_a_tup = (k for k, v in data)
print(f'The type of `(k for k, v in data)` is {type(not_a_tup)}')