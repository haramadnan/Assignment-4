def seconds_in_year(days=365):
    """Yeh function ek saal ke total seconds calculate karega"""
    seconds = days * 24 * 60 * 60  # Days → Hours → Minutes → Seconds
    return seconds

# Normal year (365 days)
normal_year_seconds = seconds_in_year()
print(f"Seconds in a normal year (365 days): {normal_year_seconds}")

# Leap year (366 days)
leap_year_seconds = seconds_in_year(366)
print(f"Seconds in a leap year (366 days): {leap_year_seconds}")