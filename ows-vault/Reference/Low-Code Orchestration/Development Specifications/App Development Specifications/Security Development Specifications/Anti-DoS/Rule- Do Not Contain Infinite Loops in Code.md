---
title: "Rule: Do Not Contain Infinite Loops in Code"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363621.html"
depth: 5
---
# Rule: Do Not Contain Infinite Loops in Code

**Description**: During asset development, GDE supports service logic processing using the script language. For example, the infinite loops of a script usually occur when the for loop and while loop cannot exit due to improper condition settings. The infinite loops may use up CPU computing resources, causing unavailable system. As a result, the infinite loop cannot occur in the code.

**Check guide**: Check whether there is any loop that cannot end due to the existence of a for or while statement block. For example, the common infinite loop expressions are while(true), for(;true;), and for(;;).

**Compliance requirements**:

1.  Do not update the loop control variable in the loop body.
2.  When the update step of the cyclic control variable changes dynamically, prevent the reverse update step or zero increase.
3.  Do not use the do{}while(_loop condition_){_update loop control variable_;} loop.
4.  Use the for loop instead of the while loop.
5.  Do not include the for loop control variable update in the condition statement.
6.  Check whether cyclic dependency occurs when a module is loaded using the require() method of JS.

**Involved scenarios**:

Service scripts compiled using JS and command scripts compiled using Python or Ruby

**Negative example 1**:

for(i=0;i<1;i--) {
 xxxx 
}

In the preceding example, the value of **i** is never greater than 1, causing an infinite loop.

var i= 0; 
while(i < 100) {
 //i++ ......
}

In the preceding example, if you forget to write the incremental expression of **i**, an infinite loop occurs.

**Incorrect example 2**: The recursion does not check the calling interface.

function check(){ 
//xxxx check() 
//xxxx 
}

**Incorrect example 3**: i++ is required only when the while condition is not met, but the loop does not end.

function test(){ 
var x = " "; 
var i = 0; 
do{ 
    x = x +"The number is"+i; 
}while(i<5){ 
    i++; 
} 
}

**Negative example 4**: A cyclic dependency occurs on the common function require() of JS.

//Common function/a/a/a:
//do something
require("/b/b/b")
//do something

//Common function/b/b/b:
//do something
require("/a/a/a")
//do something

**Note**: Only basic infinite loops in the JS script can be checked. Infinite loops in the Python or Ruby script cannot be checked. Other infinite loops need to be manually checked.

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_Script\_ProhibitInfiniteLoop

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Anti-DoS|Anti-DoS]]