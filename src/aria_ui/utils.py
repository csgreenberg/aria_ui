"""ARIA Interface and Logging Utils

This file can be imported as a module and contains utilities for interfacing apps and
logging, consisting of the following classes and function(s):

    * get_auth - runs the repl loop interfacing the user with the chatbot
    * convert_text_to_html
    * convert_html_to_text
    * class JsonFormatter
"""
import os
import json
import html
import logging

def get_auth(auth_env_var='ARIA_AUTH_JSON'):
    """Gets json string from environmental variable named auth_env_var.

    Parameters
    ----------
    auth_env_var : str, optional
        the name of the environmental variable storing a json string indicating authorization and
        other information.

    Returns
    -------
    dict
        a mapping from authorization attribute names to attribute values, e.g.,
        {"api_key":api_key_value_string}
    """
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
    """Converts text to lightweight html.

    Parameters
    ----------
    text : str
        the text to be converted to html

    Returns
    -------
    str
        a string of html corresponding to the input text
    """
    htmltext = "<!DOCTYPE html> <pre>"
    for line in text.splitlines():
        line = html.escape(line)
        htmltext += (line + '<br>')
    htmltext = htmltext[:-len('<br>')]
    htmltext += '</pre>'
    return htmltext
def convert_html_to_text(htmltext):
    """Converts text to lightweight html.

    Parameters
    ----------
    htmltext : str
        the html to be converted to text

    Returns
    -------
    str
        a string of text corresponding to the input html
    """
    text = htmltext[len("<!DOCTYPE html> <pre>"):-len('</pre>')]
    text = html.unescape(text)
    text = text.replace('<br>', '\n')
    return text

####
# the following code is adopted from:
# https://stackoverflow.com/questions/50144628/python-logging-into-file-as-a-dictionary-or-json
#

class JsonFormatter(logging.Formatter):
    """
    Formatter that outputs JSON strings after parsing the LogRecord.

    @param dict fmt_dict: Key: logging format attribute pairs. Defaults to {"message": "message"}.
    @param str time_format: time.strftime() format string. Default: "%Y-%m-%dT%H:%M:%S"
    @param str msec_format: Microsecond formatting. Appended at the end. Default: "%s.%03dZ"
    """

    def __init__(self, fmt_dict: dict = None, time_format: str = "%Y-%m-%dT%H:%M:%S",
                 msec_format: str = "%s.%03dZ"):
        self.fmt_dict = fmt_dict if fmt_dict is not None else {"message": "message"}
        self.default_time_format = time_format
        self.default_msec_format = msec_format
        self.datefmt = None

    def usesTime(self) -> bool:
        """
        Overwritten to look for the attribute in the format dict values instead of the fmt string.
        """
        return "asctime" in self.fmt_dict.values()

    def formatMessage(self, record) -> dict:
        """
        Overwritten to return a dictionary of the relevant LogRecord attributes instead of a string.
        KeyError is raised if an unknown attribute is provided in the fmt_dict.
        """
        return {fmt_key: record.__dict__[fmt_val] for fmt_key, fmt_val in self.fmt_dict.items()}

    def format(self, record) -> str:
        """
        Mostly the same as the parent's class method, the difference being that a dict is manipulated and dumped as JSON
        instead of a string.
        """
        record.message = record.getMessage()

        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        message_dict = self.formatMessage(record)

        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)

        if record.exc_text:
            message_dict["exc_info"] = record.exc_text

        if record.stack_info:
            message_dict["stack_info"] = self.formatStack(record.stack_info)

        return json.dumps(message_dict, default=str)
##
##
####