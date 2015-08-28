console.log("hello world!");
/*

string = text thats stored in a variable
int = integer, a whole number
double/float = decimal 
boolean = true/false

*/

/*
Ex. 0
*/

var x = 10;
console.log(x);
x = "Hello World!";
console.log(x);


/*
Ex. 1
*/

var omead = "is scrumming by himself";
omead = "is pretty good at demoing";
console.log(omead);

/*
Ex. 2
*/

var numberOfDemos = 109;
console.log(numberOfDemos);
numberOfDemos = "Brancato demos like a boss";
console.log(numberOfDemos);

/*
Ex. 3
*/

var Sally = 10;
var Johnny = 15;
var Jill = 25;
var Peter = 5;

if((Sally > 5 && Jill == 20) || (Peter != 8 && Johnny > 10)){
  console.log("Success!");
}
else{
  console.log("Nooooo...");
}

/*
&& - AND logic
|| - OR logic
*/

1a yxb 

if((x <= y && a < y ) || (y < x && b > a)){
  console.log("success!");
}
else{
  console.log("no!");
}

/* 
Ex. 4 
*/

if(x < y)
  console.log("success!");

else
  console.log("fail!");

/*
Ex. 5
functions
*/

var thisClassIsUseful = function(x){
  var value = 4 * x;
  return value;
}

var passedValue = 2;

thisClassIsUseful(passedValue);


var x = "hello";
var y = 15;

if(x == 'Hello'){
  console.log('yay!');
}
else if(x == 'hello'){
  console.log('this is it!');
}
else{
  console.log('poop');
}

var userGuesses = [];

for(var x = 0; x < 500; x++){
  var magicNumber = prompt("What is the magic number?");
  userGuesses.push(magicNumber);
  if(magicNumber == 25)
    break;
  else if(userGuesses.length == 5){
    alert('You will never guess this you will never guess this!... but really you wont because the game ended');
    break;
  }
  else
    console.log("nope!");
}

