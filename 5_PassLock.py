#! python3

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
			 
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1].lower()      # first command line arg is the account name

if account in PASSWORDS.keys():
	pyperclip.copy(PASSWORDS[account])
	print('Password for '+ account + ' is copied to clipboard')
	print(pyperclip.paste())
else:
	print('there is no such account')