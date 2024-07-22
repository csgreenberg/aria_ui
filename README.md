This is a simple example of the implementation and use of the ARIA dialog API.

The abstract base class to inherit and implement can be found here:
[src/aria_dialog_api/aria_dialog_api_base.py](src/aria_dialog_api/aria_dialog_api_base.py)

You can find an example implementation, using a local installation of llama2 here:
[src/aria_dialog_api/aria_dialog_api_local_lamma.py](src/aria_dialog_api/aria_dialog_api_local_lamma.py)

To run the text-basd (REPL) interface, execute the python script
[src/aria_dialog_api/run_repl.py](src/aria_dialog_api/run_repl.py)
Note that, when using the REPL with llama2, you need to use `torchrun`
or `python -m torch.distributed.launch`.  E.g., `python -m
torch.distributed.launch run_repl.py`

The ARIA-UI can be ran locally displaying the application using
localhost or as a deployed application on the NIST web servers. The
ARIA UI is passed configuration content via environment variables and
from parameters passed in the URL.

To run the UI locally passing the all information through the environment, execute the following:

   export ARIA_AUTH_JSON='{}'
   export ARIA_INFO_STRING="DEBUG:model:user1:assignment1"
   streamlit run app.py

To run the UI locally passing information via environment variable and
using URL parameters, execute the following.  The public and private
keys are for demo purpospes only.  The production versions will be
protected.

   export ARIA_UI_PUBLIC_KEY_JSON='{"n":10797705934091413540198339178373907290400599746071759106332241718571089694921142884142532031553383889483949672305899567006279245665646025164184447853469109,"e":65537}'
   export ARIA_UI_PRIVATE_KEY_JSON='{"n":10797705934091413540198339178373907290400599746071759106332241718571089694921142884142532031553383889483949672305899567006279245665646025164184447853469109,"e":65537,"d":7725804151264393605550765533245483630032881018246134672232959681816920787232170322324461966338743935389055682959490230210490866926733651030613949197719553,"p":7280719219472190143552113172630997207817632095389599140799995129824916690055165569,"q":1483054847825073043612473442605726500506364060641106340029335436963812661}'
   export ARIA_AUTH_JSON='{}'

   streamlit run app.py

   Use the URL: 
      http://localhost:8501/?info=c66a489ca66d308a4a353ad724b9158a0e6e9618e94a717df3d8adc7e946dd0fd692fcd5c92b6035e3d8661746518dbaf28ab7a0b0ff0a58e8a7f1d8c39e4a69


To deploy the UIUX do the following:
- Get an API key for Posit Connect "POSIT_API"
- cd into src/aria_uia
- Define the Post Connect Server: rsconnect add --server https://miganalytics.nist.gov  --name miganalytics --api-key POSIT_API`
- execute: `rsconnect deploy streamlit -N -t uiux-parrot -n miganalytics  .`