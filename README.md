This is a simple example of the implementation and use of the ARIA dialog API.

The abstract base class to inherit and implement can be found here:
[src/aria_dialog_api/aria_dialog_api_base.py](src/aria_dialog_api/aria_dialog_api_base.py)

You can find an example implementation, using a local installation of llama2 here:
[src/aria_dialog_api/aria_dialog_api_local_lamma.py](src/aria_dialog_api/aria_dialog_api_local_lamma.py)

To run the text-basd (REPL) interface, execute the python script [src/aria_dialog_api/run_repl.py](src/aria_dialog_api/run_repl.py)
Note that, when using the REPL with llama2, you need to use `torchrun` or `python -m torch.distributed.launch`.
E.g., `python -m torch.distributed.launch run_repl.py`

To run the UIUX, execute: `ARIA_AUTH_JSON='{}' streamlit run app.py`.

To deploy the UIUX do the following:
- Get an API key for Posit Connect "POSIT_API"
- cd into src/aria_dialog_api
- Define the Post Connect Server: 1rsconnect add --server https://miganalytics.nist.gov  --name miganalytics --api-key POSIT_API`
- execute: `rsconnect deploy streamlit -N -t uiux-parrot -n miganalytics  .`