import json
def interest(int_cent, ini_principal): # declare function interest with parameters
    month_count = int(input("Enter the number of months:\t")) # user inputs the number of months interest on priniciple to be calculated
    month = 1
    int_dict = {} # initialize dictionary to store the data
    while month <= month_count: # loop the months in the month_count
        int_year = float(ini_principal * (int_cent/100)) # interest in a year
        int_month = int_year/12 # interest in a month
        curr_principle = ini_principal # initialize the value of the principal to a new variable
        int_dict[month] = {} # create a dictionary inside the initial dict creating a nested dict

        #Input values into the nested dict
        int_dict[month][f'Principle {month} month'] = round(curr_principle, 2)
        int_dict[month][f'Interest {month} month'] = int_cent/100
        int_dict[month][f'Interest Year {month} month'] = round(int_year, 2)
        int_dict[month][f'Interest Month {month} month'] = round(int_month, 2)

        ini_principal += int_month # add principal and interest in a month
        int_dict[month][f'Compound Amount {month} month'] = round(ini_principal, 2)
        month += 1 # increment the loop
    choice = input("Press Enter to choose to print all months or (SPEC) for specific month:\t")
    if choice == 'SPEC': # use if-else statement to prompt user to choose what data to be displayed
        x = int(input("Choose the month to view:\t"))
        with open('interest.txt', 'w') as convert_file:
            convert_file.write(json.dumps(int_dict[x]))
    else:
        with open('interest.txt', 'w') as convert_file:
            convert_file.write(json.dumps(int_dict))
    #display results in notepad

a = int(input("Enter the % interest:\t"))
b = int(input("Enter the initial principle:\t"))

interest(a, b) # pass arguments into the function
