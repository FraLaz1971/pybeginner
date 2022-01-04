# ##################################
# python3 examples for beginners  ##
# ##################################

## Pay Attention!! you may get errors if executed using python2 interpreter

# pybeginner
# ##################################
Contains few programming examples to that can be run 
using python3 interpreter, to exercise and modify at your choice.
# ##################################

- exp.py --> execute exponentiation of 2 numbers in input
              as program arguments from the command line
- inpar.py ---> shows program input parameters

- myplot.py ---> matplotlib example: shows squares points

- salary.py ---> shows gross salary report for 1 employee

- stud.py ---> shows student grades average

- sum2.py ---> sum2 2 numbers

- README --> this file, contains explanations about the programs
## How to run the examples
### Using python IDLE
All the examples can be run using a Graphical User Interface
based tool or Integrated Development Environment, the most
suitable to start is the python IDLE Integrated Development and Learning Environment
that is shipped with most of the python installation packages.
You just have to open the example you want to run in the python IDLE
and select from the drop-down menu Run ---> Run Module F5
![run example in python IDLE](howtorun.png "how to run an example in the python IDLE
Integrated and Learning Environment")

### Using a shell terminal 
You may use a shell terminal to run this examples.
we are supposing your python (version 3) interpreter is called python3
### or python3.exe on MS win
### (it may be called python or python.exe on MS win)
## usage:
## it's possible to run the examples on the shell terminal
## or on python IDLE or your favourite IDE
## Integrated Desktop Environment
## console terminal on Unix-like (GNU/Linux, MacOS, ...)
## example running on bash terminal

python3 <program.py>
### or
python <program.py>
#
python3 <program.py>
#
./python3 <program.py>
### on MS win it may be just
python <program.py>
### or
python3 <program.py>
#
.\python <program.py>
### or 
.\python3 <program.py>
### where <program.py> it is a placeholder for the actual
### python source code file
./inpar.py arg otherarg this 3 33
Number of arguments: 6 arguments.
Argument List: ['./inpar.py', 'arg', 'otherarg', 'this', '3', '33']
#
### it may be
expr.py example
#
./myplot.py
![myplot results](awesome.png "myplot.py giving results")
#
./inpar.py arg otherarg this 3 33
Number of arguments: 6 arguments.
Argument List: ['./inpar.py', 'arg', 'otherarg', 'this', '3', '33']
#
py>./salary.py
*************************
** enter employee details
** name, hourly rate and
** number of hours worked
** and get salary report
*************************
employee_name:John Smith
hourly_rate ($):12
number_of_hours:300

*************************
Employee: John Smith
Gross_salary: 3600.0 $
*************************
Bye.
*************************
#
py>./salary.py < salin.csv 
*************************
** enter employee details
** name, hourly rate and
** number of hours worked
** and get salary report
*************************
employee_name:hourly_rate ($):number_of_hours:
*************************
Employee: Calvin Harris
Gross_salary: 5000.0 $
*************************
Bye.
*************************
