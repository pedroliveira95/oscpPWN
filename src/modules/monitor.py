import threading,socket,traceback
import queue
import time

from src.miscellaneous.config import bcolors,Config
from src.menus.commons import State

class Monitor(threading.Thread):

	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.flag = threading.Event()
		self.procList = []
		self.reqList = queue

	# Should I clean waiting threads in the queue??
	def shutdown(self):
		for proc in self.procList:
			proc[1].flag.set()
		for proc in self.procList:
			proc[1].join(timeout=60)

	def run(self):
		while not self.flag.is_set():
			# Check for finished tasks
			for proc in self.procList[:]:
				if not proc[1].isAlive():
					if Config.LOGGERSTATUS == "True":
						with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
							s.connect((Config.LOGGERIP,int(Config.LOGGERPORT)))
							try:
								s.sendall((bcolors.OKBLUE+"Task "+proc[0]+" Finished!"+bcolors.ENDC+"\n").encode())
							finally:
								s.close()
					else:
						print("{}Task {} Finished!{}\n".format(bcolors.OKBLUE,proc[0],bcolors.ENDC))
					self.procList.remove(proc)
			# Check for new tasks
			try:
				req = self.reqList.get_nowait()
				if Config.LOGGERSTATUS == "True":
					with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
						s.connect((Config.LOGGERIP,int(Config.LOGGERPORT)))
						try:
							s.sendall(("\n"+bcolors.OKBLUE+"Task "+req[0]+" Started!"+bcolors.ENDC).encode())
						finally:
							s.close()
				else:
					print("\n{}Task {} Started!{}".format(bcolors.OKBLUE,req[0],bcolors.ENDC))
				req[1].start()
				self.procList.append(req)
			except Exception as e:
				#print("{}".format(e))
				#print("{}".format(traceback.print_exc()))
				pass

			time.sleep(1)
		self.shutdown()
		return
