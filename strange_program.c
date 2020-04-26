#include <stdio.h>  	 	    
#include	<stdlib.h>
    void 	printTriangle(  char * 		input);
void	floatsAreBadLoopCounters();
   void whatNumberIsGMU( 	int num	 )	  ;
int	main(){
     	 int count 		 =1;
char	*input[50];
 for( count;  count 		<	10;	count++ )		{
printf("NOTIMEFORTALKINGGOTTAPAINTMYSPACESWHITE\n")	;
 count   = 		 	count	%10  ;
	}printf("WHATNUMBERISGMUCYBERSECURITY??\n");
      		 int  	num=getchar();
whatNumberIsGMU(num)	;
printf("Let's   make a 			 triangle!!!!!! 		\n")
	;
  fgets(   input	 ,	50 ,stdin	  );
	
      		printTriangle(  input	)	;
	
     		 			 
	
     	 		}			
	
     			 	  
	
      	void	printTriangle(  char  *input){
int	i,j;
  for(  i=1 	; i<=	sizeof(input)	;	++i		)
	{
  for   (		j=1	; j<	  i;++j)
	{
   printf("%c",input[j]);  	  	   
printf("	\n");
     		  	 	}
	}
     	 					}
	
  void   whatNumberIsGMU(			int num 		)
	{
  for  ( num 	;	num> 0; num-- 	)
	{
   printf(" GMU IS		NOT NUMBER	%d	 \n ",num);
	}
   printf("  GMU	IS NUMBER  	1!!!!!!! \n"	);
	}
    void 	floatsAreBadLoopCounters()	 			 {
float	demo=0.0;
    for (	 demo ; demo< 	99999999	;demo+=20000)
	{
 printf(" This   is 		  why	you	dontusefloatsasloopcounters:%.02f\n",demo)
	;
}     					 	
}	
//hello  there