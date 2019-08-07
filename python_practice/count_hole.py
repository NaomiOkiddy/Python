def count_hole(num):
	hole_count = {0:1, 1:0, 2:0, 3:0, 4:1, 5:0, 6:1, 7:0, 8:2, 9:1}
	num_list = []
	sum = 0

	while num > 0:
		num_list.append(num%10)
		num = num // 10
	
	for i in range(len(num_list)):
		sum += hole_count[num_list[i]]
	return sum

print(count_hole(819))
