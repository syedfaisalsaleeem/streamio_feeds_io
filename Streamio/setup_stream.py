import stream

class Streamio():
	def _connect(self):
		from dotenv import load_dotenv
		load_dotenv()
		import os
		clientid = os.getenv("clientid")
		secretid = os.getenv("secretid")
		self.client = stream.connect(clientid, secretid)
		return self.client

