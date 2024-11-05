N = int(input().strip())
cities = set()
for _ in range(N):
    city = input().strip()
    cities.add(city)
new_city = input().strip()
if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK")
