email_name = input("please enter your email :").strip()
user_name = email_name[:email_name.index('@')]
domain_name = email_name[email_name.index('@')+1:]

print(f"your user name is '{user_name}'", '\n' f"your domain name is '{domain_name}'")