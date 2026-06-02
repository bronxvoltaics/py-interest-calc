#query user for initial value, apr, and time;
#store those values in variables
print("enter initial value");
init = float(input());

print("enter apr");
apr = float(input()) / 100;

print("enter time");
time = int(input());

#compound interest using init, apr, time.
#store the calculation in final_value
final_value = (1+apr) ** time * init;

#spit out final_value to the user
print("final value = " + str(final_value))
