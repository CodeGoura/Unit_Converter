'''this is an unit converter app for user this is used to convertr unit one unit scale to 
other .... Written by a student on paython'''
op = print('''Please select the unit convertor whiich one you want
                                       No1: Length conversion
                                       No2: mass convertion
                                       No3: Time conversion
                                       No4: Area conversion
                                       No5:EXIT  ''')  # This is show the option to the user for unit convertor
option = int(input('Please chose any option For Unit conversion: '))
if option == 1:
    # this is option 1 section
    # based on length conversion
    #############################################################################
    print('length Conversion Wizard \n Please Select Any option for convertion\n \
          No 1: kilomiter to centimeter \n \
          No 2: Meter to centimeter \n \
          No 3: Centimeter to Meter \n')
    lent = int(input('Pleae Select one option  for coverting units :'))
    if lent == 1:
        l1 = eval(
            input('To convert Kilometer to centimeter please Enter Value: '))
        ccm = l1*10000
        print(f'{l1} after converti1ng to centimeter {ccm}')
    elif lent == 2:

        l2 = eval(input('To convert meter to centimeter please enter value: '))
        cme =l2*100
        print(f'{l2} after convert to centimeter the value is {cme}')
        #need value change from this line
    elif lent == 3 :
        l3= eval(input('To convert Centimeter to Meter please enter value: '))
        meter =l3*0.01
        print(f'{l3} after convert to centimeter the value is {meter}')
    elif len==4 :
        l4 = eval(input('To convert Millimeter to meter please enter value: '))
        milli_m =l4*0.001
        print(f'{l4} after convert to centimeter the value is {milli_m}')
    elif len == 5:
        l5 = eval(input('To convert micrometres to meter please enter value: '))
        micro_m =l5*100
        print(f'{l5} after convert to centimeter the value is {micro_m}')
    elif len ==6:
        me = eval(input('To convert meter to centimeter please enter value: '))
        cme =me*100
        print(f'{me} after convert to centimeter the value is {cme}')
    elif len ==7:
        me = eval(input('To convert meter to centimeter please enter value: '))
        cme =me*100
        print(f'{me} after convert to centimeter the value is {cme}')
    elif len == 8:
        me = eval(input('To convert meter to centimeter please enter value: '))
        cme =me*100
        print(f'{me} after convert to centimeter the value is {cme}')
    elif len == 9:
        me = eval(input('To convert meter to centimeter please enter value: '))
        cme =me*100
        print(f'{me} after convert to centimeter the value is {cme}')
    elif len == 10:
        me = eval(input('To convert meter to centimeter please enter value: '))
        cme =me*100
        print(f'{me} after convert to centimeter the value is {cme}')
    elif len == 11:
        me = eval(input('To convert meter to centimeter please enter value: '))
        cme =me*100
        print(f'{me} after convert to centimeter the value is {cme}')
    else:
        print('your entered wrong value please check and try again')

elif option == 2:
    # this is option 2 section
    # based on mass conversion
    #############################################################################

elif option == 3:
    # this is option 3 section
    # based on time conversion
    ############################################################################
    
elif option == 4:
    # this is option 2 section
    # based on Area conversion
    #############################################################################

elif option == 5:
    # cancel programme section
    # this is terminate the programme
    print('Are You Sure You Want To Close This application Type Y for Yes Or N For NO')
    confrom = input('Please Confrom for Closing Application : ')
    if confrom == 'y' or 'Y':
        exit()
    else:
        print(op)
else:
    print('you entered a wrong value Please select again')
