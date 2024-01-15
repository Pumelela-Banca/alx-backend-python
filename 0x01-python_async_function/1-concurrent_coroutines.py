#!/usr/bin/env python3
"""
uses wait_random to make a list
"""
import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    returns list of float delays
    """
    nums = []
    routines = [wait_random(max_delay) for _ in range(n)]
    for num in asyncio.as_completed(routines):
        nums.append(await num)
    return nums


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
