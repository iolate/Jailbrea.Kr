from flask import *
app = Flask(__name__)

def tssstatus(model):
	import requests
	r = requests.get('https://api.ineal.me/tss/%s/all/noindent' % (model,), timeout=3)
	firmwares = r.json()[model]['firmwares']
	return sorted(firmwares, key=lambda x: x['started'])[-3:]

@app.route('/')
def index():
	model = request.values.get('model', 'iPhone8,1')
	
	firmwares = None
	try: firmwares = tssstatus(model)
	except: pass
	
	if firmwares == None:
		try:
			model = 'iPhone8,1'
			firmwares = tssstatus(model)
		except: pass
	
	import datetime
	fetched_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
	
	return render_template('index.html', firmwares=firmwares, fetched_time=fetched_time, model=model)

