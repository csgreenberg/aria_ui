"""ARIA Logging API

This module handles logging for the ARIA dialog experiments, dialog turns, user feedback,  and other
events, e.g., API calls.

This file can be imported as a module and contains the following
functions:

    * log_experiment - logs experiment metadata
    * log_event - logs event metadata
    * log_dialog_turn - logs the metadata for a dialog turn (aka adjacency pair)
    * log_user_feedback - logs the user feedback and associated metadata
"""
import logging, sys
from utils import JsonFormatter

#TODO: replace hardcoded filepath with environment variable
log_filepath = "/tmp/foo.json"
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#TODO: enable option to write to DB reather than file
json_handler = logging.FileHandler(log_filepath)
json_formatter = JsonFormatter({
                                "message": "message",
                                "timestamp": "asctime"})
json_handler.setFormatter(json_formatter)
logger.addHandler(json_handler)

def log_experiment(experiment_id, metadata_dict):
    """Writes experiment identifier and experiment metadata to the log.

    Parameters
    ----------
    experiment_id : str
        Unique identifier associated with an experiment.
    metadata_dict : dict
        A dictionary mapping metadata attribute names to attribute values.

    Returns
    -------
    None
    """
    metadata_dict['experiment_id'] = experiment_id
    metadata_dict['logging_record_type'] = 'log_experiment'
    logger.info(metadata_dict)
def log_event(experiment_id, session_num, adjpair_num, metadata_dict):
    """Writes event metadata to the log.

    Parameters
    ----------
    experiment_id : str
        Unique identifier associated with an experiment.
    session_num : int
        Non-negative integer indicating the session number within the experiment. Each
        experiment has one or more sessions, and each session has one or more adjacency pairs
        (aka dialog turns).
    adjpair_num : int
        Non-negative integer indicating the adjacency pair within the session. Each
        experiment has one or more sessions, and each session has one or more adjacency pairs
        (aka dialog turns).
    metadata_dict : dict
        A dictionary mapping metadata attribute names to attribute values.

    Returns
    -------
    None
    """
    metadata_dict['experiment_id'] = experiment_id
    metadata_dict['logging_record_type'] = 'log_event'
    metadata_dict['session_num'] = session_num
    metadata_dict['adjpair_num'] = adjpair_num
    logger.info(metadata_dict)
def log_dialog_turn(experiment_id, session_num, adjpair_num, query, response,
                    metadata_dict=None):
    """Writes a dialog turn and optional metadata to the log.

    Parameters
    ----------
    experiment_id : str
        Unique identifier associated with an experiment.
    session_num : int
        Non-negative integer indicating the session number within the experiment. Each
        experiment has one or more sessions, and each session has one or more adjacency pairs
        (aka dialog turns).
    adjpair_num : int
        Non-negative integer indicating the adjacency pair within the session. Each
        experiment has one or more sessions, and each session has one or more adjacency pairs
        (aka dialog turns).
    query : str
        The prompt the user provided to the app.
    response : str
        The app's response to the query provided by the user.
    metadata_dict : dict, optional
        A dictionary mapping metadata attribute names to attribute values. Default value is None

    Returns
    -------
    None
    """
    if metadata_dict is None:
        metadata_dict = {}
    metadata_dict['experiment_id'] = experiment_id
    metadata_dict['logging_record_type'] = 'log_dialog_turn'
    metadata_dict['session_num'] = session_num
    metadata_dict['adjpair_num'] = adjpair_num
    metadata_dict['query'] = query
    metadata_dict['response'] = response
    logger.info(metadata_dict)

def log_user_feedback(experiment_id, session_num, adjpair_num, metadata_dict):
    """Writes a user feedback metadata to the log.

    Parameters
    ----------
    experiment_id : str
        Unique identifier associated with an experiment.
    session_num : int
        Non-negative integer indicating the session number within the experiment. Each
        experiment has one or more sessions, and each session has one or more adjacency pairs
        (aka dialog turns).
    adjpair_num : int
        Non-negative integer indicating the adjacency pair within the session. Each
        experiment has one or more sessions, and each session has one or more adjacency pairs
        (aka dialog turns).
    query : str
        The prompt the user provided to the app.
    response : str
        The app's response to the query provided by the user.
    metadata_dict : dict
        A dictionary mapping metadata attribute names to attribute values. Default value is None

    Returns
    -------
    None
    """
    metadata_dict['experiment_id'] = experiment_id
    metadata_dict['logging_record_type'] = 'log_user_feedback'
    metadata_dict['session_num'] = session_num,
    metadata_dict['adjpair_num'] = adjpair_num
    logger.info(metadata_dict)



