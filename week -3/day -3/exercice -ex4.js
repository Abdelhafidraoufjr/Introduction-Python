const readlineSync = require('readline-sync');

function hotelCost(nights) {
    const pricePerNight = 140;
    if (typeof nights !== 'number' || isNaN(nights) || nights <= 0) {
        throw new Error("Invalid number of nights");
    }
    return nights * pricePerNight;
}

function planeRideCost(destination) {
    if (typeof destination !== 'string' || !destination.trim()) {
        throw new Error("Invalid destination");
    }
    const dest = destination.trim().toLowerCase();
    if (dest === 'londres') return 183;
    if (dest === 'paris') return 220;
    return 300;
}

function rentalCarCost(days) {
    const pricePerDay = 40;
    if (typeof days !== 'number' || isNaN(days) || days <= 0) {
        throw new Error("Invalid number of days");
    }
    let total = days * pricePerDay;
    if (days > 10) {
        total *= 0.95;
    }
    return total;
}

function totalVacationCost() {

    let nights;
    while (true) {
        const input = readlineSync.question("Combien de nuits souhaitez-vous passer à l'hôtel ? ");
        nights = Number(input);
        if (!isNaN(nights) && nights > 0) break;
        console.log("Veuillez entrer un nombre valide de nuits.");
    }

    let destination;
    while (true) {
        destination = readlineSync.question("Quelle est votre destination ? ");
        if (typeof destination === 'string' && destination.trim()) break;
        console.log("Veuillez entrer une destination valide.");
    }

    let days;
    while (true) {
        const input = readlineSync.question("Combien de jours souhaitez-vous louer la voiture ? ");
        days = Number(input);
        if (!isNaN(days) && days > 0) break;
        console.log("Veuillez entrer un nombre valide de jours.");
    }

    const hotel = hotelCost(nights);
    const plane = planeRideCost(destination);
    const car = rentalCarCost(days);

    console.log(`Le prix de l'hôtel : ${hotel}$, le prix de la voiture : ${car}$, le prix des billets d'avion : ${plane}$.`);
    console.log(`Le coût total des vacances est : ${hotel + plane + car}$`);
    return hotel + plane + car;
}

totalVacationCost();