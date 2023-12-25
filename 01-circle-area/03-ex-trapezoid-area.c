#include <stdio.h>

/* trapezoid_area - calculates the area of a trapazoid.
 * @a: is the given trapezoid first base.
 * @b: is the given trapezoid second base.
 * @h: is the given trapezoid height.
 *
 * Return: the trapezoid area after calculation.
 */
float trapezoid_area(float a, float b, float h)
{
    float A = (0.5 * (a + b)) * h;
    return A;
}

int main()
{
  float result = trapezoid_area(10.7, 8.5, 5); // random values for testing
  printf("Result: %f\n", result); // It'll print 48.0
}
