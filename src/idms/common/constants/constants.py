OBJ_METADATA_YML = 'metadata.yml'
OBJ_METADATA_JSON = 'metadata.json'

TRUE = 'true'
FALSE = 'false'

TF = {
    True: TRUE,
    False: FALSE,
    1: TRUE,
    0: FALSE
}

ACTIVE_RUNSHEET_STATES = [ 'incoming', 'depends', 'choose', 'prepare',
                     'stage', 'spacecheck', 'download', 'queued',
                     'active', 'finishing', 'postprocessing', 'distribute',
                     'cleanup', 'notify', 'waiting']

# Logging Settings
DEBUG2=0
DEBUG1=1
DEBUG0=2
INFO=3
WARN=4
ERR=5

#LOGLEVEL=DEBUG1

LOGNAME=[
  'DEBUG2',
  'DEBUG1', 
  'DEBUG0', 
  'INFO', 
  'WARN', 
  'ERROR'
]

# Mapping of irods DATA_REPL_STATUS values to description
DATA_REPL_STATUS = {
    '0': 'STALE_REPLICA',
    '1': 'GOOD_REPLICA',
    '2': 'INTERMEDIATE_REPLICA',
    '3': 'READ_LOCKED',
    '4': 'WRITE_LOCKED'
}