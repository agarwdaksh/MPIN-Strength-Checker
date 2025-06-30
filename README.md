# 📌 MPIN Strength Checker

## 🔐 What is MPIN?
MPIN (Mobile Banking Personal Identification Number) is a 4 to 6-digit passcode that users set up to securely access mobile banking apps and authorize financial transactions like: 
 - Checking account balance 
 - Transferring funds
 - Paying bills 
 - Mobile recharges, etc.

This project evaluates the strength of a user's 4-digit or 6-digit MPIN (Mobile PIN) used in mobile banking applications. It flags MPINs that are either commonly used or based on the user's demographic data, such as: 
 - Date of Birth (DOB)
 - Spouse’s DOB
 - Wedding Anniversary
The goal is to identify MPINs that are weak and easily guessable, thereby promoting safer PIN creation habits among users.

## ✅ Features
 - Supports both 4-digit and 6-digit MPINs.
 - Detects weak PINs based on:
   - Commonly used PIN datasets (loaded from `.txt` files).
   - Matches with user demographic data in various combinations (`ddmm`, `mmdd`, `yymmdd`, etc.).
 - Return:
   - Strength: `STRONG` or `WEAK`  
   - Reasons for weak MPINs:
     - `COMMONLY_USED`
     - `DEMOGRAPHIC_DOB_SELF`
     - `DEMOGRAPHIC_DOB_SPOUSE`
     - `DEMOGRAPHIC_ANNIVERSARY`
 - Has **22 diverse test cases**, covering edge casesas well

## 🧪 Test Case Design
This project includes 22 carefully selected test cases (both 4-digit and 6-digit PINs) designed to validate all important functional and edge scenarios.
Here’s a breakdown of why these specific test cases were chosen:

### ✅ 1. Coverage for All Demographic Checks
 - Each of the following is tested:
   - `DEMOGRAPHIC_DOB_SELF`
   - `DEMOGRAPHIC_DOB_SPOUSE`
   -`DEMOGRAPHIC_ANNIVERSARY`
 - Some cases match only one demographic, while others match all the three.

### ✅ 2. Real-World Weak PIN Patterns
Includes common, easily guessable patterns such as:
 - `"2022"`, `"101010"`
 - These test the detection of `COMMONLY_USED` even when demographics do not match.

### ✅ 3. Edge Cases for Pattern Variants
 - Patterns such as `ddmm`, `mmdd`, `ddmmyy`, `yymmdd`, etc., are all covered through different combinations.
 - Helps validate the logic inside `extract_pin_patterns_from_date()`.

### ✅ 4. Random Strong PINs
 - Cases like `"7474"`, `"8282"`, `"004426"`, `"090825"` do not match common PINs or demographics.
 - Ensure that genuinely strong PINs are not falsely treated as weak.

## 📁 File Structure
| File                      | Purpose                                 |
| ------------------------- | --------------------------------------- |
| `main.py`                 | Contains functions for test case evaluation |
| `Mpin_Checking.ipynb`     | Jupyter notebook with interactive flow  |
| `test_cases_mpin.py`      | 22 test cases with automated validation |
| `Commonly_Used_Pins.txt`  | 4-digit commonly used PINs list         |
| `Commonly_Used_Pin_6.txt` | 6-digit commonly used PINs list         |

## ⭕ No Hardcoding Used
 - All commonly used PINs are dynamically loaded from external `.txt` files.
 - All demographic inputs are user-driven or test-provided.
 - Logic is generic and scalable.

