#  File: BabyNames.py 

#  Description:  

#  Student Name:  David Bradham

#  Student UT EID:  dmb3767

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 3/23

#  Date Last Modified: 3/24

import requests
def second_of_pair(t):
  x = int(t[1])
  return x
# Function to return whether a given name is in the dictionary
def search(name, dict_):
  keys = list(dict_.keys())
  for i in keys:
    if i == name:
      return True
  return False
# Function to show all rankings for a given name
def decades(name, dict_):
  first_line = ''
  decade = 1900
  values = list(dict_[name])
  for i in values:
    first_line = first_line + ' ' + str(i)
  print(name + ':' + first_line)
  for i in values:
    print(str(decade) + ': ' + str(i))
    decade += 10
  return
# function to translate an index value taken from a value in the dictionary and return a decade value
def idx_to_decade(idx):
  if idx == 0:
    decade = 1900
  elif idx == 1:
    decade = 1910
  elif idx == 2:
    decade = 1920
  elif idx == 3:
    decade = 1930
  elif idx == 4:
    decade = 1940
  elif idx == 5:
    decade = 1950
  elif idx == 6:
    decade = 1960
  elif idx == 7:
    decade = 1970
  elif idx == 8:
    decade = 1980
  elif idx == 9:
    decade = 1990
  else:
    decade = 2000
  return decade
# function serves the same purpose as above except it takes decades as argument and returns an index
def decade_to_idx(decade):
  if decade == 1900:
    idx = 0
  elif decade == 1910:
    idx = 1
  elif decade == 1920:
    idx = 2
  elif decade == 1930:
    idx = 3
  elif decade == 1940:
    idx = 4
  elif decade == 1950:
    idx = 5
  elif decade == 1960:
    idx = 6
  elif decade == 1970:
    idx = 7
  elif decade == 1980:
    idx = 8
  elif decade == 1990:
    idx = 9
  else:
    idx = 10
  return idx
# function that returns a sorted list in terms of the most popular names in a given decade
def names(decade, dict_):
  list_names = []
  keys = list(dict_.keys())
  for name in keys:
    if dict_[name][decade] != '0':
      list_names.append((name, dict_[name][decade]))
  list_names = sorted(list_names, key = second_of_pair)      
  return list_names
# function that displays all the names which are ranked in every decade
def always_appear(dict_):
  list_names = []
  keys = list(dict_.keys())
  for i in keys:
    append = True
    for j in range(11):
      if dict_[i][j] == '0':
        append = False
    if append == True:
      list_names.append(i)
  return sorted(list_names)
# function that displays all the names which are ranked and more popular each decade
def more_popular(dict_, keys):
  pop_list = []
  for i in keys:
    app = True
    for j in range(10):
      if int(dict_[i][j]) < int(dict_[i][j+1]):
        app = False
    if app == True:
      pop_list.append(i)
  num_names = len(pop_list)
  print(str(num_names) + ' names are more popular in every decade.')
  for i in sorted(pop_list):
    print(i)
# function that displays all ranked names which are less popular each decade
def less_popular(dict_, keys):
  pop_list = []
  for i in keys:
    app = True
    for j in range(10):
      if int(dict_[i][j]) > int(dict_[i][j+1]):
        app = False
    if app == True:
      pop_list.append(i)
  num_names = len(pop_list)
  print(str(num_names) + ' names are less popular in every decade.')
  for i in sorted(pop_list):
    print(i)
def main():
# define the url where the data is and use requests module to store data locally
  url = 'http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt'
  try:
    r = requests.get(url, stream = True)
  except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)
  dict_ = {}
# decode the data and populate a dictionary with names and list objects showing their relative rank each decade
  for line in r.iter_lines():
    line = str (line, encoding = 'utf8')
    line = line.strip()
    line = line.split()
    key = line[0]
    dict_[key] = list(line[1: ])
# display the options to a user using a loop
  user_input = True
  while user_input == True:
    print('Options:')
    print('Enter 1 to search for names.')
    print('Enter 2 to display data for one name.')
    print('Enter 3 to display all names that appear in only one decade.')
    print('Enter 4 to display all names that appear in all decades.')
    print('Enter 5 to display all names that are more popular in every decade.')
    print('Enter 6 to display all names that are less popular in every decade.')
    print('Enter 7 to quit.')
    print(' ')
    num = input('Enter choice:')
# conditional for option 1
    if num == '1':
      name = input('Enter a name:')
      if search(name, dict_) == True:
        decade_values = list(dict_[name])
        for i in range(len(decade_values)):
          if decade_values[i] == '0':
            decade_values[i] = 1001
          decade_values[i] = int(decade_values[i])
        if decade_values.count(min(decade_values)) > 1:
          list_decades = []
          for i in range(len(decade_values)):
            if decade_values[i] == min(decade_values):
              list_decades.append(idx_to_decade(i))
          print(name, end=' ')
          print(*list_decades, sep=' ')
        else:
          idx = decade_values.index(min(decade_values))
          print(name + ' ' + str(idx_to_decade(idx)))           
      else:
        print(name + ' does not appear in any decade.')
# condtional for option 2
    elif num == '2':
      name = input('Enter a name:')
      if (search(name, dict_) == True):
        decades(name, dict_)
      else:
        print(name + ' does not appear in any decade.')
# conditional for option 3
    elif num == '3':
      decade = int(input('Enter decade:'))
      print('The names are in order of rank:')
      decade = decade_to_idx(decade)
      list_names = names(decade, dict_)
      for i in list_names:
        print(i[0] + ': ' + i[1])
# conditional for option 4
    elif num == '4':
      list_names = always_appear(dict_)
      num_names = len(sorted(list_names))
      print(str(num_names) + ' names appear in every decade. The names are: ')
      for i in sorted(list_names):
        print(i)
# condtional for option 5
    elif num == '5':
      lista = always_appear(dict_)
      more_popular(dict_, lista)
# condtional for option 6
    elif num == '6':
      lista = always_appear(dict_)
      less_popular(dict_, lista)
# conditional for any input not associated with options 1-6
    else:
      print(' ')
      user_input = False
    print(' ')
  print('Goodbye.')
main()
