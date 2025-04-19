# My Library

## Overview
This project is a collection of mathematical and geometric operations implemented as macros in C. It includes functionalities for basic arithmetic operations, area calculations for various shapes, unit conversions, and factorial computation.

## Files
- **include/Calculator.h**: Defines macros for basic arithmetic operations such as addition, subtraction, multiplication, division, power of 2, square root, and cube root.
- **include/Area.h**: Contains macros for calculating the area of geometric shapes including square, rectangle, triangle, and circle, along with the constant PI.
- **include/Convert.h**: Provides macros for unit conversions, including temperature (Celsius to Fahrenheit and vice versa), length (metres to feet and vice versa), and volume (litres to cubic feet and vice versa).
- **include/Fact.h**: Defines a multiline macro for calculating the factorial of a number.

- **src/First.c**: A console application for performing basic arithmetic operations using the macros defined in Calculator.h.
- **src/Second.c**: A console application for calculating the area of different shapes using the macros defined in Area.h.
- **src/Third.c**: A console application for performing various unit conversions using the macros defined in Convert.h.
- **src/Fourth.c**: A console application for calculating the factorial of a number using the macro defined in Fact.h.

## Installation
To compile the project, use the provided Makefile. Navigate to the project directory and run:

```
make
```

This will compile all the source files and create the executable programs.

## Usage
After compiling, you can run each program as follows:

- For basic arithmetic operations:
  ```
  ./First
  ```

- For area calculations:
  ```
  ./Second
  ```

- For unit conversions:
  ```
  ./Third
  ```

- For factorial calculation:
  ```
  ./Fourth
  ```

Follow the on-screen prompts to input values and select operations.