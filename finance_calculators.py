import math

def simple_interest_calculator(amount: float, interests: float, period: float) -> float:
    # calculates future value
    future_value = round((amount* (1 + (interests/100)* period)), 2)    

    return(f'''
    Invested amount   : R{amount}
    Interests         : {interests}%
    Interest type     : {"Compound"}
    Investment period : {period} years
    Future Value      : R{future_value}''')     

def compound_interest_calculator(amount: float, interests: float, period: float) -> float:    
    # calculates future value
    future_value = round((amount* math.pow((1+(interests/100)),period)), 2) 
        
    return(f'''
        Invested amount   : R{amount}
        Interests         : {interests}%
        Interest type     : {"Compound"}
        Investment period : {period} years
        Future Value      : R{future_value}''')            


def bond_calculator(bond_annual_interests: float, payment_period_in_years: float, 
                    house_present_value: float) -> float:
  
    try:
        monthly_interests = (bond_annual_interests / 12) / 100
        number_of_payments = payment_period_in_years * 12
        
        #Calculates monthly payments.
        bond_monthly_payments = round(
            ((house_present_value *
            (monthly_interests * math.pow((1 + monthly_interests),
            number_of_payments)))/
            (math.pow((1 + monthly_interests), number_of_payments) - 1)))
               
        return(
        f'''
        House value        : R{house_present_value}
        Annual interests   : {bond_annual_interests}%
        Number of payment  : {number_of_payments}
        Monthly payment    : R{bond_monthly_payments}''')
    except ZeroDivisionError:
        print("Bond interests and payment period can't be zero")
    
def main():

    while True:
        #Main menu 
        calculator_type = input(
            '''
Select Calculator:
I - Investment Calculator
B - Bond calculator
E - to exit the program
>>> '''
        ).capitalize()
        
        if calculator_type == "I":
            
            while True: 
                try:
                    choice = int(input(
                        '''Select interest type:
                            1 - Simple interest
                            2 - Compound interest
                            3 - Back to main menu
                            >>> '''))                        
                                                   
                    if choice == 1:
                        amount = float(input("Investment amount: R"))
                        interests = float(input("Annual interest: "))
                        period = float(input("Investment period(years): "))
                        future_value = simple_interest_calculator(amount, interests, period)
                        print(future_value)
                    if choice == 2:
                        amount = float(input("Investment amount: R"))
                        interests = float(input("Annual interest: "))
                        period = float(input("Investment period(years): "))
                        future_value = compound_interest_calculator(amount, interests, period)
                        print(future_value)
                    if choice == 3:
                        break
                except ValueError:
                    print("Invalid input value")
        elif calculator_type == "B":
            while True:
                choice = input("\nPress Enter to continue or B to go back to the main menu: ").capitalize()

                if choice == "":
                    try:
                        house_present_value = float(input("\nEnter house value: R"))
                        bond_annual_interests = float(input("Bond interests: "))
                        payment_period = float(input("Payment period (years): "))
                        monthly_payments = bond_calculator(bond_annual_interests, payment_period, house_present_value)
                        print(monthly_payments)
                    except ValueError:
                        print("Invalid input value")
                if choice == "B":
                    break
        elif calculator_type == "E":
            break
        else:
            print("Please select I, B, or E")
main()          
                              

    

        

        

        

        
    
                          
