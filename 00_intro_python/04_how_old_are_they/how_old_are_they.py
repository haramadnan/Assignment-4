def calculate_ages():
    # Ali's age is given as 25 years old
    ali = 25

    # Bilal is 5 years younger than Ali
    bilal = ali - 5

    # Clara is twice as old as Bilal
    clara = 2 * bilal

    # Daniyal is the sum of Ali and Bilal's ages
    daniyal = ali + bilal

    # Eman is the average of Ali and Clara's ages
    eman = (ali + clara) // 2  # Using // for integer division

    # Print out all of the ages!
    print("Ali is", ali, "years old.")
    print("Bilal is", bilal, "years old.")
    print("Clara is", clara, "years old.")
    print("Daniyal is", daniyal, "years old.")
    print("Eman is", eman, "years old.")

# Calling the function
calculate_ages()