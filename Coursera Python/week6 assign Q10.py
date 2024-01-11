
'''Q10:
A file has a section at the top that has a preamble describing the contents of the file, 
then a blank line,
then a list of high temperatures for each day in January all on one line,
then a list of high temperatures for each day in February all on one line,
then lists for March, April, and so on through December, each on one line.  
There are thousands of lines of information after that temperature data that you aren't currently interested in.

You want to write a program that prints the average of the high temperatures in January. 
'''

import tkinter.filedialog
file_name = tkinter.filedialog.askopenfilename()
file_P = open(file_name, 'r')

def ave_temp_month(file_name, month):
    '''(file open for reading, str) -> float
    Return the average of the high temperatures in a month of year.

    pre-condition: A file has a section at the top that has a preamble describing the contents of the file, 
    then a blank line,then a list of high temperatures.

    >>>ave_temp_month(file, month)
    40.0
    '''
    temp_list = []
    for line in file_name:
        if line.startswith(month):
            temp_line = file_name.readline().strip().split()   #list = ['32', '34', '36', '33'....']
            for num in temp_line:
                temp_list.append(int(num))
                #print(temp_list)                              #list = [32, 34, 36, 33, 30,....]
            ave_temp = sum(temp_list) / len(temp_list)
            return f'average of the high temperatures in {month} = {ave_temp}'
            #return ave_temp
        
               
print(ave_temp_month(file_P, 'January'))
        


# data = "January: 32 34 36 33 30 29 31 30 32 35 37 38 40 39 36 35 34 32 30 31 33 35 36 38 39 40 41 42 43 41"

# # Finding the index of the colon
# colon_index = data.find(':')

# # Extracting the temperatures for January
# january_temperatures = data[colon_index + 1:].split()

# print(january_temperatures)



# def get_temperatures_for_month(file_name, month):
#     with open(file_name, 'r') as file:
#         for line in file:
#             if line.startswith(month):
#                 colon_index = line.find(':')
#                 temperatures = line[colon_index + 1:].split()
#                 return temperatures

# # Usage
# file_name = 'temperature_data.txt'
# requested_month = 'January'

# january_temperatures = get_temperatures_for_month(file_name, requested_month)
# print(f"Temperatures for {requested_month}: {january_temperatures}")
