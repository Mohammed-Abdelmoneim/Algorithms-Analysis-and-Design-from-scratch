#include <stdio.h>

/* circle_area - calculates the area of a circle.
 * @r: in the given cirlce radius.
 *
 * Return: the circle area after calculation.
 */
float circle_area(float r)
{
  float a = 3.1415 * (r * r);
  return (a);
}

int main()
{
  float result = circle_area(10);
  printf("Result: %f\n", result);
}
