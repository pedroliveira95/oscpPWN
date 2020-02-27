import queue

from ..miscellaneous.config import Config

class State:
    menu_state = "main"
    module_state = ""
    module_class = ""
    global_option = ["services","hosts","config","help","ls","back"]
    menu_option = {
        "main": {
            "internal":{
                "share":{
                    "smb":{},
                    "ftp":{},
                    "http":{},
                    "powershell":{},
                    "vbscript":{}
                    },
                "linux":{},
                "windows":{}
            },
            "external":{
                "shellZ":{
                    "linux_x86":{},
                    "windows_x86":{},
                    "php":{},
                    "asp":{},
                    "jsp":{}
                    },
                "use":{},
                "search":{}
            },
            "bof" : {
                "badchars":{},
                "pattern":{},
                "offset":{},
                "lendian":{},
                "nasm":{},
                "nops":{},
                "notes":{}
            },
            "buckets":{
                "open":{},
                "list":{},
                "add":{},
                "del":{}
                },
            "exit":{}
        }
    }
    env_option = {}
    module_option = {
                "get":{},
                "set":{},
                "go":{}
            }
    procs = queue.Queue(maxsize=Config.MAXTHREADS)
    share_state = {
            "smb":{
                "status":False,
                "pid":0
            },
            "ftp":{
                "status":False,
                "pid":0
            },
            "http":{
                "status":False,
                "pid":0
            }
        }

    def __init__(self):
        pass