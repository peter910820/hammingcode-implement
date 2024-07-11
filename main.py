from functools import reduce

class hammingcode_implement:
    def hammingcode_encode(self, data: str) -> list:
        hammingcode_len = len(data)
        k = 1
        while 2**k-k < hammingcode_len+1:
            k += 1
        hammingcode_len = hammingcode_len + k
        hammingcode_list = [bits for bits in data]
        retention_bit = 1 #release
        check_bit_len = 0
        while retention_bit < hammingcode_len:
            hammingcode_list.insert(retention_bit-1, None)
            retention_bit *= 2
            check_bit_len += 1
        caculate = [int(index+1) for index, values in enumerate(hammingcode_list) if values == "1"]
        check_code = bin(reduce(lambda x, y: x ^ y, caculate)).lstrip("0b") #xor
        if len(check_code) < check_bit_len: #zero padding
            check_code = check_code.zfill(check_bit_len)
        check_code = list(check_code)
        for index in range(0, len(hammingcode_list)-1):
            if hammingcode_list[index] == None:
                hammingcode_list[index] = check_code.pop()
        return ''.join(hammingcode_list)
        
    def hammingcode_decode(self):
        pass

run = hammingcode_implement()

print(run.hammingcode_encode("1"))