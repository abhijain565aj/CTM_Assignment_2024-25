from secret import flag, KEY_1, KEY_2
import binascii

# KEY_1 = 1234
# KEY_2 = 6789
# flag = "CSeC{This is a flag}"
assert KEY_1 in range(int(1000), int(2000))
assert KEY_2 in range(int(6000), int(7000))


def messed_up(x, y):
    enc_1 = (primitive ** y) % modulus
    enc_2 = (enc_1 ** x) % modulus
    return enc_2


modulus = 57812309821904813
primitive = 5214987

mess = messed_up(KEY_1, KEY_2)
# print(mess)

bin_flag = flag.encode('utf-8')
# print(bin_flag)

hex_flag = binascii.hexlify(bin_flag)
# print(hex_flag)

int_flag = int(hex_flag, 16)
# print(int_flag)

xor_1 = bin(int_flag)[2:]
# print(xor_1)

string = ""
while (len(string) < len(xor_1)):
    string += bin(mess)[2:]
    # print(string)
string = string[:len(xor_1)]
# print(string)

ct = ""
for i in range(len(xor_1)):
    ct += str(int(xor_1[i]) ^ int(string[i]))

print("Output: ", ct)
