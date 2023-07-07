print("barname mohasebe BMI")
w=int(input("vazn shakhs ra vared konid (be kg)"))
h=int(input("ghad shakh ra vared konid (be metr)"))
bmi=w/(h*h)
if bmi<=18.5:
    print("your BMI is underweight")
elif bmi<=24.9:
    print("your BMI is normal")
elif bmi<=29.9:
    print("your BMI is over weight")
elif bmi<=34.9:
    print("your BMI is obese")
elif bmi>=35:
    print("your BMI is extremely obese")