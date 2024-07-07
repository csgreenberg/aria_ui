#
from repl import repl

# import API implementation
from aria_dialog_api_parrot import Parrot_ARIADialogAPI as ARDI_API
# define auth used by API implementation
auth = None
#

repl(ARDI_API, auth)

