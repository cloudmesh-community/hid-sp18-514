from eve import Eve
import platform
import psutil
import json
from flask import Response

app = Eve ()


def responseFormatter(data):
	response = Response()
	response.headers["status"] = 200
	response.headers["Content-Type"] = "application/json;charset=utf-8"
	response.data = data
	return response


@app.route('/getProcessorInfo', methods=['GET'])	
def getProcessorInfo():
	processor =  platform.processor()
	data = json.dumps({'processor_name' : processor})
	response =  responseFormatter(data)
	return response

@app.route('/getNoOfCpus', methods=['GET'])
def getNoOfCpus():
	cpu =  psutil.cpu_count()
	data = json.dumps({'No.of CPU' : cpu})
	response =  responseFormatter(data)
	return response

@app.route('/processInfo',  methods = ['GET'])
def processInfo():
	process_ids = psutil.pids()
	process_name = []
	for i in process_ids:
		process_name.append(psutil.Process(i))

	return str(process_name)


@app.route('/virtualMem')
def virtualMem():
	virtaul_memory = psutil.virtual_memory()
	return str(virtaul_memory)


@app.route('/swapMem')
def swapMem():
	swap_memory = psutil.swap_memory()
	return str(swap_memory)


if __name__ == '__main__':
    app.run()



