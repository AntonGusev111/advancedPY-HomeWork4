#task1
# Task1 v.1
class FlatIterator:

    def __init__(self,nested_list):
        self.start = 0
        self.flag = -1
        self.object = nested_list

    def __iter__(self):
        return self

    def __next__(self):
        self.flag +=1
        if self.flag == len(self.object[self.start]):
            self.start += 1
            self.flag = 0
        if self.start == len(self.object):
            raise StopIteration
        return self.object[self.start][self.flag]

# Task1 v.2
class FlatIterator1:
    def __init__(self,nested_list):
        self.object = nested_list
        self.start = -1
        self.end = len(self.object)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return '\n'.join(str(elem) for elem in self.object[self.start])

#Task2 v.1
def flat_generator(nested_list):
    for list in nested_list:
        for item in list:
            return item




#Task2 v.2
def flat_generator1(nested_list):
    item = ((el) for l in range(len(nested_list)) for el in nested_list[l])
    return item


#Task3
class ListsIterator:
    def __init__(self, object):
        self.object = object
        self.start = -1
    def __iter__(self):
        return flat_gen(self.object)
    def __next__(self):
        self.start += 1
        if self.start == len(self.object):
            raise StopIteration
        return  '\n'.join(str(elem) for elem in self.object[self.start]) #self.object


#Task4
def flat_gen(object):
    for item in object:
        if type(item) == list:
            iter_object = (obj for obj in flat_gen(item))
            for res in iter_object:
                yield res
        else:
            yield item



nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list1 = [
	['a', 'b', 'c',[1,2,'d'],'d'],
	['d', 'e', 'f', 'h', False,[True,1,False,['1',2,'435345'],[9,0,0,9]]],
	[1, 2, False]
]

print('Task1 v.1')
for item in FlatIterator(nested_list):
    print(item)
print('--------------------')
print('Task1 v.1')
flat = [item for item in FlatIterator(nested_list)]
print(flat)
print('--------------------')
print('Task1 v.2')
for item in FlatIterator1(nested_list):
    print(item)
print('--------------------')
print('Task1 v.2')
flat = [item for item in FlatIterator1(nested_list)]
print(flat)
print('--------------------')
print('Task3')
for item in ListsIterator(nested_list1):
    print(item)
print('--------------------')
flat = [item for item in FlatIterator(nested_list1)]
print(flat)
print('--------------------')
print('Task4')
for i in flat_gen(nested_list1):
    print(i)
print('--------------------')
res = [item for item in flat_gen(nested_list1)]
print(res)