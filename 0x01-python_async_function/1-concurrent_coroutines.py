#!/usr/bin/env python3
"""
uses wait_random to make a list
"""
import asyncio
import typing
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    returns list of float delays
    """
    nums = []
    for num in range(0, max_delay):
        nums.append(wait_random(max_delay))
    return nums
