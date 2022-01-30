console.log("Arithamatic Operations");

var a = 10;
var b= 20;

var sum = a+b;
var diff = b-a;
var product = a*b;
var div = b/a;
var mod = b%a;
console.log("a=10, b=20");
console.log("a"+ "+" +"b"+"="+sum);
console.log("b"+ "-" +"a"+"="+diff);
console.log("a"+ "*" +"b"+"="+product);
console.log("b"+ "/" +"a"+"="+div);
console.log("b"+ "%" +"a"+"="+mod);

console.log(" ");

console.log("Condition statements");

if(a>b){
    console.log(a +"is greter than" + b);
}
else {
    console.log(b + "is greter than" + a);
}

console.log(" ");

console.log(" Functions ");


function addNum(x,y){

    var result = x+y;

    return result;

}

