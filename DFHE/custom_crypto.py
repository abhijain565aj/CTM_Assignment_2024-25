from chall_ctm import flag, KEY_1, KEY_2
import binascii

assert KEY_1 < 10000
assert KEY_2 < 10000

def messed_up(x, y):
    enc_1 = (primitive ** y) % modulus
    enc_2 = (enc_1 ** x) % modulus
    return enc_2

modulus = 57812309821904813
primitive = 5214987

mess = messed_up(KEY_1, KEY_2)

bin_flag = flag.encode('utf-8')
hex_flag = binascii.hexlify(bin_flag)
int_flag = int(hex_flag,16)
xor_1 = bin(int_flag)[2:]

string = ""
while(len(string) < len(xor_1)):
    string += bin(mess)[2:]
string = string[:len(xor_1)]

ct = ""
for i in range(len(xor_1)):
    ct += str(int(xor_1[i]) ^ int(string[i]))

print("Output: ", ct)