function displayNumbersDivisible(divisor = 23) {
    let sum = 0;
    let numbers = [];
    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            console.log(i);
            numbers.push(i);
            sum += i;
        }
    }
    console.log('Sum :', sum);
}

displayNumbersDivisible();
displayNumbersDivisible(3);
displayNumbersDivisible(45);