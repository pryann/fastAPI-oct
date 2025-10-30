def run_callback(callback):
    callback()


def logger():
    print("Logging from logger function")


run_callback(logger)

salaries = [1000, 2000, 3000, 4000, 5000]
# functional programming to increase each salary by 10%
increased_salaries = list(map(lambda x: x * 1.1, salaries))

print("hello".upper())

s = "hello"
print(type(s))
