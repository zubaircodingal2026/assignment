prev_mean = 38
wrong_number = 36
correct_number = 56
total_number = 40

#Calculate Current Total
current_sum = total_number * prev_mean
correct_sum = current_sum - (wrong_number - correct_number)

#correct Mean
correct_mean = correct_sum / total_number

#print CORRECT MEAN
print(correct_mean)