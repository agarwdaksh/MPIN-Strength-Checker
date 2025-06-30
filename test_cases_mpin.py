from main import evaluate_mpin_strength, load_common_pin_file

# Load both 4-digit and 6-digit commonly used PINs
common_pins_4 = load_common_pin_file("Commonly_Used_Pins.txt")
common_pins_6 = load_common_pin_file("Commonly_Used_Pin_6.txt")

# Unique and realistic test cases for MPIN strength checking
test_cases = [
    # 4-digit MPINs
    (
        "0912",
        "09-12-1997",
        "15-07-1994",
        "20-11-2020",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SELF"],
    ),
    (
        "1507",
        "01-01-1990",
        "15-07-1994",
        "10-10-2010",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SPOUSE"],
    ),
    (
        "2011",
        "03-03-1985",
        "04-04-1986",
        "20-11-2020",
        "WEAK",
        ["COMMONLY_USED", "DEMOGRAPHIC_ANNIVERSARY"],
    ),
    ("7474", "10-10-1999", "11-11-1998", "12-12-1997", "STRONG", []),
    (
        "0101",
        "01-01-1991",
        "01-01-1992",
        "01-01-1993",
        "WEAK",
        [
            "COMMONLY_USED",
            "DEMOGRAPHIC_DOB_SELF",
            "DEMOGRAPHIC_DOB_SPOUSE",
            "DEMOGRAPHIC_ANNIVERSARY",
        ],
    ),
    ("8282", "05-05-2000", "06-06-2001", "07-07-2002", "STRONG", []),
    (
        "2022",
        "22-02-2020",
        "23-03-2021",
        "24-04-2022",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SELF"],
    ),
    (
        "0412",
        "04-12-1999",
        "05-12-1998",
        "06-12-1997",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SELF"],
    ),
    (
        "2405",
        "24-05-1999",
        "01-01-2000",
        "02-02-2001",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SELF"],
    ),
    ("0908", "09-01-1990", "16-02-1991", "17-08-1992", "STRONG", []),
    (
        "3112",
        "31-12-1999",
        "01-01-2000",
        "02-02-2001",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SELF"],
    ),
    # 6-digit MPINs
    (
        "091297",
        "09-12-1997",
        "15-07-1994",
        "20-11-2020",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SELF"],
    ),
    (
        "150794",
        "01-01-1990",
        "15-07-1994",
        "10-10-2010",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SPOUSE"],
    ),
    (
        "201120",
        "03-03-1985",
        "04-04-1986",
        "20-11-2020",
        "WEAK",
        ["DEMOGRAPHIC_ANNIVERSARY"],
    ),
    ("004426", "31-12-2000", "30-12-1999", "29-12-1998", "STRONG", []),
    (
        "198907",
        "07-08-1988",
        "10-10-1990",
        "11-11-1991",
        "STRONG",
        [],
    ),
    (
        "101090",
        "12-12-2000",
        "10-10-1990",
        "01-01-2010",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SPOUSE"],
    ),
    (
        "030405",
        "30-01-1980",
        "20-02-1981",
        "01-01-2020",
        "WEAK",
        ["COMMONLY_USED"],
    ),
    (
        "199001",
        "01-01-1990",
        "02-02-1992",
        "03-03-1993",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SELF"],
    ),
    ("090825", "08-08-1999", "09-09-1998", "10-10-1997", "STRONG", []),
    (
        "202020",
        "01-01-1991",
        "20-20-2020",
        "01-01-1993",
        "WEAK",
        ["DEMOGRAPHIC_DOB_SPOUSE"],
    ),
    (
        "101010",
        "01-01-1990",
        "02-02-1991",
        "10-10-2010",
        "WEAK",
        ["COMMONLY_USED", "DEMOGRAPHIC_ANNIVERSARY"],
    ),
]


def run_tests():
    total = len(test_cases)
    passed_count = 0

    for i, (
        pin,
        dob_self,
        dob_spouse,
        anniv,
        expected_strength,
        expected_reasons,
    ) in enumerate(test_cases, 1):
        # Select appropriate pin set based on length
        common_set = common_pins_4 if len(pin) == 4 else common_pins_6
        actual_strength, actual_reasons = evaluate_mpin_strength(
            pin, common_set, dob_self, dob_spouse, anniv
        )
        passed = (actual_strength == expected_strength) and (
            sorted(set(actual_reasons)) == sorted(set(expected_reasons))
        )

        if passed:
            passed_count += 1

        print(f"Test {i:02d}: {'✅ PASSED' if passed else '❌ FAILED'}")
        print(f"   MPIN: {pin}")
        print(f"   DOB_SELF: {dob_self}, SPOUSE: {dob_spouse}, ANNIV: {anniv}")
        print(f"   Expected: {expected_strength}, {expected_reasons}")
        print(f"   Actual:   {actual_strength}, {actual_reasons}\n")

    print("📊 Summary")
    print(f"✅ Passed: {passed_count}/{total}")
    print(f"❌ Failed: {total - passed_count}/{total}")


if __name__ == "__main__":
    run_tests()
