from aria_dialog_api_local_lamma import LocalLlama_ARIADialogAPI as ARDI_API

RESTART_CMD_STRING = "!RESTART"
USER_PROMPT = "You: "
DS_PROMPT = "Dialog System: "

def request_restart(user_response):
    return user_response.strip() == RESTART_CMD_STRING
def repl(auth=None):
    welcome_string = \
        f"Welcome to a simple aria dialog system repl! Engage in a dialog.\nEnter the following "\
        "command to restart your dialog: {RESTART_CMD_STRING}. Press Ctrl+D to exit.\n"
    exit_string = "\nThank you for using a simple aria dialog system repl!"
    ardi_api = ARDI_API()
    ardi_api.OpenSession(auth)
    print(welcome_string)
    exit = False
    while exit is False:
        try:
            user_response = input(USER_PROMPT)
        except EOFError:
            ardi_api.CloseSession(destroy_generator=True)
            exit = True
            print(exit_string)
            continue
        if request_restart(user_response):
            ardi_api.CloseSession()
            ardi_api.OpenSession(auth)
            print(welcome_string)
            continue
        llm_response = ardi_api.GetResponse(user_response)
        print(f'\n{DS_PROMPT}{llm_response}\n')

if __name__ == '__main__':
    repl()

