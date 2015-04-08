set I;
param d{i in I}; #shipping cost per unit
param h{i in I}; #demand quantity
param l{i in I};#Lagrangian multiplier 
param f; #fiXed cost to build a facility
var X binary; #whether to build a facility
var Y{i in I}>= 0; #each customer should be served 
minimize Z: sum{i in I} ((h[i]*d[i]-l[i])*Y[i])+f*X;
subject to Uperbound{i in I}: Y[i]<= X;


