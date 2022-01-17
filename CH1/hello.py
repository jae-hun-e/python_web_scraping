# [] : list (변경가능) <-> array
# () : tuple (변경불가능) <-> ? 
# {} : dictionary (key : value) <-> obj

def say_hello():
  print('hello')
  
say_hello()

test = {
  'name' : 'jaehun',
  'test_list' : ['one', 'two', 'three'],
  'test_tuple' : ('one', 'two', 'three'),
  'test_dictionary' : {'one' : 1, 'two' : 2, 'three' : 3}
  
}

print (test)

nico = {'age':44}

print(nico)
