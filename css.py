CorrectUsername = "ali"
CorrectPassword = "sher"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[1;93mTool Username \x1b[1;93m»» \x1b[1;96m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[1;93mTool Password \x1b[1;93m»» \x1b[1;96m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://smmpanelpk.com')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://smmpanelpk.com')

def login():
	os.system('clear')
	try:
			br.open('https://m.facebook.com')
	except mechanize.URLError:
		print"\n\x1b[1;91mThere is no internet connection"
