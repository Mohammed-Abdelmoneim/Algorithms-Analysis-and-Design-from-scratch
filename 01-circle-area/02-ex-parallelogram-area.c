#include <stdio.h>

/* parallelo_area - calculates the area of a parrallelogram.
 * @b: is the given parallelogram base.
 * @h: is the given parallelogram height.
 *
 * Return: the parallelogram area after calculation.
 */
float parallelo_area(float b, float h)
{
    float a = b * h;
    return a;
}

int main()
{
  float result = parallelo_area(10.7, 8.5);
  printf("Result: %f\n", result);
}
