print("Please answer the following questions with 'yes' or 'no'.")
fever = input("Do you have a fever? ")
cough = input("Do you have a cough? ")
fatigue = input("Do you feel tired or fatigued? ")
breathing = input("Are you experiencing shortness of breath or difficulty breathing? ")

if fever == "yes" and cough == "yes" and fatigue == "yes" and breathing == "yes":
    print("You may have COVID-19. Please contact a medical professional.")
elif fever == "yes" and cough == "yes" and fatigue == "yes":
    print("You may have the flu. Please contact a medical professional.")
elif cough == "yes" and breathing == "yes":
    print("You may have asthma. Please contact a medical professional.")
else:
    print("It's unclear what disease you may have. Please contact a medical professional for further evaluation.")

