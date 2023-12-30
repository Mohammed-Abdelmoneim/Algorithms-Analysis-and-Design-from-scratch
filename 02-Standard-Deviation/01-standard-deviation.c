#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float std_dev()
{
  int i;
  float sd = 0, ave = 0, n, a, b;
  float *x;

  // Get the total number from the user
  printf("Enter total numbers: ");
  scanf("%f", &n);

  // allocate space for x in the memory
  x = malloc(sizeof(float) * n);

  // loop to get the x values
  for (i = 0; i < n; i++)
  {
    printf("x[%d]:", i);
    scanf("%f", &x[i]);
    ave += x[i];
  }

  // get the ave value
  ave = ave / n;

  // loop to get the a value 
  for (i = 0; i < n; i++)
  {
    a += pow((x[i] - ave), 2);
  }

  b = a / n;

  sd = sqrt(b);
  
  printf("%f\n", sd);

  free(x);
  return sd;
}

int main()
{
  std_dev();
  return (0);
}
