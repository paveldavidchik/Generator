
def accelerator():
    total = 0
    while True:
        value = yield total
        print(f'Get {value}')
        if not value:
            break
        total += value


generator = accelerator()
next(generator)
print(f'Accumulated {generator.send(1)}')
print(f'Accumulated {generator.send(1)}')
