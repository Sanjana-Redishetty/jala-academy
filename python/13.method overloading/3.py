class Demo:
    def process(self, a):
        if a.isdigit():
            print("Processing number:", a)
        else:
            print("Processing string:", a)

d = Demo()
d.process(input("Enter a value (digit or string): "))
