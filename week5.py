def gen():
    #list
    d = []
    #user input
    user_input = input("enter 6 digit code: ")
    #check if user has entered 6 numbers
    if len(user_input) != 6:
        print("Error must enter 6 numbers") 
    else:
        #turn user input into single ints
        d = [int(digit) for digit in user_input]

        #work out 7th dig
        d7 = (4*d[0]+10*d[1]+9*d[2]+2*d[3]+1*d[4]+7*d[5]) % 11 
        #create error if greater than 9
        if d7 < 10:
            d.append(d7)


        d8 = (7*d[0]+8*d[1]+7*d[2]+1*d[3]+9*d[4]+6*d[5]) % 11 
        if d8 < 10:
            d.append(d8)


        d9 = (9*d[0]+1*d[1]+7*d[2]+8*d[3]+7*d[4]+7*d[5]) % 11 
        if d9 < 10:
            d.append(d9)

        d10 = (1*d[0]+2*d[1]+9*d[2]+10*d[3]+4*d[4]+1*d[5]) % 11
        if d10 < 10:
            d.append(d10)

        #if list is smaller than 10 print error
        size = len(d)
        if size < 10:
            print("unusable number")
        else:
            print(d)
gen()