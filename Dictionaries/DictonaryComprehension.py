numbers = dict(first=1, second=2, third=3, fourth=4)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}

for key, value in squared_numbers.items():
    print(f"Square of {key} = {value}")

num_list = list(range(1, 11))
even_or_odd = {num: {'even' if num % 2 == 0 else 'odd'} for num in num_list}
for key, value in even_or_odd.items():
    print(f"{key}: {value}")
