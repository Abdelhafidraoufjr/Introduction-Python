const people = ["Greg", "Mary", "Devon", "James"];

people.shift()
console.log(people)

const index = people.indexOf("James")
if (index !== -1){
    people[index] = "jason"
}
console.log(people)

people.push("abdelhafid")
let index_mary = people.indexOf("abdelhafid")
console.log(people)
console.log(index_mary)


let copie = people.slice(1, 4)
console.log("people = ",copie)

let index_foo = people.indexOf("Foo")
console.log(index_foo)
console.log("il affiche -1 car on a pas Foo dans notre Array")

let last = people[people.length - 1]
console.log(last)

console.log(people)

for (let i = 0; i<people.length; i++){
    console.log(people[i]);
}

for (let i = 0; i<people.length; i++){
    console.log(people[i]);
    if(people[i]=="Devon"){
        break;
    }
}