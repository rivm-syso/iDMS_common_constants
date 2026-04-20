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

ACTIVE_RUNSHEET_STATES = [ 'incoming', 'prepare', 'stage', 'spacecheck', 'download', 'queued', 'startup', 'active', 'finishing', 'postprocessing', 'distribute', 'cleanup' ]

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