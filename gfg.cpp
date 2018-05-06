/* file : gfg.c */
 
#include <stdio.h>
#include <math.h>
#include <jni.h>
 
//our header file
#include "gfg.h"
#define ll long long
 

JavaVM *jvm;
JNIEnv* env;
 
// calculate factorial
ll int fact(ll int n)
{
    if(n <= 1)
        return 1;
    else
        return (n * fact(n-1));
}
 
//find mod
int my_mod(int n, int m)
{
  return(n % m);
}


void vm()
{

	 JavaVMInitArgs args;
	 JavaVMOption options;
	 args.version = JNI_VERSION_1_8;
	 args.nOptions = 1;
	 options.optionString = "-Djava.class.path=jsapi.jar";

	 args.options = &options;
	 args.ignoreUnrecognized = 0;
	 int rv;
	 rv = JNI_CreateJavaVM(&jvm, (void**)&env, &args);
	 if (rv < 0 || !env)
	     printf("Unable to Launch JVM %d\n",rv);
	 else
	     printf("Launched JVM! :)\n");
	 

}


int main(){
	vm();
	return 0;
}