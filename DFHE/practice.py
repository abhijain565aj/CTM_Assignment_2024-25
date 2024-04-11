import binascii
flag = "CSeC{crypto"
bin_flag = flag.encode('utf-8')
# print(bin_flag)

hex_flag = binascii.hexlify(bin_flag)
# print(hex_flag)

int_flag = int(hex_flag, 16)
# print(int_flag)

xor_1 = bin(int_flag)[2:]
print(xor_1)
output = "0100000010110011001000111010010100110000011000110100101000110100111101010000000111111101011110000110111101110010000000001100101100100001111100010001101001101011010010000111100011010111000011011110100101111000010011110110000000011110111001110001001"
comp = "1100011000010101111010010010001111000110010101111010110111000110000101011110100100100011110001100101011110101101110001100001010111101001001000111100011001010111101011011100011000010101111010010010001111000110010101111010110111000110000101011110100"
print(len(output))
ans = ""
for i in range(len(xor_1)):
    ans += str(int(xor_1[i]) ^ int(output[i]))
print(ans)
print(len(ans))
modulus = 57812309821904813
m = bin(modulus)[2:]
print("modulus", len(m))
print(m)
flag_end = "}"
bin_flag_end = flag_end.encode('utf-8')
# print(bin_flag_end)
hex_flag_end = binascii.hexlify(bin_flag_end)
# print(hex_flag_end)
int_flag_end = int(hex_flag_end, 16)
# print(int_flag_end)
xor_2 = bin(int_flag_end)[2:]
xor_2 = "0"+xor_2
print(xor_2)
ans2 = ""
for i in range(len(xor_2)):
    ans2 += str(int(xor_2[i]) ^ int(output[len(output)-len(xor_2)+i]))
print(ans2)
mess = "10001100001010111101001001000111"
mess = "10001100001010111101001001000111"
mess = "110001100001010111101001001000111"
mess = "1100011000010101111010010010001"
mess = "110001100001010111101001001000111100011"  # ans
print(len(mess))
mess = "11000110000101011110100100100011"  # gives CSeC{....}
mess = "11000110000101011110100100100011110001100101011110101101"  # ans
print(len("11000110000101011110100"))
print(mess)
x = len(mess)
print(x)
y = len(output)
ans3 = ""
mess = ans[0:56]
for i in range(len(output)):
    ans3 += str(int(mess[i % x]) ^ int(output[i]))
    # if (i % 8 == 7):
    # if (ans[len(ans)-1] != "0"):
    # ans = ans[0:-1]+"0"
    # mess = mess[0:i % x]+str(int(output[i]))+mess[i % x+1:]
print(mess)
print(y)
byte_data = int(ans3, 2).to_bytes((y + 7) // 8, byteorder='big')

print(byte_data)
# Decode bytes using UTF-8 encoding
decoded_text = byte_data.decode('utf-8')

# Print the decoded text
print(decoded_text)
