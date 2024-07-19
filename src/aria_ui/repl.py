
import sys

from utils import convert_html_to_text
from aria_logging_api import log_experiment, log_event, log_dialog_turn, log_user_feedback

RESTART_CMD_STRING = "!RESTART"
USER_PROMPT = "You: "
DS_PROMPT = "Dialog System: "

def request_restart(user_response):
    return user_response.strip() == RESTART_CMD_STRING

def repl(ARDI_API, experiment_id, auth=None):
    def open_connection():
        oc_success = ardi_api.OpenConnection(auth)
        metadata_dict = {'event': 'OpenConnection',
                         'success': str(oc_success)}
        log_event(experiment_id, session_num, adjpair_num, metadata_dict)
        return oc_success
    def start_session():
        ss_success = ardi_api.StartSession()
        metadata_dict = {'event': 'StartSession',
                         'success': str(ss_success)}
        log_event(experiment_id, session_num, adjpair_num, metadata_dict)
        return ss_success
    def close_connection():
        cc_success = ardi_api.CloseConnection()
        metadata_dict = {'event': 'CloseSession',
                         'success': str(cc_success)}
        log_event(experiment_id, session_num, adjpair_num, metadata_dict)
        return cc_success
    welcome_string = \
        f"Welcome to a simple aria dialog system repl! Engage in a dialog.\nEnter the following "\
        f"command to restart your dialog: {RESTART_CMD_STRING}. Press Ctrl+D to exit.\n"
    exit_string = "\nThank you for using a simple aria dialog system repl!"
    ardi_api = ARDI_API()
    #
    session_num = 0
    adjpair_num = 0
    # log experiment metadata
    metadata_dict = {'model_name': ARDI_API.model_name,
                    'api_version': ARDI_API.GetVersion()}
    log_experiment(experiment_id, metadata_dict)
    #
    os_success = open_connection()
    if not os_success:
        print('Cannot establish connection!')
        sys.exit(1)
    #
    session_num += 1
    ss_success = start_session()
    if not ss_success:
        print('Session Start Failed!')
        sys.exit(1)
    print(welcome_string)
    loop = True
    while loop is True:
        try:
            user_response = input(USER_PROMPT)
        except EOFError:
            cc_success = close_connection()
            if not cc_success:
                print('Close Connection Failed!')
            loop = False
            print(exit_string)
            continue
        if request_restart(user_response):
            session_num += 1
            ss_success = start_session()
            if not ss_success:
                print('Session Start Failed!')
                sys.exit(1)
            print(welcome_string)
            continue
        adjpair_num += 1
        llm_response = ardi_api.GetResponse(user_response)
        if not llm_response['success'] is True:
            llm_response_text = '[LLM DID NOT SUCCESSFULLY RESPOND]'
        else:
            llm_response_text = convert_html_to_text(llm_response['response'])
        log_dialog_turn(experiment_id, session_num, adjpair_num, user_response, llm_response)
        print(f'\n{DS_PROMPT}{llm_response_text}\n')

if __name__ == '__main__':
    import uuid
    from aria_dialog_api_team import Team_ARIADialogAPI as ARDI_API
    from utils import get_auth
    try:
        auth = get_auth()
    except ValueError as e:
        print("Exiting")
        sys.exit(1)
    experiment_id = str(uuid.uuid4())
    repl(ARDI_API, experiment_id, auth)
