function biggestNumberInArray(arrayNumber) {
    if (!Array.isArray(arrayNumber) || arrayNumber.length === 0) {
        return 0;
    }
    let max = 0;
    for (let item of arrayNumber) {
        if (typeof item === 'number' && item > max) {
            max = item;
        }
    }
    return max;
}

const array = [-1, 0, 3, 100, 99, 2, 99]; 
const array2 = ['a', 3, 4, 2]; 
const array3 = []; 

console.log(biggestNumberInArray(array));   
console.log(biggestNumberInArray(array2));  
console.log(biggestNumberInArray(array3));  