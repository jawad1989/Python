"""
Input:
    python check_pass.py admin jawa jhbbb88hby8bh

Output:
    total records: 579 
    found, 51040 times        
    for admin result is: 51040

    total records: 594 
    found, 1146 times       
    for jawa result is: 1146

    total records: 564 
    for jhbbb88hby8bh result is: 0

Notes:
    haveibeenpwned.com
    kanimity: send but anonymously
    https://passwordsgenerator.net/sha1-hash-generator/ => to get first 5 chars 
""" 

import requests
import sys
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    # print(dir(res))
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, try again')
    else:
        return res


def read_response(response):
    nlines = response.text.count('\n')
    print(f"total records: {nlines} ")


def get_password_leaks_count(hashes, hash_to_check):
    hashes = ( line.split(':') for line in hashes.text.splitlines() )
    
    for h, count in hashes:
        if h == hash_to_check:
            print(f"found, {count} times")
            return count
    return 0

def pwned_api_check(password):
    # check if password exists in API
    sh1password        = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sh1password[:5], sh1password[5:]
    response           = request_api_data(first5_chars)
    read_response(response)

    return get_password_leaks_count(response, tail)
     

def main(passwords):
    for p in passwords:
        result = pwned_api_check(p)
        print(f"for {p} result is: {result}\n")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))