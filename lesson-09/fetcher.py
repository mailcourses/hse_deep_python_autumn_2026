import asyncio
import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.text()
    return text


async def fetch_batch_urls(urls):
    tasks = []
    res = []

    for i, url in enumerate(urls):
        tasks.append(fetch_url(url))

    async for compl_task in asyncio.as_completed(tasks):
        task_result = await compl_task
        res.append(task_result[:100])

    print(res)

    return res


if __name__ == "__main__":
    URL = "https://docs.python.org/3/whatsnew/3.14.html"
    asyncio.run(fetch_batch_urls([URL] * 3))
