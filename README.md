# Task: To create a basic tool for brute-forcing usernames and passwords in Python

# Submitted By RASHMIKA R S 

## WORKING IN A NUTSHELL:-
- Open the target.com website and navigate to the login page.
- Simultaneously, launch the Burp Suite software to intercept the target website.
- Activate Burp Suite's Proxy Mode to capture and store keystrokes.
- With Burp Suite ready, enter your credentials on the target website as you normally would.
- Burp Suite will record your login attempt, including captured keystrokes.
- Extract the captured credentials from Burp Suite using your Brute.py Python script.
- Pass the target website URL and Burp Suite proxy address to the script to locate the captured credentials.
- Import a text file containing a list of usernames and passwords into the script.
- The script will systematically try each username/password combination until it finds the correct one.
- This automated trial-and-error approach of guessing all possible combinations is known as brute-forcing.

## WORKING SCREENSHOTS:-

### Burp Suit's Proxy Window:

![burp-proxy-intercept](https://github.com/Cipher-unhsiV/Prudent-Vishnu/assets/121817913/bc6bcd54-6998-4cae-8987-063b4b2d2041)

### Credential Interception:

![burp-creds](https://github.com/Cipher-unhsiV/Prudent-Vishnu/assets/121817913/609e3799-a1e7-4fa2-8846-fac96d14c776)

### Directory Structure:

![dir-structure](https://github.com/Cipher-unhsiV/Prudent-Vishnu/assets/121817913/603391a9-2b5e-4e97-84df-4f7a23c85bcf)

### Credentials.txt - Text File:

![creds](https://github.com/Cipher-unhsiV/Prudent-Vishnu/assets/121817913/71d1c2a9-28bb-4b04-9e32-d4802259a20f)

### Brute.py - Python Script:

![code](https://github.com/Cipher-unhsiV/Prudent-Vishnu/assets/121817913/04d49e72-d0b1-436a-9bd9-0d457a511fe2)

### Final Output:

![output](https://github.com/Cipher-unhsiV/Prudent-Vishnu/assets/121817913/dced0ee9-a138-4d8b-87bf-fd466590245e)
