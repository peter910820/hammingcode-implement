from argparse import ArgumentParser
from functools import reduce

def parse_args() -> object:
    parse = ArgumentParser(description='hamming code implement for python')
    parse.add_argument('-E', '--encode', type=str)
    parse.add_argument('-D', '--decode', type=str)
    args = parse.parse_args()
    return args

class hammingcode_implement:
    def hammingcode_encode(self, data: str) -> str:
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
        caculate = [int(index+1) for index, values in enumerate(hammingcode_list) if values == '1']
        check_code = bin(reduce(lambda x, y: x ^ y, caculate)).replace('0b', '') #xor
        if len(check_code) < check_bit_len: #zero padding
            check_code = check_code.zfill(check_bit_len)
        check_code = list(check_code)
        for index in range(0, len(hammingcode_list)-1):
            if hammingcode_list[index] == None:
                hammingcode_list[index] = check_code.pop()
        return ''.join(hammingcode_list)
        
    def hammingcode_decode(self, data: str) -> str:
        data = list(data)
        check_bits = [index+1 for index, cheker in enumerate(data) if cheker == '1']
        check_bit = int(bin(reduce(lambda x, y: x^y, check_bits)).replace('0b', ''), 2)
        if check_bit != 0:
            change_bit = int(data[check_bit-1]) | int(data[check_bit-1])
            change_bit = 1 if change_bit == 0 else 0
            data[check_bit-1] = str(change_bit)
            return f'an errors in the data, error bits is {check_bit}, correct data is {"".join(data)}'
        elif check_bit == 0:
            return 'there are no errors in the data'
        else:
            return 'another state'
        
if __name__ == '__main__':
    args = parse_args()
    run = hammingcode_implement()
    try:
        if args.encode:
            print(run.hammingcode_encode(args.encode))
        if args.decode:
            print(run.hammingcode_decode(args.decode))
    except:
        print('error!')