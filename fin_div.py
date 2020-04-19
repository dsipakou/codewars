def divisors(integer):
    output = []
    for i in range(2, integer):
        if integer % i == 0:
            output.append(i)
    if len(output) > 0:
        return output
    else:
        return str(integer) + " is prime"