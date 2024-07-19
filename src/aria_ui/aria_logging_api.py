
import logging, sys
from utils import JsonFormatter


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
json_handler = logging.FileHandler("/tmp/foo.json")
json_formatter = JsonFormatter({
                                "message": "message",
                                "timestamp": "asctime"})
json_handler.setFormatter(json_formatter)
logger.addHandler(json_handler)

def log_experiment(experiment_id, metadata_dict):
    metadata_dict['experiment_id'] = experiment_id
    metadata_dict['logging_record_type'] = 'log_experiment'
    logger.info(metadata_dict)
def log_event(experiment_id, session_num, adjpair_num, metadata_dict):
    metadata_dict['experiment_id'] = experiment_id
    metadata_dict['logging_record_type'] = 'log_event'
    metadata_dict['session_num'] = session_num
    metadata_dict['adjpair_num'] = adjpair_num
    logger.info(metadata_dict)
def log_dialog_turn(experiment_id, session_num, adjpair_num, query, response):
    dt_dict = {'logging_record_type': 'log_dialog_turn',
               'experimentid': experiment_id,
               'session_num': session_num,
               'adjpair_num': adjpair_num,
               'query': query,
               'response': response}
    logger.info(dt_dict)
def log_user_feedback(experiment_id, session_num, adjpair_num, metadata_dict):
    metadata_dict['experiment_id'] = experiment_id
    metadata_dict['logging_record_type'] = 'log_user_feedback'
    metadata_dict['session_num'] = session_num,
    metadata_dict['adjpair_num'] = adjpair_num
    logger.info(metadata_dict)



