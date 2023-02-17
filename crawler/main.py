import asyncio
import aiohttp
import json
import time

from loguru import logger


url = "https://shopee.sg/api/v4/shop/search_items?" \
      "filter_sold_out=0&limit={limit}&" \
      "offset={offset}&order=desc&shopid={name}&" \
      "sort_by=pop&se_case=1"
storage_path = "./shared-volume/{}.json"
shop_id = ["220997827", "223946658"]


# Create concurently task
def get_data_task(session):
    tasks = []
    logger.info("Get Data...")
    for s in shop_id:
        tasks.append(get_data(s, session))

    return tasks


async def get_data(n, session):
    offset = 0
    limit = 30
    total = 0
    result = []

    while offset <= total:
        # Get the item on url
        resp = await session.get(url.format(
            limit=limit, offset=offset, name=n), ssl=False)
        content = await resp.json()
        total = max(content["total_count"], total)

        for item in content["items"]:
            item_dict = {}
            item_dict["name"] = item["item_basic"]["name"]
            item_dict["price"] = item["item_basic"]["price"]
            result.append(item_dict)
        offset += limit

        if content["nomore"]:
            break

    with open(storage_path.format(n), "w") as f:
        f.write(json.dumps(result, indent=2))


# Concurely call API
async def call_api():
    async with aiohttp.ClientSession() as session:
        get_tasks = get_data_task(session)
        await asyncio.gather(*get_tasks)


if __name__ == "__main__":
    while True:
        try:
            asyncio.run(call_api())
            logger.info("DONE")
            time.sleep(100)
        except Exception as e:
            logger.error(e)
