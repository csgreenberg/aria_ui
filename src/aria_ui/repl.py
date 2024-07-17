from sys import exit

RESTART_CMD_STRING = "!RESTART"
USER_PROMPT = "You: "
DS_PROMPT = "Dialog System: "

def request_restart(user_response):
    return user_response.strip() == RESTART_CMD_STRING
def repl(ARDI_API, auth=None):
    welcome_string = \
        f"Welcome to a simple aria dialog system repl! Engage in a dialog.\nEnter the following "\
        f"command to restart your dialog: {RESTART_CMD_STRING}. Press Ctrl+D to exit.\n"
    exit_string = "\nThank you for using a simple aria dialog system repl!"
    ardi_api = ARDI_API()
    if not ardi_api.OpenConnection(auth):
        print('Cannot establish connection!')
        exit(1)
    if not ardi_api.StartSession():
        print('Session Start Failed!')
        exit(1)
    print(welcome_string)
    loop = True
    while loop is True:
        try:
            user_response = input(USER_PROMPT)
        except EOFError:
            ardi_api.CloseConnection()
            loop = False
            print(exit_string)
            continue
        if request_restart(user_response):
            if not ardi_api.StartSession():
                print('Session Start Failed!')
                exit(1)
            print(welcome_string)
            continue
        llm_response = ardi_api.GetResponse(user_response)
        print(f'\n{DS_PROMPT}{llm_response}\n')

if __name__ == '__main__':
    from aria_dialog_api_team import Team_ARIADialogAPI as ARDI_API
    from utils import get_auth
    try:
        auth = get_auth()
    except ValueError as e:
        print("Exiting")
        exit(1)
    repl(ARDI_API, auth)