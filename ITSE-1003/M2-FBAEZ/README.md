# M2-FBAEZ - Pet Management System

Mini project for Module 2 focused on Object-Oriented Programming with inheritance.

## Objective

Build a simple pet management system that:

- defines `Dog` and `Puppy` classes,
- creates at least 2 dogs and 1 puppy,
- stores objects in a list,
- loops through the list to print descriptions and call methods.

## Main File

- `pet_management_system.py`

## Implemented Features

- Base class `Dog` with:
  - attributes `name` and `age`,
  - method `describe()`,
  - method `bark()`.
- Derived class `Puppy` that inherits from `Dog` and adds:
  - method `play()`.
- Input validation for `age`:
  - prevents negative values,
  - enforces integer type.
- Main flow with a pet list and output loop.

## Execution

From the repository root:

```bash
python ITSE-1003/M2-FBAEZ/pet_management_system.py
```

## Expected Output (Example)

```text
Buddy is 3 years old
Woof!
Rocky is 5 years old
Woof!
Max is 1 years old
The puppy is playing!
```

## Covered Rubric Criteria

- Class design and OOP structure
- Constructor and attributes
- Methods and functionality
- Inheritance
- Object creation and list-based management
- Loop-driven program flow and output
- Input validation
- Code readability
