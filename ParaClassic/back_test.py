from condition import buy_condition,sell_condition
def back_test(value,total=10000,sum=0,asset=10000,*args):
	for i in range(1,len(value)):
		if buy_condition(i,*args) and total>0:
			if total>100：
				total=total-100
				sum=sum+100.0/value[i]
			elif total<=100:
				total=0
				sum=sum+total/value[i]
		if sell_condition(i,*args) and sum>0:
			sum=sum/2
			total=total+sum*value
		asset=total+sum*value[i]
		print("day: "+str(i)+"	stock:"+str(sum)+" cash:"+str(total)+" asset:"+str(asset))