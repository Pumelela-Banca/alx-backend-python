#!/usr/bin/env python3
"""
asynchronous coroutine returns rando number
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it
    """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r


if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
