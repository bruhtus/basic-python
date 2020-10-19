### Report

#### Tuples

> once a tuple is created, we cannot change its values. we cannot use add, insert, remove methods in a tuple.

Methods related to tuples:
- tuple(): to create an empty tuple.
- count(): to count the number of a specified item in a tuple.
- index(): to find the index of a specified item in a tuple.

Slicing tuples basically the same as slicing list.

If only one item in tuple, you need to do this: `tpl = ('item', )`.

#### Sets

> set is a collection of unordered and unindexed distinct elements. in python, set is used to store unique items and it is possible to find the union, intersection, difference, symmetric difference, subset, super set, and disjoint set among sets.

Creating empty set: `st = {}`.

removing items in sets is still ordered from first to last but print the set is unordered. so if you add items to your sets then it's gonna be on the last order but if you print the sets, it's position is random (unordered).

there're two ways to remove an item in set, using remove() method or discard() method. The difference between the two is that if the item is not found in set then remove() method will raise an errors, however discard() method doesn't raise any errors.

finding symetric difference in set means display item in set 1 minus item in set 2 (doesn't show item in set 1 and in set 2).

if two sets do not have a common item or items, we call them disjoint sets.

#### Dictionaries
> dictionary is a collection of unordered, modifiable paired (key:value) data type.
