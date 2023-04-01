from pwn import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f",
                    "--filename",
                    type=str,
                    help="name of the executable file that you want to find the offset of",
                    required=True)
parser.add_argument("-p",
                    "--payload-size",
                    type=int,
                    help="size of the payload to use to find the offset (must be enough to cause a segmentation fault in the program)",
                    required=True)
args = parser.parse_args()

def find_rip_offset():
    """
    Finds the offset in a buffer overflow on a 64-bit system to the RSP pointer.

    :param payload_size: (int) the size of payload to use while finding the RIP (must be enough to cause a segmentation fault)
    :return: (int) the offset to the RSP
    """
    p = process(args.filename)
    p.sendlineafter(b'WeLcOmE To mY EcHo sErVeR!', cyclic(args.payload_size))

    p.wait()
    rsp_offset = cyclic_find(p.corefile.read(p.corefile.rsp, 4))
    info("RIP offset is {}".format(rsp_offset))

    p.kill()
    return rsp_offset

find_rip_offset()
