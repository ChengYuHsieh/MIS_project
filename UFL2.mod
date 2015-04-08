set I;
set J;
param d{i in I, j in J}; #shipping cost per unit
param h{i in I}; #demand quantity 
param f{j in J}; #fixed cost to build a facility

var X{j in J} >= 0; #whether to build a facility
var Y{i in I, j in J} >= 0; #each customer should be served 

minimize Z: ( sum{i in I, j in J} h[i]*d[i, j]*Y[i, j] ) + ( sum{j in J}f[j]*X[j] );
subject to Facility{i in I}: sum{j in J} Y[i,j] = 1; 
subject to Uperbound{i in I, j in J}: Y[i, j] <= X[j];


