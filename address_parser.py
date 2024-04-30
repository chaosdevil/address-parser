import os
import thaiaddress
import multiprocessing
from pprint import pprint
from typing import List, AnyStr, Dict
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from time import time


def address_parser(address: str) -> str:
    
    result = thaiaddress.parse(text=address)
    
    return result

def parse_address_list(addresses: List[str]) -> List[Dict]:
    # parsed_result = []
    # for address in addresses:
    #     result = thaiaddress.parse(text=address)
    #     # print(type(result))
    #     parsed_result.append(result)

    start = time()
    # parsed_addresses = []
    with ThreadPoolExecutor() as executor:
        parsed_result = executor.map(address_parser, addresses)
    
    print(f"Time elapsed: {time() - start} secs")

    return parsed_result


if __name__ == "__main__":
    addresses = [
        "88/99 หมู่บ้านศิริชัย ทวีวัฒนา เขตทวีวัฒนา กรุงเทพมหานคร 11170",
        "71 ซอยเลี่ยงเมืองนนทบุรี 3 แยก 2 ตำบลสวนใหญ่ อำเภอเมือง จังหวัดนนทบุรี 11000",
        "ไทยรัฐออนไลน์ บริษัท เทรนด์ วีจี3 จำกัด อาคาร 17 ชั้น 7, 9 เลขที่ 1 ถนนวิภาวดีรังสิต แขวงจอมพล เขตจตุจักร กรุงเทพฯ 10900 อีเมล: cs@thairath.co.th โทร: 02-127-1222 แฟกช์: 02-272-1783"
    ] * 100
    # start = time()
    # parsed_result = []
    # for address in addresses:
    #     parsed_result.append(address_parser(address=address))
    # # pprint(parsed_result)
    # with open("parsed_result_1.txt", "w") as f:
    #     for res in parsed_result:
    #         f.write(str(res) + "\n")
    #     f.close()
    # print(f"Time elapsed : {time() - start} secs")

    # multi-threading
    start = time()
    # parsed_addresses = []
    with ThreadPoolExecutor() as executor:
        result = executor.map(address_parser, addresses)
    with open("parsed_result_2.txt", "w") as f:
        for address in result:
            f.write(str(address) + "\n")
        f.close()
    print(f"Time elapsed : {time() - start} secs")
    result = parse_address_list(addresses)

    # for res in result:
    #     print(res)
    
    # for res in result:
    #     print(res)
