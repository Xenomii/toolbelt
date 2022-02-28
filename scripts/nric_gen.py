def generate(identification):
    weight = (2,7,6,5,4,3,2)  #()this is tuple and cannot be modified
    alpha_singaporean = ('J','Z','I','H','G','F','E','D','C','B','A')
  
    total_sum = 0
    for i in range (len(weight)):
        current_product = weight[i] * int(identification[i+1])
        total_sum += current_product
        
    remainder = total_sum % 11
    
    #generate last checking alphabet of the identification no.
    if ((identification[0] =='S') or (identification[0] =='T')):
        return identification+alpha_singaporean[remainder]

for i in range(99999):
    identification = 'S'+'96'+'{0:05}'.format(i)
    print(generate(identification))