# FILE LOADING


def load_common_pin_file(filename):
    try:
        with open(filename, "r") as file:
            pins = {line.strip() for line in file if line.strip()}
        return pins
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in the current directory.")
        return set()
    except Exception as e:
        print(f"An error occurred while loading the MPINs: {e}")
        return set()


# Demographic Checking


def extract_pin_patterns_from_date(date_str, length):
    patterns = set()
    try:
        day, month, year = date_str.split("-")
    except:
        return patterns

    dd = day.zfill(2)
    mm = month.zfill(2)
    yyyy = year.zfill(4)
    yy = yyyy[-2:]

    if length == 4:
        patterns.update([
            dd + mm, mm + dd,
            yy + mm, mm + yy,
            dd + yy, yy + dd
        ])
    elif length == 6:
        patterns.update([
            dd + mm + yy, mm + dd + yy, yy + mm + dd,
            dd + yy + mm, mm + yy + dd, yy + dd + mm,
            dd + mm + yyyy[-2:], mm + dd + yyyy[-2:],
            yyyy + mm, yyyy + dd,
            mm + yyyy, dd + yyyy 
        ])

    return patterns



# Strength Evaluation
def evaluate_mpin_strength(pin, common_pin_set, dob_self, dob_spouse, anniversary):
    reasons = []
    pin_length = len(pin)

    if pin in common_pin_set:
        reasons.append("COMMONLY_USED")
    if pin in extract_pin_patterns_from_date(dob_self, pin_length):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if pin in extract_pin_patterns_from_date(dob_spouse, pin_length):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if pin in extract_pin_patterns_from_date(anniversary, pin_length):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"
    return strength, reasons
