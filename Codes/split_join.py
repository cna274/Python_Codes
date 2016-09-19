string, substring = (raw_input(), raw_input())
print string, substring
print sum([1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)]==substring])