for i in range(5):
    current_num = i+1

    exponential = [current_num ** j for j in range(4)]
    print(current_num, exponential[0], exponential[1], exponential[2], exponential[3])
