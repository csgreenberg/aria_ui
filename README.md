This is a simple example of the implementation and use of the ARIA dialog API.

The abstract base class to inherit and implement can be found here:
[src/aria_dialog_api/aria_dialog_api_base.py](src/aria_dialog_api/aria_dialog_api_base.py)

You can find an example implementation for a simple echo app here:
[src/aria_dialog_api/aria_dialog_api_team.py](src/aria_dialog_api/aria_dialog_api_team.py)
Note that different branches might have different implementations of the api, and an example 
for Gemini can be found in ada_auth_gemini branche.

To run the text-basd (REPL) interface, execute the python script [src/aria_dialog_api/repl.py](src/aria_dialog_api/repl.py)

To run the UIUX, execute: `ARIA_AUTH_JSON='{}' streamlit run app.py`.

