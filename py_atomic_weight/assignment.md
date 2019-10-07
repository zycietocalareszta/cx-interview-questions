# Shopping Basket

## Requirements

You have been asked to implement a "atomic weight" pricing function for a science project. This is a component which if given a chemical formula returns the atomic weight of that compound as a floating-point number. 

```python
>>> from atomic_weight import get_atomic_weight_for_compound
>>> get_atomic_weight_for_compound("O2")
31.998
>>>
```

The developer who worked on this project only implemented the minimum required to make a very small collection of tests pass. The tests are incomplete and do not capture the desired full behavior of the system. You should expand these tests and the implementation accordingly. In order to deliver this assignment you will have to fully implement two functions which are currently stubbed out. You can add as many more functions as you need.

You have been given a data file, [periodic_table.json](periodic_table.json) which contains all of the information needed for this function to work.

### Definitions

* **formula**: A string consisting of **symbols** and numbers plus numbers which specify a chemical compound. 
* **element**: One of the basic substances of the universe, most commonly in the Periodic Table.
* **compound** A substance made from one or more elements. It can be specififed by a "chemical formula".
* **symbol**: A 1-3 char string, that is a UID for an element in the Periodic Table. Examples of valid symbols are "H" (Hydrogen), "He" (Helium). "Hen" is not a valid symbol because it does not appear in the Periodic Table.
* **atomic weight**: Also called "relative atomic weight" is the average weight of an atom's mass relative to a standard mass. The atomic weight of a compound is sum of it's constituent atom's atomic mass.

### Behavior

The required behavior has been written into the comments in [atomic_weight.py](atomic_weight.py) and [periodic_table.py](periodic_table.py)

#### Other considerations

* You can create as many additional functions, modules and tests as you think you need.
* Please ensure your code has been formatted with the [Black](https://github.com/psf/black) code formatting tool.
* Please use [Pytest](https://docs.pytest.org/en/latest/) to build your unit-tests. Please follow a TDD (Test Driven Development) approach.
* You can use any 3rd party component if you think it will be helpful. Expand the included [Pipfile](Pipfile) to identify any dependencies your component needs. 
* Provide some documentation that will help us run your submission. You can put your documentation in [the readme file](./readme.md)

## Bonus

* Ensure that all declarations have type annotations. Use the mypy type-checking tool to verify your types are correct and consistent. Please provide a shell-script that will allow us to quickly verify that the types are correct and consistent.
