
import os
import json
import html
def get_auth(auth_env_var='ARIA_AUTH_JSON'):
    auth_json = os.getenv(auth_env_var)
    auth = {}  ### The default
    if (auth_json is not None):
        try:
            auth = json.loads(auth_json)
        except ValueError as e:
            print(f"Error parsing JSON string /{auth_json}/ error {e}.")
            raise
    return auth
def convert_text_to_html(text):
    htmltext = "<!DOCTYPE html> <pre>"
    htmltext += html.escape(text)
    htmltext += '</pre>'
    return htmltext