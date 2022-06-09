#when interest compound anually
def compound_interest(principle, rate, time):
 
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)
compound_interest(7500, 4, 2)
