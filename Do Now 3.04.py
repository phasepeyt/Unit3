'''
###############
Do Now 3.04
###############
Quiz Announcement
-----------------
We will have a quiz tomorrow on Unit 2
We will also have a quiz next Tuesday over Unit 3 so far.

Discussion
----------
Is there any topic you would like to focus on and cover more of?  def functions
I will check the responses here and prepare to discuss tomorrow in class

In your Notebook
----------------
Rank the following from easiest to hardest:

Importing built-in functions 5

Using randint 6

Abstraction/creating functions 7

Passing int/str/float/bool arguments into functions 4

Calling a function 3

List syntax 2

Return vs print 1

Type the following in script mode
---------------------------------
my_list = ['a', 'b', 'c', 'd']
# input: a list of strings
# output: None
def my_function(list_argument):
    list_argument[0] = 'z'
print(my_list)
my_function(my_list)
print(my_list)
What did the program output and what is this program doing? it output ['a','b','c','d'] then ['z','b','c','d']. it changes the first letter to z


Try writing a similar program but passing in integers instead of a list. What happens? it just made it numbers
'''
my_list = ['a','b','c','d']
def my_function(list_argument):
    list_argument[0] = 'z'
print(my_list)
my_function(my_list)
print(my_list)


list2 = [1,2,3,4]
def func1(list_argument):
    list_argument[0] = 9
print(list2)
func1(list2)
print(list2)
