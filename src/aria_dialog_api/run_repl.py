#
from repl import repl

# import API implementation
from aria_dialog_api_team import Team_ARIADialogAPI as ARDI_API
# define auth used by API implementation
auth = None
#

repl(ARDI_API, auth)

