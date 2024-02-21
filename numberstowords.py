def convertToWords(num):
    print("Number to convert: ", num)

    list_output = []

    # Dictionary for numbers    
    # base 
    base_dict = {
        0: 'zero', 1: 'one', 2:'two', 3: 'three',
        4: 'four', 5: 'five', 6:'six', 7: 'seven',
        8: 'eight', 9: 'nine',
    }
    # tens
    tens_dict = {
        2: 'twenty', 3: 'thirty', 
    }

    # evaluate the number
    temp_num = num
    # get the tens value
    if temp_num > 10:
        temp_num = int(temp_num / 10)
        list_output.append( tens_dict[temp_num] )

    # get the base value
    temp_num = num % 10
    list_output.append( base_dict[temp_num] )

    res = " ".join(list_output)
    print(res)
    

numberInput = int(input("Enter the number you want between 0-9 and between 20-30: "))

convertToWords(numberInput)