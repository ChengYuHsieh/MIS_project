#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<fstream>
#include<time.h>
#include<string>
#include<sstream>
#include<math.h>
using namespace std;

int main(int argc, const char * argv[])
{
	int num,m,n,hbar,dbar,fbar;
	
	srand((unsigned)time(NULL));
	num =  atoi(argv[1]);
	m = atoi(argv[2]);
	n = atoi(argv[3]);
	hbar = atoi(argv[4]);
	dbar =atoi(argv[5]);
	fbar = atoi(argv[6]);
	
	// printf("%s","The number of instance: ");
	// scanf("%d", &num);
	// printf("%s","The number of demand: ");
	// scanf("%d", &m);
	// printf("%s", "The number of facility: ");
	// scanf("%d", &n);
	// printf("%s", "Quantity Limit H-bar: ");
	// scanf("%d", &hbar);
	// printf("%s", "Distance Matrix D-bar: ");
	// scanf("%d", &dbar);
	// printf("%s", "Fix Cost Limit F-bar: ");
	// scanf("%d", &fbar);	
	// cout << endl;
	for(int i=0; i<num; i++)
	{
		int hi,fj,dij;
		string t,s = "output";
		stringstream ss(t);
		ss << i+1;
		s += ss.str();
		s += ".txt";
		cout << "File Name: "<< s << endl;
		cout << "m= " << m << endl;
		cout << "n= " << n << endl << endl;
		ofstream outfile(s.c_str());
		outfile << m << endl;
		outfile << n << endl;
		cout << "hi: ";
		for(int j=0; j<m; j++)
		{
			hi = rand() % hbar + 1;
			cout << hi << " ";
			outfile << hi << " ";
		}
		cout << endl ;
		outfile << endl;
		
		//int p[dbar][dbar], d[m][n];
		int **p = new int *[dbar];
		for(int j=0; j<dbar; j++)
		{
			p[j] = new int [dbar];
		}
		int **d = new int *[m];
		for(int j=0; j<m; j++)
		{
			d[j] = new int [n];
		}		
		//cout << "~~~~~~~~~~~~~~~~";
		for(int j=0; j<dbar; j++)
		{
			for(int k=0; k<dbar; k++)
			{
				p[j][k] = 0;
			}
		}
		for(int j=0; j<m; j++)
		{
			for(int k=0; k<n; k++)
			{
				d[j][k] = 0;
			}
		}
		//cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
		for(int j=1; j<=m; )
		{
			int r = rand() % (dbar*dbar);
			if(p[r/dbar][r%dbar] == 0)
			{
				p[r/dbar][r%dbar] = -j;
				cout << "No." << j << " demand: p(" << r/dbar << "," << r%dbar << ")= " << -j << endl;
				j++;
				outfile << r/dbar << " " << r%dbar << endl ;
			}
		}
		cout << endl;
		cout << "fj: ";
		for(int j=0; j<n; j++)
		{
			fj = rand() % fbar + 1;
			cout << fj << " ";
			outfile << fj << " ";
		}
		cout << endl ;
		outfile << endl;
		
		for(int j=1; j<=n;)
		{
			int r = rand() % (dbar*dbar);
			if(p[r/dbar][r%dbar] == 0)
			{
				p[r/dbar][r%dbar] = j;
				cout << "No." << j << " Supply: p(" << r/dbar << "," << r%dbar << ")= " << j << endl;
				j++;
				outfile << r/dbar << " " << r%dbar << endl;
				
				for(int k=0; k<dbar*dbar; k++)
				{
					if(p[k/dbar][k%dbar] < 0)
					{
						int ith = -p[k/dbar][k%dbar];
						int jth = p[r/dbar][r%dbar];
						d[ith-1][jth-1] = sqrt(pow(k/dbar - r/dbar,2)+ pow(k%dbar - r%dbar,2));
					}
				}
			}
		}		
		cout << endl << endl;
		cout << "Dij";
		for(int j=0; j<n; j++)
		{
			cout << " " << j+1 << ".";
		}
		cout << endl;
		for(int j=0; j<m; j++)
		{
			cout << "" << j+1 << ". ";
			for(int k=0; k<n; k++)
			{
				cout << d[j][k] << " ";
				outfile << d[j][k] << " ";
			}
			cout << endl ;
			outfile << endl;
		}		
		for(int j=0; j<dbar; j++)
			delete []p[j];
		delete []p;
		for(int j=0; j<m; j++)
			delete []d[j];
		delete []d;
	}
	
	return 0;
}


