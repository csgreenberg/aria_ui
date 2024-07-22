import json
import rsa
import os
import streamlit as st
from streamlit_javascript import st_javascript
from urllib.parse import urlparse
from urllib.parse import parse_qs

##################################################################
### Look for USER ID via <URL>/?userid=302-billy&sessionid=9001
### eg. https://miganalytics.nist.gov/content/_w_17dee71660904e73a999171242da7d3e/85f12516-a979-4ce1-9c0c-4ea3c821e12e/?userid=2954-022
def extract_param_from_url(param):
    url = st_javascript("await fetch('').then(r => window.parent.location.href)")
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    if (param in query_dict):
        return(query_dict[param][0])
    return("")

#################################################################
#### get the auth json string used by API implementation
def get_env_json_as_dict(env_var):
    json_str = os.getenv(env_var)
    dic = {}  ### The default
    if (json_str is not None):
        try:
            dic = json.loads(json_str)
        except ValueError as e:
            print(f"Error parsing JSON string /{json_str}/ error {e}.")
            print("Aborting")
            exit(1)
    return(dic)

#################################################################
#### get the auth json string used by API implementation
def get_env_string(env_var):
    env_str = os.getenv(env_var)
    if (env_str is None):
        return("")
    return(env_str)


#################################################################
###    Info Generator tools
#################################################################

#### The INFO String Definition
### <STATE>:<EVALMODE>:<USERID>:<ASSIGNMENT>
#### <STATE>: ARIA UI States of operation
#       DISABLED [default] = info string is empty or not parsable.
#       DEBUG = This runs the application but saves no logs
#       DEBUGTEXT = This runs the application but saves logs as TEXT
#       DEBUGDB = This runs the application but saves logs to the DB
#       LIVE = This runs the application and saves logs
### <EVALMODE>: the ARIA evaluation mode
#       model = run as a model tester
#       redteam = ruun as a red teamer
#       field = run as a field tester
### <USERID>: The string of the USER ID
### <ASSIGNMENTID>: The string of the ASSIGNMENT ID

#################################################################
#### get the unique assignment id for this application exec.
def get_assignment_id(user_id):
    pid = os.getpid()
    return(f"{user_id}_{datetime.today().strftime('%Y-%m-%d')}-{pid:07d}")

#################################################################
#### build the information string
def build_info_str(state, user_id, eval_mode):
    return(f"{state}:{eval_mode}:{user_id}:{get_assignment_id(user_id)}")

#################################################################
#### build the information string
def parse_info_str(info_str):
    states = ['DISABLED', 'DEBUG', 'DEBUGTEXT', 'DEBUGDB', 'LIVE']
    eval_modes = ['model', 'redteam', 'field']

    if (info_str == ""):
        return(["DISABLED", "", "", ""])
    
    info_arr = info_str.split(':')
    
    if (len(info_arr) != 4):
        print(f"Error: info string /{info_str}/ requires four values: <STATE>:<EVALMODE>:<USERID>:<ASSIGNMENT> but {len(info_arr)} where found.  Aborting.")
        exit(1)
    state, eval_mode, user_id, assignment = info_arr
    if (state not in states):
        print(f"Error: The state /{state}/ in info string /{info_str}/ is not one of {states}. Aborting")
        exit(1)
    if (eval_mode not in eval_modes):
        print(f"Error: The eval_mode /{eval_mode}/ in info string /{info_str}/ is not one of {eval_modes}. Aborting")
        exit(1)
    return([state, eval_mode, user_id, assignment])

#################################################################
#### encrypt the info str with the passed public key
def encrypt_info_str(info_str, public_key):
    return(rsa.encrypt(info_str.encode(), public_key))

#################################################################
#### decrypt the info str with the passed private key
def decrypt_info_str(enc_info_str, private_key):
    if (private_key is None):
        print(f"Error: Attempd to decrypt {enc_info_str} failed.  Private key object is None")
        exit(1)
        
    return(rsa.decrypt(bytes.fromhex(enc_info_str), private_key).decode())

#################################################################
#### make a public key object from the dictionary
def make_PublicKey(dic):
    if (len(dic) == 0):
        return(None)
    for v in ['n', 'e']:
        if (v not in dic):
            print(f"Error: Can not make a public key from the dictionary.  Missing the {v} variable. Aborting")
            exit(1)
    return(rsa.PublicKey(dic['n'], dic['e']))

#################################################################
#### make a private key object from the dictionary
def make_PrivateKey(dic):
    if (len(dic) == 0):
        return(None)
    for v in ['n', 'e', 'd', 'p', 'q']:
        if (v not in dic):
            print(f"Error: Can not make a private key from the dictionary.  Missing the {v} variable. Aborting")
            exit(1)
    return(rsa.PrivateKey(dic['n'], dic['e'], dic['d'], dic['p'], dic['q']))

#################################################################
#### build NEW public/private keys pair and returns two dictionaries
def make_public_private_envs():
    publicKey, privateKey = rsa.newkeys(512)
    pub =  json.dumps({"n": publicKey.n, "e": publicKey.e}, separators=(',', ':'))
    priv = json.dumps({"n": privateKey.n, "e": privateKey.e, "d": privateKey.d, "p": privateKey.p, "q": privateKey.q}, separators=(',', ':'))

    
    enc = encrypt_info_str("DEBUG:model:user1:assignment1", publicKey).hex()
    print(f"export ARIA_UI_PUBLIC_KEY_JSON='{pub}'")
    print(f"export ARIA_UI_PRIVATE_KEY_JSON='{priv}'")
    print("export ARIA_AUTH_JSON='{}'")
    print(f"echo DEBUG model testing URL: ")
    print(f"echo http://localhost:8501/?info={enc}")
    
    print("streamlit run app.py")

    

