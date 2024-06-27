This is a simple example of the implementation and use of the ARIA dialog API.

The abstract base class to inherit and implement can be found here:
[src/aria_dialog_api/aria_dialog_api_base.py](src/aria_dialog_api/aria_dialog_api_base.py)

You can find an example implementation, using a local installation of llama2 here:
[src/aria_dialog_api/aria_dialog_api_local_lamma.py](src/aria_dialog_api/aria_dialog_api_local_lamma.py)

To run the text-basd (REPL) interface, execute the python script ./src/aria_dailog_api/run_repl.py.
Note that, when using the REPL with llama2, you need to use torchrun or python -m torch.distributed.launch.
E.g., python -m torch.distributed.launch run_repl.py