let sentence = "Le film n'est pas si mauvais, je l'aime bien";

let wordNot = sentence.indexOf("pas");
let wordBad = sentence.indexOf("mauvais");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    let before = sentence.slice(0, wordNot);
    let after = sentence.slice(wordBad + "mauvais".length);
    let result = before + "bon" + after;
    console.log(result.trim());
} else {
    console.log(sentence);
}