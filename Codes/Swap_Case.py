input_string = raw_input()
input_list = list(map(ord,input_string))
answer = [i-32 if i>96 and i<123 else i+32 if i>64 and i<91 else i for i in input_list]
out_char = map(chr,answer)
print ''.join(out_char)