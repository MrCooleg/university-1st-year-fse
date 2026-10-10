n = int(input())

seconds = n % 60
minutes = (n // 60) % 60
hours = (n // 3600) % 24

print(f'{hours}:{minutes:0>2}:{seconds:0>2}')