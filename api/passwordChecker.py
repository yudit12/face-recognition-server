"""
Password checker
read passwords from given password file you want to check  if they  ever been hacked
return how many time  each password  was  hacked  (using API)

website to check if you ben pwened:
https://haveibeenpwned.com/Passwords

 the  password strength based on k-anonymity k-anonymity
 k-anonymity mean we allows somebody receive information about us with out knowing who we are
 how it's done?
when we requests  password pwend API the requests.get url includes the password, converted to hash furthermore, for more security it add only the first 5 characters of the  result hash password
the response is the all hash password that their beginning  fits to your given password hash beginning
so we get a lot of  fit hash password

*******
hash function-  function that  generates a value of fixed length for each input that it gets
 hashes rules
- one way - given the hash you cant know what the input was
- for the same input the result is always the same hash
- changing one char absolutely changing  the output hash

*******
"""

# print(__doc__)

import requests
import hashlib
import sys

"""
func that request our data and return a response 
"""


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    # print(res)
    if not res.ok:
        raise RuntimeError("Error fetching:{} check the API and try again".format(res.status_code))
    return res


"""
parmeters : the responses hasheses , our hash to check
the responses hasheses are all the hashs that ther beginning fits to our hash and the amount they were leaks 
 return the number of time the hash was leaked 
 if it not  return 0
"""


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print(hashes)
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


""" 
check if password was pwend
create hash password 
run the request_api_data(query_char)  func -> get response 
and return if password was pwend

 """


def pwend_api_check(password):
    # check if password exists in API response
    ## create hash password - hexdigest() convert to hexadecimal string
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_char, left = sha1password[:5], sha1password[5:]
    response = request_api_data(first_five_char)
    # print("response={} request={}".format(response,requests))
    return get_password_leaks_count(response, left)





"""
checks for all given password if  they were leaked 
"""


def passwordChecker(password):

    # password="hellow"
    count = pwend_api_check(password)
    if count:
        print(f'{password} was found {count} times!! you should  change your password!')
        return f'{password} was found {count} times!! you should  change your password!'
    else:
        print(f'{password} was NOT found.you have good strong password keep going! ')
        return f'{password} was NOT found. you have good strong password keep going! '
    # return 'Done'


# if __name__ == "__main__":
#     main(password)
