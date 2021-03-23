import requests
import hashlib
import sys

# k-anonymity technique
# K-anonymity allows somebody to receive information about us yet still not know who we are

# this API allows us to actually trust no one, that is we only trust ourselves and we're only going to give the bits of information that we feel comfortable to the API so that it gives us a response with some data

def request_api_data(query_char): # pass the hashed version of the password, request the data and give a response
    url = 'https://api.pwnedpasswords.com/range/'+ query_char# uses k-anonymity, matches passwords with first 5 characters of hashed password (SHA1)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')# raise an error if no status 200
    return res

# reading the response
def get_password_leaks_count(hashes,hash_to_check):# loops through the hash and count, check if any matches (how many times the password has been leaked
    # tuple comprehension
    hashes=(line.split(':') for line in hashes.text.splitlines())
    # h->> refer to the hash tail that we get from the response
    # hash_to_check->> refers to our tail
    for h,count in hashes:
        if h==hash_to_check:# tail end of the hashed password
            # return how many times this password has been leaked
            return count# how many times the password has been leaked
        # otherwise just return 0
    return 0

# check password if it exists in API response
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()#converts the hashed password to a string of double length containing only hexadecimal digits
    first5_char,tial = sha1password[:5], sha1password[5:]# store the first 5 characters in the first variable, and the reamining characters in the second variable
    response=request_api_data(first5_char)# call request API data and pass the first 5 characters
    # print(response)
    return get_password_leaks_count(response,tial)

# main function that receives the arguments[which is the passwords that we want to check]

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'{password} was Not found. carry on!')
    return 'done!!!!'

# main-module
if __name__=='__main__': # only run this file from the command line, not if imported in
    sys.exit(main(sys.argv[1:])) # exit the process and get the return value from main
    
    

'''
better idea to enhance the program:
read passwords from a test file instead of just from the command line
because in the command line your commands will be saved somewhere ;)
'''