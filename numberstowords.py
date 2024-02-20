def convert(num):
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

    # between 20 and 30
    if num <= 30 and num >= 20:
        # evaluate the number
        temp_num = num
         # get the tens value
        temp_num = int(temp_num / 10)

        list_output.append( tens_dict[temp_num] )

        # get the base value
        temp_num = num % 10
        list_output.append( base_dict[temp_num] )
           

    else:
        print("Sorry, I can only process numbers between 20 and 30")

    print(list_output)
    

convert(21)