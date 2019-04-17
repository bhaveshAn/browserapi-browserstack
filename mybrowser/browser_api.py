from requests.auth import HTTPBasicAuth
import requests


class BrowserAPI(object):

	def __init__(self, username=None, access_key=None):

		self.username = username
		self.access_key = access_key
		self.ROOT_URL = 'https://api.browserstack.com/5'
		self.auth = None

	def authenticate(self, username, password):

		if not self.username and not self.access_key:
			return {"401 Unauthorized, username and access_key are missing"}

		elif not self.username:
			return {"401 Unauthorized, username is missing"}

		elif not self.access_key:
			return {"401 Unauthorized, access_key is missing"}

		self.auth = HTTPBasicAuth(self.username, self.access_key)

		return self.auth

	def get_browsers(self, flat=False, all=False):

		if not self.auth:
			self.auth = self.authenticate(self.username, self.access_key)

		url = '{0}/browsers'.format(self.ROOT_URL)

		if not flat or not all:
			browsers = requests.get(url, auth=self.auth)

		else:
			payload = {}

			if flat:
			    
			    payload = {'flat': True}
			
			elif all:

				payload = {'all': True}

			browsers = requests.get(url, auth=self.auth, params=payload)

		return browsers.text


	def take_screenshot(self, id, format, headers=None):

		if not self.auth:
			self.auth = self.authenticate(self.username, self.access_key)

		allowed_formats = ['json', 'xml', 'png']

		header_formats = ['text/json', 'text/xml', 'image/png']

		if not id:
			return {"worker id is missing"}
		if not format and not headers['Accept']:
			return {"format is missing"}

		if headers['Accept']:
			payload = {}
			payload['Accept'] = headers['Accept']
			response = requests.get(url, params=payload, auth=self.auth)
		else:

			url = '{0}/worker/{1}/screenshot(.{2})'.format(self.ROOT_URL, id, format)
			response = requests.get(url, auth=self.auth)

		return response.text

	def get_workers(self):

		if not self.auth:
			self.auth = self.authenticate(self.username, self.access_key)

		url = '{0}/workers'.format(self.ROOT_URL)

		workers = requests.get(url, auth=self.auth)

		return workers.text

	def get_worker(self, id):

		if not self.auth:
			self.auth = self.authenticate(self.username, self.access_key)

		if not id:
			return {"worker id is missing"}

		url = '{0}/worker/{1}'.format(self.ROOT_URL, id)

		worker = requests.get(url, auth=self.auth)

		return worker.text

	def get_status(self):

		if not self.auth:
			self.auth = self.authenticate(self.username, self.access_key)

		url = '{0}/status'.format(self.ROOT_URL)

		status = requests.get(url, auth=self.auth)

		return status.text

	def delete_worker(self, id):

		if not self.auth:
			self.auth = self.authenticate(self.username, self.access_key)

		if not id:
			return {"worker id is missing"}

		url = '{0}/worker/{1}'.format(self.ROOT_URL, id)
		response = requests.delete(url, auth=self.auth)

		return response.text

	def post_worker(self, os, os_version, browser, browser_version, url, **kargs):

		if not self.auth:
			self.auth = self.authenticate(self.username, self.access_key)

		browsers = self.get_browsers()

		os_list = []
		os_version_list = {}
		browsers_list = {}
		device_list = []
		post_url = '{0}/worker'.format(self.ROOT_URL)

		for key, val in kargs:
			if key not in os_list:
				os_list.append(key)
			if val not in os_version_list[key]:
				os_version_list[key].append(val)


		data = {
		    'os': os, 'os_version': os_version, 'browser': browser, 'url': url,
		    'browser_version': browser_version}

		r = requests.post(post_url, data=data, auth=self.auth)

		return r.text