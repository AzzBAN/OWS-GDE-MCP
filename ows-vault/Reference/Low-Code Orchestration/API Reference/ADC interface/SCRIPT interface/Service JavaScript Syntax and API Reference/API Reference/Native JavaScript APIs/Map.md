---
title: "Map"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_032.html"
depth: 7
---
# Map

**Table 1** Map APIs supported by service JavaScript   
| API | Description | Example |
| :-- | :-- | :-- |
| new Map() | Creates a Map object. The Map object saves key-value pairs and stores the original insertion sequence of keys. Any value (object or base type) can be used as a key or a value. | 
Creating a Map object: var map = new Map();

 |
| size | Accessibility property, which is used to return the number of members of a Map object. | const map1 = new Map();

map1.set('a', 'apple');
map1.set('b', 'boy');
map1.set('g', 'girl');

console.log(map1.size);
// expected output: 3

 |
| clear() | Removes all elements from a Map object. | const map1 = new Map();
map1.set('bench', 'baz');
map1.set(1, 'zoo');
console.log(map1.size);
// expected output: 2
map1.clear();
console.log(map1.size);
// expected output: 0

 |
| delete() | Removes a specified element from a Map object. | const map1 = new Map();
map1.set('boy', 'food');
console.log(map1.delete('boy'));
// expected result: true
// (true indicates successful removal)
console.log(map1.has('boy'));
// expected result: false

 |
| entries() | Returns a new iterator object that contains the key-value pair. The iteration sequence of the returned iterator is the same as the insertion sequence of the Map object. | const map1 = new Map();
map1.set('0', 'food');
map1.set(1, 'boy');
const iterator1 = map1.entries();
console.log(iterator1.next().value);
// expected output: \["0", "food"\]
console.log(iterator1.next().value);
// expected output: \[1, "boy"\]

 |
| forEach() | Executes a given function for each key-value pair in the Map object in the insertion sequence. | function logMapElements(value, key, map) {
  console.log(\`m\[${key}\] = ${value}\`);
}
new Map(\[\['food', 4\], \['bar', {}\], \['baz', undefined\]\])
  .forEach(logMapElements);
// expected output: "m\[food\] = 4"
// expected output: "m\[boy\] = \[object Object\]"
// expected output: "m\[baz\] = undefined"

 |
| get() | Returns a specified element in a Map object. | const map1 = new Map();
map1.set('boy', 'food');
console.log(map1.get('boy'));
// expected output: "food"
console.log(map1.get('baz'));
// expected output: undefined

 |
| has() | Returns a Boolean value indicating whether the specified element exists in the Map object. | var myMap = new Map();
myMap.set("boy", "food");
myMap.has("boy");  // returns true
myMap.has("baz");  // returns false

 |
| keys() | Returns an iterator object of a key. It contains the key value of each element inserted into the Map object in sequence. | const map1 = new Map();
map1.set('0', 'food');
map1.set(1, 'boy');
const iterator1 = map1.keys();
console.log(iterator1.next().value);
// expected output: "0"
console.log(iterator1.next().value);
// expected output: 1

 |
| set() | Adds or updates a key-value pair with a specified key and value for a Map object. | const map1 = new Map();
map1.set('boy', 'food');
console.log(map1.get('boy'));
// expected output: "food"
console.log(map1.get('baz'));
// expected output: undefined

 |
| values() | Returns a new iterator object. It contains the value of each element inserted into the Map object in sequence. | var myMap = new Map();
myMap.set("0", "food");
myMap.set(1, "boy");
myMap.set({}, "baz");
var mapIter = myMap.values();
console.log(mapIter.next().value);
 // "food"
console.log(mapIter.next().value);
 // "boy"
console.log(mapIter.next().value);
 // "baz"

 | **Parent topic:** [[Native JavaScript APIs|Native JavaScript APIs]]