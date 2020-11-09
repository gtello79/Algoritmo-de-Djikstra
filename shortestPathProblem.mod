reset;

option solver gurobi;
option gurobi_option 'outlev=1 mipgap 0.01 bestbound 1 logfile "./logfile.txt"';

param nodes;
data nodes.dat;

solve;