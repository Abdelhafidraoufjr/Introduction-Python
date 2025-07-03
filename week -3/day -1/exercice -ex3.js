const input = prompt("Veuillez saisir un nombre :");

let number = Number(input);

while (number < 10) {
    console.log("Vous avez saisi :", number);
    number = Number(prompt("Veuillez saisir un nombre :"));
}