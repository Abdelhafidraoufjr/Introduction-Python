let age = [20, 5, 12, 43, 98, 55];

let somme = age.reduce((acc, val) => acc + val, 0);
console.log(somme);

let maxAge = Math.max(...age);
console.log(maxAge);