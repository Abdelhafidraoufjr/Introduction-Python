const colors = ["rouge", "bleu", "vert", "jaune", "noir"];
const numbersSTR = ["premier", "deuxième", "troisième", "quatrième", "cinquième"];

console.log("--------------Mon choix n°-------------------\n")
for (let i = 0; i < colors.length; i++) {
    console.log("Mon choix n°" + (i + 1) + " est " + colors[i]);

}

console.log("--------------Mon numbersSTR-------------------\n")
for (let i = 0; i < colors.length; i++) {
    console.log("Mon " + numbersSTR[i] + " choix est " + colors[i]);
}

