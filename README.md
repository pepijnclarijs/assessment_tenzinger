# Assessment Tenzinger

## Code Notes

When making this application I tried to keep in mind, as much as possible, that people from HR probably do not have
a lot of coding experience. For this reason I tried to make it very user-friendly. 

In general, when coding in python, I use PEP 8 styling. I find that following this styling makes it easier to be 
consistent. 

I put assertions in the calc_travel_comp function itself so that these general mistakes are also taken care of when the 
function would be used somewhere else.

In calc_travel_comp I give the option to pass along a directory to save the output in so that the output path can easily
be changed. I ask users to first create the directory themselves because it would be easy to make some spelling error in
the input, which could cause the directory to be created in weird places.

I chose to make a new table inside the csv for each month because I think it is more readable for HR than it would be if
I would keep adding columns for different months.

For the sake of simplicity, I assumed no holidays and that each month has 4.5 weeks. Of course in practice the number of
actual workdays per month should calculated more carefully. Things like holidays and leap year should be taken into 
account.


## Used Libraries

I use the csv library to handle csv related tasks. If there is a library, it's probably better to use it than to 
reinvent the wheel.

I use the os library because I've found that it makes working with paths a lot easier.

timedelta and date from the datetime library are used for date related tasks.

I use Path from pathlib to convert strings to paths. 
