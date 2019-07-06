import numpy as np
def generate_label(array,sign,num=3):
	if sign==0:
		return generate_label_Reg(array)
	elif sign==1:
		return generate_label_two(array)
	elif sign==2:
		return generate_label_multi(array,num)
	
def generate_label_Reg(array):
	delta=[]
	delta.append(0)
	for i in range(len(array)-1):
		delta.append(array[i+1]-array[i])
	return delta
def generate_label_two(array):
	bi_delta=[]
	delta=generate_label_Reg(array)
	for i in range(len(delta)):
		if delta[i]>0:
			bi_delta.append(1)
		else:
			bi_delta.append(0)
	return bi_delta
def generate_label_multi(array,cluster):
    num=cluster+1
    delta=np.array(generate_label_Reg(array))
    labels=[]
    print(delta)
    per=np.array([np.percentile(delta,i*100.0/num) for i in range(0,num)])
    print(per)
    for i in range(len(delta)):
        for j in range(len(per)-1):
            if delta[i]>=per[j] and delta[i]<per[j+1]:
                labels.append(j)
    return labels

