const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

console.log("Avec .toString():", numbers.toString());

console.log("Avec .join('+'):", numbers.join("+"));
console.log("Avec .join(' '):", numbers.join(" "));
console.log("Avec .join(''):", numbers.join(""));

let sortedNumbers = [...numbers];

for (let i = 0; i < sortedNumbers.length - 1; i++) {
    for (let j = 0; j < sortedNumbers.length - 1 - i; j++) {
        if (sortedNumbers[j] < sortedNumbers[j + 1]) {
            let temp = sortedNumbers[j];
            sortedNumbers[j] = sortedNumbers[j + 1];
            sortedNumbers[j + 1] = temp;
        }
        console.log(`Après échange à i=${i}, j=${j}:`, sortedNumbers);
    }
}
console.log("Tableau trié par ordre décroissant:", sortedNumbers);