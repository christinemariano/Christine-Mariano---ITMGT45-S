'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

import math

def compute_savings(gross_pay, tax_rate, expenses):
    taxable_income = gross_pay - (gross_pay * tax_rate)
    savings = taxable_income - expenses
    return savings

def compute_after_tax(gross_pay, tax_rate):
    after_tax = math.floor(gross_pay - (gross_pay * tax_rate))
    return after_tax

# ask for the gross pay, tax rate, and expenses
gross_pay = int(input("Input gross pay: "))
tax_rate = float(input("Input tax rate: "))
expenses = int(input("Input expenses: "))

# compute for after-tax pay and savings of employee
after_tax = compute_after_tax(gross_pay, tax_rate)
savings = compute_savings(gross_pay, tax_rate, expenses)

print("Your gross pay is", gross_pay, "pesos.")
print("Your tax rate is {:.2%}.".format(tax_rate))
print("Your expenses have totaled to", expenses, "pesos.")
print("Your after-tax pay is", after_tax, "pesos.")
print("Your remaining money after taxes and expenses is {:.2f} pesos.".format(savings))

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def compute_material_waste(total_material, material_unit, num_jobs, job_consumption):
    total_consumed_material = num_jobs * job_consumption
    material_waste = total_material - total_consumed_material
    return material_waste, material_unit

# ask for total material available
total_material = int(input("Input total material available: "))
print("The total material available is", total_material)

# ask for number of jobs
num_jobs = int(input("Input the number of jobs to run: "))
print("The number of jobs to run is", num_jobs)

# ask for material unit
material_unit = input("Input the units used to express quantity of material: ")
print("The units used are", material_unit)

# ask for material consumption per job
job_consumption = int(input("Input the amount of material consumed per job: "))

# compute the amount of remaining material
material_waste, material_unit = compute_material_waste(total_material, material_unit, num_jobs, job_consumption)

print("The amount of remaining material is:", material_waste, material_unit)

def interest(principal, rate, periods):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def compute_interest(principal, rate_decimal, periods):
    interest = principal * rate_decimal * periods
    return interest

def compute_final_value(interest, principal):
    final_value = int(principal + interest)
    return final_value

# ask for investment details
principal = int(input("Enter the principal amount in centavos: "))
rate_percentage = float(input("Enter the interest rate in percentage form (without % symbol): "))
periods = int(input("Enter the number of periods invested: "))

# compute interest and final value of investment
rate_decimal = rate_percentage / 100
interest = compute_interest(principal, rate_decimal, periods)
final_value = compute_final_value(interest, principal)

print("Investment Details")
print("Principal Amount: PHP", principal / 100)
print("Interest Rate: {:.2f}%".format(rate_percentage))
print("Number of Periods Invested: {}".format(periods))
print("Interest Earned: PHP", interest / 100)
print("Final Value of Investment: PHP", final_value / 100)

def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def pounds_to_kg(weight_pounds):
    weight_kg = weight_pounds * 0.453592
    return weight_kg

def feet_inches_to_meters(height_ft, height_in):
    height_in += height_ft * 12
    height_meters = height_in * 0.0254
    return height_meters

# ask for weight in pounds
weight_pounds = float(input("Enter your weight in pounds: "))

# convert weight from pounds to kg
weight_kg = pounds_to_kg(weight_pounds)
print("Your weight is", weight_kg, "kilograms.")

# ask for height in feet and inches
height_ft = int(input("Enter your height in feet: "))
height_in = int(input("Enter your height in inches: "))

# convert height from feet and inches to meters
height_meters = feet_inches_to_meters(height_ft, height_in)
print("Your height is", height_meters, "meters.")

# bmi calculatuon
bmi = weight_kg / (height_meters ** 2)
print("Your BMI is", round(bmi, 2))
