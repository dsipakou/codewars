def parse_bank_account(bank_account):
    account = list(bank_account.split('\n'))
    d = {
        " _ | ||_|": 0,
        "     |  |": 1,
        " _  _||_ ": 2,
        " _  _| _|": 3,
        "   |_|  |": 4,
        " _ |_  _|": 5,
        " _ |_ |_|": 6,
        " _   |  |": 7,
        " _ |_||_|": 8,
        " _ |_| _|": 9,
    }
    output = []
    for i in range(0, len(account[0]), 3):
        number = account[0][i:i+3] + account[1][i:i+3] + account[2][i:i+3]
        output.append(d[number])
    output = ''.join(str(s) for s in output)
    return int(output)