def flip_it(v):
    try:
        if v.bit_length():
            return v
    except:
        return v[::-1]
        
            
        