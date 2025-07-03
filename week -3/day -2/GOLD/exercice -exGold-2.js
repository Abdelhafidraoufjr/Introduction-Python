function abbrevName(name) {
    let parts = name.trim().split(' ');
    if (parts.length < 2) return name;
    return `${parts[0]} ${parts[1][0]}.`;
}

console.log(abbrevName("Robin Singh")); 