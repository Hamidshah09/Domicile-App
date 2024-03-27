def SpellNumber(MyNumber):

    Temp = ""
    Dollars = ""
    Cents = ""

    DecimalPlace = 0
    Count = 0

    Place = ['', '', ' Thousand ', ' Million ', ' Billion ', ' Trillion ']

#     ' String representation of amount.

    MyNumber = str(MyNumber)
    MyNumber = MyNumber.strip()
#     ' Position of decimal place 0 if none.

#     DecimalPlace = InStr(MyNumber, ".")

#     ' Convert cents and set MyNumber to dollar amount.

#     if DecimalPlace > 0:

#     Cents = GetTens(Left(Mid(MyNumber, DecimalPlace + 1), 2))

#     MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))

#     End If

    Count = 1

    while MyNumber != "":

        Temp = GetHundreds(MyNumber[-3:])
        # if Temp is None:
        #     Temp = ''
        if Temp != "":
            print(Temp, Place[Count], Dollars)
            Dollars = "{}{}{}".format(Temp, Place[Count], Dollars)
        if len(MyNumber) > 3:
            MyNumber = MyNumber[:(len(MyNumber) - 3)]
            # MyNumber = MyNumber + "000"
        else:
            MyNumber = ""
        print(MyNumber)
        Count = Count + 1
    if Dollars == '':
        Dollars = 'No Rupees'
    elif Dollars == 'One':
        Dollars == 'One Rupees'
    else:
        Dollars = Dollars + "Rupees Only"

#     'Select Case Cents

#     'Case ""

#     'Cents = " and No Cents"

#     'Case "One"

#     'Cents = " and One Cent"

#     'Case Else

#     'Cents = " and " & Cents & " Cents"

#     'End Select

    SpellNumber = Dollars + Cents
    return SpellNumber
# ' Converts a number from 100-999 into text


def GetHundreds(MyNumber):

    Result = ''

    if int(MyNumber) == 0:
        return ''

    MyNumber = "000" + MyNumber
    MyNumber = MyNumber[-3:]

#     ' Convert the hundreds place.

    if MyNumber[:1] != "0":

        Result = GetDigit(MyNumber[:1]) + " Hundred "


#     ' Convert the tens and ones place.

    if MyNumber[1] != "0":
        gttens = GetTens(MyNumber[1:])
        if gttens is not None:
            Result = Result + gttens

    else:
        gttens = GetTens(MyNumber[2:])
        if gttens is not None:
            Result = Result + gttens

    return Result


#     ' Converts a number from 10 to 99 into text.


def GetTens(TensText):

    Result = ""

    if int(TensText[:1]) == 1:

        if int(TensText) == 10:
            Result = "Ten"
        elif int(TensText) == 11:
            Result = "Eleven"
        elif int(TensText) == 12:
            Result = "Twelve"
        elif int(TensText) == 13:
            Result = "Thirteen"
        elif int(TensText) == 14:
            Result = "Fourteen"
        elif int(TensText) == 15:
            Result = "Fifteen"
        elif int(TensText) == 16:
            Result = "Sixteen"
        elif int(TensText) == 17:
            Result = "Seventeen"
        elif int(TensText) == 18:
            Result = "Eighteen"
        elif int(TensText) == 19:
            Result = "Nineteen"

    else:

        if int(TensText[:1]) == 2:
            Result = "Twenty "
        elif int(TensText[:1]) == 3:
            Result = "Thirty "
        elif int(TensText[:1]) == 4:
            Result = "Forty "
        elif int(TensText[:1]) == 5:
            Result = "Fifty "
        elif int(TensText[:1]) == 6:
            Result = "Sixty "
        elif int(TensText[:1]) == 7:
            Result = "Seventy "
        elif int(TensText[:1]) == 8:
            Result = "Eighty "
        elif int(TensText[:1]) == 9:
            Result = "Ninety "
        gtdigit = GetDigit(TensText[-1:])
        if gtdigit is not None:
            Result = Result + gtdigit

    return Result
#     ' Converts a number from 1 to 9 into text.


def GetDigit(Digit):
    if int(Digit) == 1:
        GetDigit = "One"
    elif int(Digit) == 2:
        GetDigit = "Two"
    elif int(Digit) == 3:
        GetDigit = "Three"
    elif int(Digit) == 4:
        GetDigit = "Four"
    elif int(Digit) == 5:
        GetDigit = "Five"
    elif int(Digit) == 6:
        GetDigit = "Six"
    elif int(Digit) == 7:
        GetDigit = "Seven"
    elif int(Digit) == 8:
        GetDigit = "Eight"
    elif int(Digit) == 9:
        GetDigit = "Nine"
    else:
        GetDigit = ""
    return GetDigit


print(GetHundreds('2220'))
