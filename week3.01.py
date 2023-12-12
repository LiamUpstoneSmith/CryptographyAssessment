def coder():
    d = []
    no_s = [2, 6, 7, 8, 10]
    #user input
    user_input = input("enter 10 digit code: ")
    #turn user input into single ints
    d = [int(digit) for digit in user_input]

    noErrors = True
    while noErrors:

        s1 = (1*d[0]+1*d[1]+1*d[2]+1*d[3]+1*d[4]+1*d[5]+1*d[6]+1*d[7]+1*d[8]+1*d[9]) % 11
        s2 = (1*d[0]+2*d[1]+3*d[2]+4*d[3]+5*d[4]+6*d[5]+7*d[6]+8*d[7]+9*d[8]+10*d[9]) % 11
        s3 = (1*d[0]+4*d[1]+9*d[2]+5*d[3]+3*d[4]+3*d[5]+5*d[6]+9*d[7]+4*d[8]+1*d[9]) % 11
        s4 = (1*d[0]+8*d[1]+5*d[2]+9*d[3]+4*d[4]+7*d[5]+2*d[6]+6*d[7]+3*d[8]+10*d[9]) % 11

        P = ((s2 * s2 ) - (s1 * s3)) % 11
        Q = ((s1 * s4) - (s2 * s3)) % 11
        R = ((s3 * s3) - (s2 * s4)) % 11

        #no error
        if (s1, s2, s3, s4) == (0, 0, 0, 0):
            print("no errors")
            print(d)
            print(P,Q,R)
            noErrors = False

        #single error
        elif P==0 & Q==0 & R==0:
            mag = s1
            inverse = 0 #vaule of s1 multiplyed
            holder = 0 #will be what s1 is multiplyed by aka inverse
            while inverse != 1:
                holder += 1
                y = s1 * holder
                inverse = y % 11

            
            pos = (s2 * holder) % 11 #find out the pos of error

            d[pos - 1] -= mag #how to change the error
            #print new code
            print(d)
            print("single error")
            print(("a = "),mag ,"i = ",pos," , syn = ",s1, s2, s3, s4)
            noErrors = False
        #double error    
        elif P!= 0 or Q!= 0 or R!=0:
            #workout i
            i1 = ((Q**2)-(4*P*R)) % 11 # square root of part 1 of 1
            if (i1 * i1) % 11 in no_s or ((i1 * i1) % 11) > 10:
                print("more than 2 errors")
                break
                
            else:
                sq = 1
                while (sq * sq) % 11 != i1:
                    sq += 1

            
            i2 = (2*P) % 11 # part 2 of equashion
            
            i3 = (-Q + sq) % 11 # part 2 of part 1 
            y = 1
            #inverse function
            while ((i2)*y) % 11 != 1:
                y += 1 
            #works out i
            i = (i3 * y) % 11

            #workout J
            j1 = ((Q**2)-(4*P*R)) % 11 # square root of part 1 of 1
            if j1 % 11 in no_s or (j1 % 11) > 10:
                print("more than 2 errors")
                break
                
                
            else:
                sq2 = 1
                while (sq2 * sq2) % 11 != j1:
                    sq2 += 1

            j2 = int((2*P) % 11) # part 2 of equashion
            j3 = int((-Q - sq2) % 11) # part 2 of part 1 
            y = 1
            #inverse function
            while ((j2)*y) % 11 != 1:
                y += 1 
            #works out j
            j = (j3 * y) % 11

            #workout b and a
            bp2 = (i - j) % 11
            y=1
            while ((bp2)* y) % 11 != 1:
                y += 1

            bp1 = (i * s1) % 11
            hh = (bp1 - s2) % 11
            b = (hh * y) % 11
            a = (s1 - b) % 11

            old_i = d[i - 1]
            new_i = (old_i - a) % 11 #current vaule - magA

            old_j = d[j - 1]
            new_j = (old_j - b) % 11 #current vaule - magB
            

            d[i - 1] = new_i #add new value
            d[j - 1] = new_j #add new value

            print(("i ="),i ,"a =",a,"j =",j,"b =",b," , syn = ",s1, s2, s3, s4, ",PQR =",P,Q,R)
            print(d)
            noErrors = False

coder()

