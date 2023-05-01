#!/usr/bin/env python
# coding: utf-8

# ## Savings
# 1. Ask for the gross pay of the employee.
# 2. Ask for the tax rate.
# 3. Multiply the tax rate to the gross pay. Round down.
# 4. Ask for the expenses.
# 5. Subtract the expenses from the after-tax pay of the employee.

# In[ ]:


def compute_savings(gross_pay,tax_rate,expenses):
    savings = gross_pay - ((gross_pay*tax_rate)+expenses)
    return savings

import math

def compute_aftertax (gross_pay,tax_rate):
    after_tax = math.floor(gross_pay - (gross_pay*tax_rate))
    return after_tax

# Ask for the gross pay.
gross_pay = int(input("Input gross pay:"))
print("Your gross pay is", gross_pay)

# Ask for the tax rate.
tax_rate = float(input("Input tax rate:"))
print("Your tax rate is", tax_rate)

# Ask for the expenses.
expenses = int(input("Input expenses:"))
print("Your expenses have totaled to", expenses)

# Compute for the after-tax pay of the employee.
after_tax = compute_aftertax(gross_pay,tax_rate)

# Compute for the savings of the employee.
savings = compute_savings(gross_pay,tax_rate,expenses)

# Display savings.
print("Your remaining money after taxes and expenses is", savings*100, "centavos")


# ## Material Waste
# 1. Ask for the total material available.
# 2. Ask for the number of jobs.
# 3. Ask for the material consumption per job.
# 4. Multiply the number of jobs by the material consumption per job.
# 5. Subtract the total material consumed from the total material available.

# In[ ]:


def compute_materialwaste(total_material, material_units, num_jobs, job_consumption):
    materialwaste = total_material - set_job
    return materialwaste

# Ask for the total material available.
total_material=int(input("Input total material available:"))
print("The total material available is", total_material)

#Ask for the number of jobs.
num_jobs=int(input("Input the number of jobs to run:"))
print("The number of jobs to run is", num_jobs)

#Ask for the material consumption per job.
material_units= input("Input the units used to express quantity of material:")
print("The units used is", material_units)

#Job Consumption
job_consumption = int(input("The amount of material consumed per job is:"))

#Multiply the number of jobs by the material consumption per job.
set_job=num_jobs*job_consumption

#Subtract the total material consumed from the total material available.
materialwaste = compute_materialwaste(total_material, material_units, num_jobs, job_consumption)

print("The amount of remaining material is:", materialwaste, material_units)


# ## Interest
# 1. Ask for the principal.
# 2. Ask for the rate in decimal notation.
# 3. Ask for the number of period.
# 4. Compute for the interest.
# 5. Compute for the final value.
# 
# Note: 
# * Simple Interest = Principal * Rate * Time
# * Final Value = Principal + Interest

# In[ ]:


def compute_interest(principal,rate_decimal,periods):
    interest = principal*rate_decimal*periods
    return interest

def compute_finalvalue(interest,principal):
    finalvalue = int(principal + interest)
    return finalvalue

# Ask for the principal.
principal = int(input("Input principal in centavos:"))
print("Your principal is", principal, "centavos")

# Ask for the rate.
rate_percentage = float(input("Input rate in percentage form (do not include % symbol):"))
rate_decimal = rate_percentage / 100
print("Your rate is", rate_decimal)

# Ask for the number of periods invested.
periods = int(input("Input the number of periods invested:"))
print("You invested for", periods, "period/s")

# Compute for the interest.
interest = compute_interest(principal,rate_decimal,periods)

# Compute for the final value.
finalvalue = compute_finalvalue(interest,principal)

# Display final value of investment.
print("The final value of your investment is: PHP", finalvalue)


# ## Body Mass Index
# 
# 1. Ask for the weight of the person in pounds, and convert it in kilograms.
# 2. Ask for the height of the person in feet and inches, and convert it in meters.
# 3. Compute for the BMI.

# In[ ]:


# Ask for the weight of the person in pounds, and convert it in kilograms.
weight_pounds = float(input("Input your weight in pounds:"))
weight_kg = weight_pounds *0.453592
print("Your weight in pounds is equal to", weight_kg, "in kilograms.")

# Ask for the height of the person in feet and inches, and convert it in meters.
height_ft = int(input("Feet:"))
height_in = int(input("Inches:"))

height_in += height_ft *12

height_meters = ((height_in)/12)*0.3048

print("Your height in feet is equal to", height_meters, "in meters.")

# Compute for the BMI.
bmi = weight_kg / (height_meters**2)
print("Your BMI is:", bmi)

