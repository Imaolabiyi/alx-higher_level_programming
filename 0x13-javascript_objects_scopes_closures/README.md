Working on 0x13. JavaScript - Objects, Scopes and Closures
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/node
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
All your files must be executable
The length of your files will be tested using wc
You are not allowed to use var
More Info
Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard
Documentation

$ sudo npm install semistandard --global
Tasks
0. Rectangle #0
mandatory
Write an empty class Rectangle that defines a rectangle:

You must use the class notation for defining your class
1. Rectangle #1
mandatory
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
2. Rectangle #2
mandatory
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
3. Rectangle #3
mandatory
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
4. Rectangle #4
mandatory
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
Create an instance method called rotate() that exchanges the width and the height of the rectangle
Create an instance method called double() that multiples the width and the height of the rectangle by 2
5. Square #0
mandatory
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

You must use the class notation for defining your class and extends
The constructor must take 1 argument: size
The constructor of Rectangle must be called (by using super())
6. Square #1
mandatory
Write a class Square that defines a square and inherits from Square of 5-square.js:

You must use the class notation for defining your class and extends
Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
7. Occurrences
mandatory
Write a function that returns the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)
8. Esrever
mandatory
Write a function that returns the reversed version of a list:

Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
9. Log me
mandatory
Write a function that prints the number of arguments already printed and the new argument value. (see example below)

Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument value>
10. Number conversion
mandatory
Write a function that converts a number from base 10 to another base passed as argument:

Prototype: exports.converter = function (base)
You are not allowed to import any file
You are not allowed to declare any new variable (var, let, etc..)
11. Factor index
#advanced
Write a script that imports an array and computes a new array.

Your script must import list from the file 100-data.js
You must use a map. Tips
A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
Print both the initial list and the new list
12. Sorted occurences
#advanced
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

Your script must import dict from the file 101-data.js
In the new dictionary:
A key is a number of occurrences
A value is the list of user ids
Print the new dictionary at the end
13. Concat files
#advanced
Write a script that concats 2 files.

The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination

