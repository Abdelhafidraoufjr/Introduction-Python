const personne1 = {
    nom: "Dupont",
    prenom: "Jean",
    masse: 75, 
    hauteur: 1.8, 
    calculerIMC: function() {
        return this.masse / (this.hauteur * this.hauteur);
    }
};

const personne2 = {
    nom: "Martin",
    prenom: "Claire",
    masse: 68, 
    hauteur: 1.65, 
    calculerIMC: function() {
        return this.masse / (this.hauteur * this.hauteur);
    }
};

function comparerIMC(p1, p2) {
    const imc1 = p1.calculerIMC();
    const imc2 = p2.calculerIMC();

    if (imc1 > imc2) {
        console.log(`${p1.prenom} ${p1.nom} a l'IMC le plus élevé (${imc1.toFixed(2)})`);
    } else if (imc2 > imc1) {
        console.log(`${p2.prenom} ${p2.nom} a l'IMC le plus élevé (${imc2.toFixed(2)})`);
    } else {
        console.log(`Les deux personnes ont le même IMC (${imc1.toFixed(2)})`);
    }
}

comparerIMC(personne1, personne2);