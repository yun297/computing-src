def validateNRIC(nric):
    digitWeight = {
        1: 2,
        2: 7,
        3: 6,
        4: 5,
        5: 4,
        6: 3,
        7: 2
    }

    remainderST = {
        0: 'J',
        1: 'Z',
        2: 'I',
        3: 'H',
        4: 'G',
        5: 'F',
        6: 'E',
        7: 'D',
        8: 'C',
        9: 'B',
        10: 'A'
    }

    remainderFG = {
        0: 'X',
        1: 'W',
        2: 'U',
        3: 'T',
        4: 'R',
        5: 'Q',
        6: 'P',
        7: 'N',
        8: 'M',
        9: 'L',
        10: 'K'
    }

    print("Validating NRIC: " + nric + " ...")

    # length check
    if len(nric) == 9:
        print("Valid NRIC length")
    else:
        print("Invalid NRIC length")
        exit()

    # format check

    for i in range(1, 8):
        if nric[i].isdigit():
            continue
        else:
            print("Invalid NRIC format")
            exit()
    print("Valid NRIC format")

    # first letter check

    if nric[0].isalpha() == True and (nric[0] == 'S' or nric[0] == 'T' or nric[0] == 'F' or nric[0] == 'G'):
        print("Valid NRIC first letter")
    else:
        print("Invalid NRIC first letter")
        exit()

    # last letter check

    sum = 0
    if nric[0] == 'S' or nric[0] == 'T':
        for i in range(1, 8):
            sum += int(nric[i]) * digitWeight[i]
        remainder = sum % 11
        if nric[8] != remainderST[remainder]:
            print("Invalid NRIC last letter")
            exit()

    elif nric[0] == 'F' or nric[0] == 'G':
        for i in range(1, 8):
            sum += int(nric[i]) * digitWeight[i]
        remainder = sum % 11
        if nric[8] != remainderFG[remainder]:
            print("Invalid NRIC last letter")
            exit()

    print("Valid NRIC")


validateNRIC("T0771574G")
