function estPalindrome(chaine) {
    const str = chaine.replace(/\s+/g, '').toLowerCase();
    return str === str.split('').reverse().join('');
}

console.log(estPalindrome("madame")); 
console.log(estPalindrome("bob"));    
console.log(estPalindrome("kayak"));  
console.log(estPalindrome("bonjour"));