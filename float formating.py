#how to formate the float
#we can control degit after decimal point by three method
#1 round,2 percentage, 3string formating
x=float(input('ENTER NUMERATOR:'))
y=float(input('ENTER DENOMENATOR:'))
result=x/y
#upto two decimal figure we can we round(variable,uptu2 decimal
result1=round(result,1)
print('THE RESULT IS =',result1)
# % method use for roundoff figure "%.3f"% variable
print('THE RESULT IS= %.2f'%result)

# string format use
print('THE RESULT IS={:.3f}'.format(result))
#thanks akhlakansari94@gmail.com