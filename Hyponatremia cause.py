# defining corrected sodium in hyperglycemia
def corrected_sodium(Na, glucose):
    return Na + 0.024 * (glucose - 100)

# defining the errors
def incorrect_input(inp):
    if inp == "y" or inp == "n":
        return False
    else:
        return True
    
# defining pathway 2
def pathway_2():                             
    error = True
    print("Evaluate for glucocorticoid deficiency with AM cortisol and ACTH stimulation test, and for hypothyroidism with TSH")
    print("Is AM cortisol or ACTH stimulation test abnormal?")
    while error:
        cortisol = input("y/n? ")
        error = incorrect_input(cortisol)
    error = True
    if cortisol == "y":
        print("Glucocorticoid deficiency")
    else:
        print("Is TSH abnormal?")
        while error:
            tsh = input("y/n? ")
            error = incorrect_input(tsh)
        error = True
        if tsh == "y":
            print("Severe Hypothyroidism")
        else:
            print("SIADH")
            print("Nephrogenic SIADH")
            print("Reset osmostat")
            print("Evaluate underlying etiology")

# defining pathway 3
def pathway_3():
    error = True
    print("Does the patient have edema (peripheral, pulmonary or ascites)?")
    while error:
        edema = input("y/n? ")
        error = incorrect_input(edema)
    error = True
    if edema == "y":
        print("Low effective arterial blood volume (Heart failure or cirrhosis)")
    else:
        print("Any signs of hypovolemia (low BP or postural hypotension)?")
        while error:
            hypovolemia = input("y/n? ")
            error = incorrect_input(hypovolemia)
        error = True
        if hypovolemia == "y":
            print("Measure urine sodium")
            urine_na = int(input(" "))
            if urine_na < 25:
                print("Hypovolemic hyponatremia")
                print("Extrarenal losses (GI losses, third space losses)")
            elif urine_na >= 25 and urine_na <= 40:
                        print("Infuse isotonic saline and remeasure urine sodium")
            else:
                print("Hypovolemic hyponatremia")
                print("Renal losses")
                print("Review history and medications")
                print("Measure AM cortisol and ACTH stimulation test")
                print("Choose among the following:")
                print("1) Low cortisol")
                print("2) Use of diuretics")
                print("3) Head injury or cranial surgery")
                choice = int(input("choose a number (1-3)"))
                if choice == 1:
                    print("Primary adrenal insufficiency")
                elif choice == 2:
                    print("Diuretics induced")
                else:
                    print("Cerebral salt wasting")
        else:
            print("Measure urine sodium and urine osmolality. Urine osmolality:")
            urine_osm = int(input(" "))
            if urine_osm < 100:
                print("Was the measurement done after initiation of therapy")
                while error:
                    therapy = input("y/n? ")
                    error = incorrect_input(therapy)
                error = True
                if therapy == "y":
                    print("Recovery from 1 of the following")
                    print("-Mild hypovolemia (patient given isotonic fluids")
                    print("-Hypopituitarism (patient given glucocorticooids)")
                else:
                    print("Patient with rapid water consumption?")
                    while error:
                        water = input("y/n? ")
                        error = incorrect_input(water)
                    error = True
                    if water == "n":
                        print("High-fluid, low-protein diet, including:")
                        print("-Beer potomania")
                        print("-Tea and toast diet")
                    else:
                        print("Self-induced water intoxication, including:")
                        print("-Psychogenic polydipsia")
                        print("-Endurance activities (marathon)")
                        print("-Ecstasy use")
            else:
                print("What is the urine sodium?")
                urine_na = int(input(" "))
                if urine_na <= 40:
                    print("Ensure sodium intake > 150mEq over next 24 hours (infuse 1l of isotonic saline over 1 or more hours)")
                    print("Remeasure urine sodium and osmolality")
                    print("Is Urine Na < 40 and Urine osmolality < 100?")
                    while error:
                        urine = input("y/n? ")
                        error = incorrect_input(urine)
                    error = True
                    if urine == "y":
                        print("Hypovolemic hyponatremia")
                    else:
                        pathway_2()
                else:
                    pathway_2()
    
# defining pathway 1
def pathway_1():
    error = True
    print("Hypotonic Hyponatremia")
    print("What is the glomerular filtration rate?")
    gfr = int(input(" "))
    if gfr <= 15:
        print("Renal failure")
    else:
        print("Any use of thiazide diuretics?")
        while error:
            thiazide = input("y/n? ")
            error = incorrect_input(thiazide)
        error = True
        if thiazide == "y":
            print("Stop Thiazide")
            print("Did hyponatremia resolve?")
            while error:
                resolved = input("y/n? ")
                error = incorrect_input(resolved)
            error = True
            if resolved == "y":
                print("Thiazide induced hyponatremia")
            else:
                pathway_3()
        else:
            pathway_3()
            print("Does the patient have edema (peripheral, pulmonary or ascites)?")
            while error:
                edema = input("y/n? ")
                error = incorrect_input(edema)
            error = True
            if edema == "y":
                print("Low effective arterial blood volume (Heart failure or cirrhosis)")
            else:
                print("Any signs of hypovolemia (low BP or postural hypotension)?")
                while error:
                    hypovolemia = input("y/n? ")
                    error = incorrect_input(hypovolemia)
                error = True
                if hypovolemia == "y":
                    print("Measure urine sodium")
                    urine_na = int(input(" "))
                    if urine_na < 25:
                        print("Hypovolemic hyponatremia")
                        print("Extrarenal losses (GI losses, third space losses)")
                    elif urine_na >= 25 and urine_na <= 40:
                        print("Infuse isotonic saline and remeasure urine sodium")
                    else:
                        print("Hypovolemic hyponatremia")
                        print("Renal losses")
                        print("Review history and medications")
                        print("Measure AM cortisol and ACTH stimulation test")
                        print("Choose among the following:")
                        print("1) Low cortisol")
                        print("2) Use of diuretics")
                        print("3) Head injury or cranial surgery")
                        choice = int(input("choose a number (1-3)"))
                        if choice == 1:
                            print("Primary adrenal insufficiency")
                        elif choice == 2:
                            print("Diuretics induced")
                        else:
                            print("Cerebral salt wasting")
                else:
                    print("Measure urine sodium and urine osmolality. Urine osmolality:")
                    urine_osm = int(input(" "))
                    if urine_osm < 100:
                        print("Was the measurement done after initiation of therapy")
                        while error:
                            therapy = input("y/n? ")
                            error = incorrect_input(therapy)
                        error = True
                        if therapy == "y":
                            print("Recovery from 1 of the following")
                            print("-Mild hypovolemia (patient given isotonic fluids")
                            print("-Hypopituitarism (patient given glucocorticooids)")
                        else:
                            print("Patient with rapid water consumption?")
                            while error:
                                water = input("y/n? ")
                                error = incorrect_input(water)
                            error = True
                            if water == "n":
                                print("High-fluid, low-protein diet, including:")
                                print("-Beer potomania")
                                print("-Tea and toast diet")
                            else:
                                print("Self-induced water intoxication, including:")
                                print("-Psychogenic polydipsia")
                                print("-Endurance activities (marathon)")
                                print("-Ecstasy use")
                    else:
                        print("What is the urine sodium?")
                        urine_na = int(input(" "))
                        if urine_na <= 40:
                            print("Ensure sodium intake > 150mEq over next 24 hours (infuse 1l of isotonic saline over 1 or more hours)")
                            print("Remeasure urine sodium and osmolality")
                            print("Is Urine Na < 40 and Urine osmolality < 100?")
                            while error:
                                urine = input("y/n? ")
                                error = incorrect_input(urine)
                            error = True
                            if urine == "y":
                                print("Hypovolemic hyponatremia")
                            else:
                                pathway_2()
                        else:
                            pathway_2()

error = True
na = int(input("What is the sodium level? "))
if na >= 135:
    print("The patient does not have hyponatremia.")
else:
    glucose = int(input("What is the glucose level? "))
    na = corrected_sodium(na, glucose)
    if na >=135:
        print("Hyperglycemia induced hyponatremia.")
    else:
        print("Could extra solutes be present in the serum?")
        print("- Is patient postoperative after prostate or uterine surgery?")
        print("- Has the patient received intravenous mannitol or IVIG?")
        while error:
            solutes = input("y/n? ")
            error = incorrect_input(solutes)
        error = True
        if solutes == "y":
            print("What is the serum osmolality?")
            osmolality = int(input(" "))
            if osmolality >= 280:
                print("Isoosmolar or hyperosmolar hyponatremia:")
                print("TURP and hysteroscopy can be associated with absorption of irrigation solutions(glycine, sorbitol)")
                print("Patients with suspected pseudohyponatremia should have sodium measure by direct potentiometry. If normal, measure total proteins and lipids.")
            else:
                pathway_1()
        else:
            pathway_1()
                
print("Thank you")
enter=input("Press enter to exit.")
