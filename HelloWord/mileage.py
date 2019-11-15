print("How many kilometer did you have cycle?");

kms = input();
miles = float(kms)/1.60934;
miles = round(miles,3);

print(f"{kms}km Convert To {miles}mi");