from email_Process import emailProcess, printMg
emails = ["chuongsuper000@gmail.com", "ffdd@yahoo.com", "convitroi@youtube.com"]
def main():
    for email in emails:
        username, domain = emailProcess(email)
        printMg(username, domain)
#main()
print(type(-10))
