from operator import itemgetter

num_count = int(input())

num_list = []

for num in input().split():
    num_list.append(int(num))

output_list = []

for num in num_list:
    
    bin_num = bin(num)[2:]

    if '0' in bin_num and '1' in bin_num:
        while bin_num.index('0') < bin_num.rindex('1'):
            index = bin_num.index('0')
            bin_num = bin_num[:index] + '1' + bin_num[index + 1:]

            index = bin_num.rindex('1')
            bin_num = bin_num[:index] + '0' + bin_num[index + 1:]

        new_num = int(bin_num, 2)
        output_list.append({'num': num, 'new_num': new_num})

    else:
        output_list.append({'num': num, 'new_num': num})

actual_output = []
for item in output_list:
    actual_output.append(item['new_num'])

print(" ".join(str(num) for num in actual_output))
