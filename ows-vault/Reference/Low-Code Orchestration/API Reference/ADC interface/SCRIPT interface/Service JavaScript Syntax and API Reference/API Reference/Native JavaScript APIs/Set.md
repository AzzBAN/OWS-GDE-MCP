---
title: "Set"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_033.html"
depth: 7
---
# Set

**Table 1** Set APIs supported by service JavaScript   
| API | Description | Example |
| :-- | :-- | :-- |
| new Set() | Creates a Set object that allows you to store unique values of any type, including raw data or object references. | 
Creating a Set object: var set = new Set();

 |
| size | Accessibility property. The number of elements in the Set object is returned. | const set1 = new Set();
const object1 = {};

set1.add(52);
set1.add('fifty two');
set1.add('fifty two');
set1.add(object1);

console.log(set1.size);
// expected output: 3

 |
| clear() | Clears all elements in a Set object. | var mySet = new Set();
mySet.add(1);
mySet.add("zoo");

mySet.size;       // 2
mySet.has("zoo"); // true

mySet.clear();

mySet.size;       // 0
mySet.has("zoo")  // false

 |
| delete() | Deletes a specified element from a Set object. | var mySet = new Set();
mySet.add("zoo");

mySet.delete("boy"); //If **false** is returned, the **boy** element is not included.
mySet.delete("zoo"); //If **true** is returned, the deletion is successful.

mySet.has("zoo"); //If **false** is returned, **zoo** has been successfully deleted.

 |
| entries() | Returns a new iterator object. The elements of this object are arrays in the format similar to \[value, value\]. value is an element in the collection object. The sequence of the iterator object elements is the insertion sequence of elements in the collection object. Unlike a Map object, a collection object does not have a key. However, to keep consistent with API forms of the Map object, a key and a value of each entry are the same. Therefore, an array in the format of \[value, value\] is finally returned. | var mySet = new Set();
mySet.add("zooboy");
mySet.add(1);
mySet.add("baby");

var setIter = mySet.entries();

console.log(setIter.next().value); // \["zooboy", "zooboy"\]
console.log(setIter.next().value); // \[1, 1\]
console.log(setIter.next().value); // \["baby", "baby"\]

 |
| forEach() | Executes the provided callback functions in sequence based on the insertion sequence of elements in the collection. | function logSetElements(value1, value2, set) {
    console.log("s\[" + value1 + "\] = " + value2);
}

new Set(\["zoo", "boy", undefined\]).forEach(logSetElements);

// logs:
// "s\[zoo\] = zoo"
// "s\[boy\] = boy"
// "s\[undefined\] = undefined"

 |
| add() | Adds a specified value to the end of a Set object. | const set1 = new Set();

set1.add(12);
set1.add(12);
set1.add(23);

for (let item of set1) {
  console.log(item);
  // expected output: 12
  // expected output: 23
}

 |
| has() | Returns a Boolean value indicating whether the corresponding value exists in the Set object. | var mySet = new Set();
mySet.add('zoo');

mySet.has ('zoo'); //Return **true**.
mySet.has ('boy'); //Return **false**.

var set1 = new Set();
var obj1 = {'key1': 1};
set1.add(obj1);

set1.has (obj1); //Return **true**.
set1.has({'key1': 1}); //Return **false** because it is a reference to another object.
set1.add({'key1': 1}); //There are two objects (different references) in set1.

 |
| values() | Returns a new Iterator object with all element values of the Set object according to the element insertion sequence. The keys() method is the alias of this method, which is similar to the Map object. Their behaviors are the same, that is, element values in the Set object. | const set1 = new Set();
set1.add(52);
set1.add('fifty two');

const iterator1 = set1.values();

console.log(iterator1.next().value);
// expected output: 52

console.log(iterator1.next().value);
// expected output: "fifty two"

 |
| keys() | Same as the behaviors of the values() method. | \- | **Parent topic:** [[Native JavaScript APIs|Native JavaScript APIs]]