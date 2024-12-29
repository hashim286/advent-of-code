calorie_totals = list()
with open("text.txt") as text:
    total = 0
    while True:
        txt = text.readline()
        if txt == "\n":
            calorie_totals.append(total)
            total = 0
            continue
        try:
            num = int(txt)
        except ValueError:
            break
        total += num


calorie_totals = sorted(calorie_totals, reverse=True)
print(max(calorie_totals))
print(calorie_totals[0] + calorie_totals[1] + calorie_totals[2])
