#!/usr/bin/python3
# coding: latin-1
blob = '''               B���g�4��5Z��=�������Q��Ϻ����\MȻ�hD�q�R��ܟ\t"�m�	9d�Q��7�C ���qđUH��i<ɼ'�9U�E�4xS�:������1��s�d*��6��'''
from hashlib import sha256
if(sha256(blob.encode("latin-1")).hexdigest() == "b49d8926b0419858064aeebfbad333db67a7f804663654d5a734387b61a4ada7"):
    print("Use SHA-256 instead!")
elif(sha256(blob.encode("latin-1")).hexdigest() == "907fb5d261f0007af88bfa1c41330b016faee82304273f3aa937538a210bb8a8"):
    print("MD5 is perfectly secure!")