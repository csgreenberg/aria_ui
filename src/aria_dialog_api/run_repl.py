#
from repl import repl
import os

# import API implementation
from aria_dialog_api_auth_gemini import AuthGemini_ARIADialogAPI as ARDI_API
# define auth used by API implementation
AUTH_ENV_VAR = 'API_KEY'
auth = {'api_key': os.getenv(AUTH_ENV_VAR)}
#

repl(ARDI_API, auth={'api_key': os.getenv(AUTH_ENV_VAR)})