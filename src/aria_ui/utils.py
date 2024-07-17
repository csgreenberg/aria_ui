
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
    for line in text.splitlines():
        line = html.escape(line)
        htmltext += (line + '<br>')
    htmltext += '</pre>'
    return htmltext

def convert_html_to_text(htmltext):
    text = htmltext.lstrip("<!DOCTYPE html> <pre>").rstrip('</pre>')
    text = html.unescape(text)
    text = text.replace('<br>', '\n')
    return text


if __name__=='__main__':
    with open('/tmp/x.txt') as f:
        text = f.read()
        htmltext = convert_text_to_html(text)
        print(htmltext)
        with open('/tmp/y.html', 'w') as g:
            g.write(htmltext)