def synthetic(dividends, divisor):

    results = [dividends[0]]

    for index, dividend in enumerate(dividends):
        if index == 0 :
            continue  # Skip first number

        row_number = results[-1] * divisor

        result = dividend + row_number

        results.append(result)

    return results

dividends = []

print "Enter the coefficients of the dividend."

while True:
    dividend = raw_input("Coefficient: ")
    try:
        dividend = float(dividend)
    except ValueError:
        break

    dividends.append(dividend)

divisor = float(raw_input("Divisor: "))

print synthetic(dividends, divisor)
