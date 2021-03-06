############ OUTPUT GRAPHICS ################
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Config:

	CONFIG = {
		"GENERAL" : {
			"SESSID" : "",
			"EDITOR" : "vim",
			"PATH"   : "",
			"HOSTIP" : "127.0.0.1",
		},
		"CONCURRENCY" : {
			"MAXMODULES"  		: 3,
			"MAXPROFILES" 		: 5, 
			"PROFILETIMEOUT" 	: 300 #Seconds
		},
		"SHARES" : {	
			"HTTPPORT" : "80",
			"FTPPORT"  : "21",
			"FTPUSER"  : "user",
			"FTPPASS"  : "user",
			"SMBPORT"  : "445",
			"SMBUSER"  : "user",
			"SMBPASS"  : "user"
		},
		"SHELLZ" : {
			"SHELLPORT" : "443"
		},
		"LOGGER" : {
			"LOGGERIP" 	   : "127.0.0.1",
			"LOGGERPORT"   : "9999",
			"LOGGERSTATUS" : "False"
		},
		"OUTPUT" : {
			"LOGGERVERBOSE" : "True",
			"CLIENTVERBOSE" : "False",
			"OUTMODE"	: "0"
		}
	}
