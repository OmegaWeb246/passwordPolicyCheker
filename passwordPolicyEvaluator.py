#!/user/bin/env python

import optparse

parser = optparse.OptionParser()

parser.add_option("-m","--max", dest="max_length",help="Maximum length of the password string")
parser.add_option("-s","--min-length", dest="min_length",help="Minimum length of the password string")
parser.add_option("-p","--pwd-type", dest="pwd_type",help="Password type, letter(lt), alphanumerical(an), numerical(num), all character (all)")

(options, arguments) = parser.parse_args()

max_length = options.max_length
max_length = int(2 if max_length is None else options.max_length)
min_length = options.min_length
min_length = int(1 if min_length is None else options.min_length)
pwd_type = str(options.pwd_type)
 
def total_possibilities(distance, nb_char):
    counter = 0
    total = 0
    while counter <= distance:
        total = total + nb_char ** (min_length + counter)
        counter += 1
    return total    

def counting_possibilities(min,max, pwd):
  
    dist = max - min
    if pwd == "lt":        
        possible = total_possibilities(dist, 52)
    elif pwd == "an":
        possible = total_possibilities(dist,62 )
    elif pwd == "num":
        possible = total_possibilities(dist,10 )
    elif pwd == "all":
        possible = total_possibilities(dist,94 )
    else:
        possible = "ERROR, INVALID PASSWORD TYPE"
    return possible

possibilities = counting_possibilities(min_length,max_length, pwd_type)

time_seconds = int(possibilities / 100)

if time_seconds > 3600:
    time_hour = int(time_seconds / 3600)
    print(time_hour)
    index_hour = len(str(time_hour)) + int(len(str(time_hour)) / 3) -1
if index_hour > 3:
    counter_hour = 3
    time = str(time_hour)
    while index_hour > counter_hour:
        time = time[:-counter_hour] + ',' + time[-counter_hour:]
        counter_hour = counter_hour + 4


possibilities =str(possibilities)
index = len(possibilities) + int(len(possibilities) / 3) -1


if index > 3:
    counter = 3
    while index > counter:
        possibilities = possibilities[:-counter] + ',' + possibilities[-counter:]
        counter = counter + 4

print('Your password policy allows for ' + possibilities + ' different passwords.')
print('')
print('Hacker would take about ' + time + ' hours to test every possibilities. Giving he can test 100 password per second.')


