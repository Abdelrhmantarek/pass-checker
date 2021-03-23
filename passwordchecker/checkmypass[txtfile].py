import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()#converts the hashed password to a string of double length containing only hexadecimal digits
    first5_char,tial = sha1password[:5], sha1password[5:]# store the first 5 characters in the first variable, and the reamining characters in the second variable
    response=request_api_data(first5_char)# call request API data and pass the first 5 characters
    # print(response)
    return get_password_leaks_count(response,tial)

def main():
    with open('pass.txt',mode='r') as file:
        password_lst = file.readlines()
        for password in password_lst:
            # print('heeey',password[:-1])
            passy = password[:-1]
            count = pwned_api_check(passy)
            if count:
                print(f'{password} was found {count} times... you should probably change your password')
            else:
                print(f'{password} was Not found. carry on!')
        return 'done!!!!'

if __name__=='__main__':
    sys.exit(main())