# Shopping Basket

## Requirements

You have been asked to implement a "atomic weight" pricing function for a science project.

This is a comoponent which if given a chemical formula returns the atomic weight of that substance as a floating-point number. 

The developer who worked on this project (briefly) only implemented the minimum required to make a very small collection of tests pass. You should expand these tests and the implementation accordingly. In order to deliver this assignment you will have to fully implement at least two incomplete functions. 

You have been given a data file [periodic_table.json](periodic_table.json) which contains all of the information needed for this function to work.

### Definitions

* **formula**: A string consisting of uppercase and lowercase letters plus numbers which specify a chemical compound.
* **element**: One of the basic substances of the universe, most commonly in the Periodic Table.
* **symbol**: A 1-3 char string, that is a UID for an element in the Periodic Table.

### Behavior

The required behavior has been written into the comments in [atomic_weight.py](atomic_weight.py) and [periodic_table.py](periodic_table.py)

#### Other considerations

* You can create as many other functions, modules and tests as you think you need.
* Please ensure your code has been formatted with the [Black](https://github.com/psf/black) code formatting tool.
* Please use [Pytest](https://docs.pytest.org/en/latest/) to build your unit-tests. Please follow a TDD (Test Driven Development) approach.
* You can use 3rd party component if you think it will be helpful, for example in your testing. Use the included [Pipfile](Pipfile) to identify any dependencies your component needs. 
* Provide some documentation that will help us run your submission. You can put your documentation in [the readme file](./readme.md)

## Examples

```python
>>> from atomic_weight import get_atomic_weight_for_compound
>>> get_atomic_weight_for_compound("O2")
31.998
>>>
```
