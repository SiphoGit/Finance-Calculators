import math


# Displayed message when user opens the calculator.
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print('''
    investment - to calculate the amount of interest you'll earn on investment
    bond       - to calculate the amount you'll have to pay on a home loan \n''')  
 
# User's calculator selection.
calculator = input("Select calculator: ").lower()
investment_calculator = "investment"
bond_calculator = "bond"

# Error message when invalid calculator option entered.
while (
    calculator != investment_calculator and
    calculator != bond_calculator):
    print("\nInvalid input, please select investment or bond calculator.\n")
    calculator = input("Select calculator: ").lower()

else:
    print("You've selected {} calculator.\n".format(calculator))  


# Investment calculator.
# User's input.
if calculator == investment_calculator:
    investment_amount = float(input("Investment amount: R"))
    interest_rate = float(input("Annual interest: "))
    investment_period = float(input("Investment period: "))
    interest = input("Simple or Compound interest?: ").lower()
    simple_interest = "simple"
    compound_interest = "compound"

    # Error message when invalid interest type entered.
    while (
        interest != simple_interest and
        interest != compound_interest):
        print("\nInvalid input, please select simple or coumpound interest.\n")
        interest = input("Simple or Compound interest?: ").lower()

    else:
        print("\nYou've selected {} interest.\n".format(interest))
        

    # Simple interest calculator.    
        if interest == simple_interest:

            future_value = round((
                investment_amount
                * (1 + (interest_rate/100)
                * investment_period)), 2)           # Simple interest formula.    
            
            print(
                '''
                Invested amount   : R{}
                Annual interests  : {}%
                Interest type     : {}
                Investment period : {} years
                Future Value      : R{}'''.format(investment_amount,
                                                    interest_rate,
                                                    interest,
                                                    investment_period,
                                                    future_value))

    
        # Compound interest calculator.
        
        else:  

            future_value = round((
                investment_amount
                * math.pow((1+(interest_rate/100)),
                            investment_period)), 2)   # Compound interest formula.
                
            print(
                '''
                Invested amount   : R{}
                Annual interests  : {}%
                Interest type     : {}
                Investment period : {} years
                Future Value      : R{}'''.format(investment_amount,
                                                    interest_rate,
                                                    interest,
                                                    investment_period,
                                                    future_value))                                           
else:

    # Bond Calculator.
    # User's input.
    
    house_present_value = float(input("Enter house value: R"))
    bond_annual_interests = float(input("Loan interests: "))
    payment_period_in_years = float(input("Payment period (years): "))
    
    # Converting annual inputs to monthly.
    
    monthly_interests = (bond_annual_interests / 12) / 100
    number_of_payments = payment_period_in_years * 12
    

    #Bond monthly payment formula.

    bond_monthly_payments = round(((
        house_present_value * (monthly_interests * math.pow((1 + monthly_interests)
                            , number_of_payments)))
        / (math.pow((1 + monthly_interests), number_of_payments) - 1)))
    

    print(
        '''
           Bond Amount        : R{}
           Annual interests   : {}%
           Number of payment  : {}
           Monthly payment    : R{}'''.format(house_present_value,
                                              bond_annual_interests,
                                              number_of_payments,
                                              bond_monthly_payments))
        
            
                              

    

        

        

        

        
    
                          
