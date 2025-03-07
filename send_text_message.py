import asyncio
import re
from email.message import EmailMessage
from typing import Collection, List, Tuple, Union

import aiosmtplib

HOST = "smtp.gmail.com"



# pylint: disable=too-many-arguments
async def send_txt(
    num: Union[str, int], carrier: str, email: str, pword: str, msg: str, subj: str
) -> Tuple[dict, str]:
    to_email = "vtext.com"

    # build message
    message = EmailMessage()
    message["From"] = email
    message["To"] = f"{num}@{to_email}"
    message["Subject"] = subj
    message.set_content(msg)

    # send
    send_kws = dict(username=email, password=pword, hostname=HOST, port=587, start_tls=True)
    res = await aiosmtplib.send(message, **send_kws)  # type: ignore
    msg = "failed" if not re.search(r"\sOK\s", res[1]) else "succeeded"
    print(msg)
    return res


async def send_txts(
    nums: Collection[Union[str, int]], carrier: str, email: str, pword: str, msg: str, subj: str
) -> List[Tuple[dict, str]]:
    tasks = [send_txt(n, carrier, email, pword, msg, subj) for n in set(nums)]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    _num = "999999999"
    _carrier = "verizon"
    _email = "user@gmail.com"
    _pword = "pword"
    _msg = "Dummy msg"
    _subj = "Dummy subj"
    coro = send_txt(_num, _carrier, _email, _pword, _msg, _subj)
    # _nums = {"999999999", "000000000"}
    # coro = send_txts(_nums, _carrier, _email, _pword, _msg, _subj)
    asyncio.run(coro)