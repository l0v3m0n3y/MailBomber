import asyncio
from bomber import AsyncBomber
async def main(email):
	await AsyncBomber().send_spam(email)
print("help for Developer . ton: UQAeAZH2DkWqsU8zLtdpx9ELkM0agCtCoi8myYkPOJ-9ObNS")
count=int(input("count threads»"))
email=input("email»")
for x in range(count):
	asyncio.get_event_loop().run_until_complete(main(email))