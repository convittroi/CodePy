
def emailProcess(email):
    username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    #print(f"Your username is {username}")
    return[username, email_domain]

def printMg(username, email_domain):
    print(f"""Your username is: {username}
Your domain is {email_domain} """)


def main():
    email = input("Please enter your email: ").strip()
    username,email_domain= emailProcess(email)
    printMg(username, email_domain)



if __name__=="__main__":
    main()

