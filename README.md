<div align="center"> <video src="https://github.com/user-attachments/assets/11eaf4a9-b8be-4bdd-b163-6b66c7245f97" width="100%" autoplay loop muted></video> 
  <p><i>Real-time Password strength checker </i></p></div>

# Password Strength Checker 

A lightweight, interactive Python command-line tool that evaluates password strength based on industry-standard security complexity metrics. This project demonstrates foundational concepts in secure coding, regular expressions, and user input validation.

## Security Features & Criteria

The tool analyzes input strings against a strict validation pipeline to ensure resistance against dictionary and brute-force attacks:

* **Length Check:** Validates a minimum of 8 characters.
* **Numeric Density:** Ensures at least one numerical digit (`0-9`) is present.
* **Casing Diversity:** Requires a combination of uppercase (`A-Z`) and lowercase (`a-z`) characters.
* **Special Characters:** Utilizes regex pattern matching to enforce inclusion of symbols (e.g., `!@#$%^&*`).

## Getting Started

### Prerequisites
* Python 3.x installed on your system.

### Installation & Execution
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the project directory:
   ```bash
   cd YOUR_REPOSITORY_NAME
   ```
3. Run the script:
   ```bash
   python password_checker.py
   ```

## Usage Example

```text
Enter your password: mypassword
Weak: password must contain at least one digit

Enter your password: Mypassword1
Weak: password must contain 2at least one special character

Enter your password: P@ssword123!
Strong: password is strong!

Enter your password: exit
Exiting password checker.

https://github.com/user-attachments/assets/d78d2462-81f5-470c-a8df-07a6b65b6ebf


```

## Built With
* **Python 3** - Core programming language.
* **re Module** - Python's built-in regular expression library for advanced pattern matching.




