class DateCalculator:
    def __init__(self, year,month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_calculator(self):
        Y = self.year
        m = self.month
        q = self.day

        if m < 3:
            m += 12
            #m=m+12
            Y -= 1
            #y = y-1

        K = Y % 100
        J = Y // 100

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

x = int(input("Input the Year: "))
y = int(input("Input the Month: "))
z = int(input("Input the Day: "))

d = DateCalculator(x, y, z)
print(f"The day of the week on {z}/{y}/{x} is: {d.day_calculator()}")