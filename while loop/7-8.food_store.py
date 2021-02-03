sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("We are out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    a = sandwich_orders.pop()
    print(f"I made your {a}")
    finished_sandwiches.append(a)

for i in finished_sandwiches:
    print(i)

