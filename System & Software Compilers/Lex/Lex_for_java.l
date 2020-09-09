%{
	#include<stdio.h>
	FILE* yyin;
%}

Digit [0-9]
Number {Digit}+
Real {Digit}*[.]{Number}
Text [A-Za-z]
Keyword "class"|"static"
DataType "int"|"float"|"double"|"char"|"long"|"String"
ConditionalKeyword "if"|"else"|"else if"|"switch"|"case"
IterativeKeyword "for"|"while"|"do"
Preprocessor "import"[^\n]*";"
Sc ";"
RelationalOperator "<="|"=="|">="|"!="|"<"|">"
Identifier {Text}({Digit}|{Text}|"_")*
ArithmeticOperator "+"|"-"|"/"|"*"|"%"
LogicalOperator "&&"|"||"|"!"
AccessSpecifier "public"|"private"|"protected"
PrintStmnt "System.out.println"[^\n]*";"
Function {AccessSpecifier}{DataType}{Identifier}"("[^\n]*";"
	
%%
[ \n\t]+ ;
{Preprocessor} {printf("%s\t--> Preprocessor\n",yytext);}
{ConditionalKeyword} {printf("%s\t--> Conditional Keyword\n",yytext);}
{IterativeKeyword} {printf("%s\t--> Iterative Keyword\n",yytext);}
{DataType} {printf("%s\t--> Datatype\n",yytext);}
{AccessSpecifier} {printf("%s\t--> Access Specifier\n",yytext);}
{Keyword} {printf("%s\t--> Keyword\n",yytext);}
{Identifier} {printf("%s\t--> Identifier\n",yytext);}
{Real} {printf("%s\t--> Real number\n",yytext);}
{Number} {printf("%s\t--> Number\n",yytext);}
{Sc} {printf("%s\t--> Semi Colon\n",yytext);}
{ArithmeticOperator} {printf("%s\t--> Arithmetic Operator\n",yytext);}
{LogicalOperator} {printf("%s\t--> Logical Operator\n",yytext);}
{RelationalOperator} {printf("%s\t--> Relational Operator\n",yytext);}
{PrintStmnt} {printf("%s\t--> Print Statement\n",yytext);}
"=" {printf("%s\t--> Assignment Operator\n",yytext);}
"{" {printf("%s\t--> Block Starts\n",yytext);}
"}" {printf("%s\t--> Block Ends\n",yytext);}
"(" {printf("%s\t--> Paranthesis Starts\n",yytext);}
")" {printf("%s\t--> Paranthesis Ends\n",yytext);}
. ;

%%

int yywrap()
{
	return 1;
}
int main(int argc, char* argv[])
{
	yyin = fopen(argv[1],"r");
	yylex();
	yywrap();
	fclose(yyin);
	return 0;
}