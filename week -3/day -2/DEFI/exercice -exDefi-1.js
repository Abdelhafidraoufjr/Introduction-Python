const planets = [
    {
        name: "Mercure",
        colorClass: "mercury",
        moons: []
    },
    {
        name: "Vénus",
        colorClass: "venus",
        moons: []
    },
    {
        name: "Terre",
        colorClass: "earth",
        moons: ["Lune"]
    },
    {
        name: "Mars",
        colorClass: "mars",
        moons: ["Phobos", "Deimos"]
    },
    {
        name: "Jupiter",
        colorClass: "jupiter",
        moons: ["Io", "Europe", "Ganymède", "Callisto"]
    },
    {
        name: "Saturne",
        colorClass: "saturn",
        moons: ["Titan", "Encelade", "Mimas", "Téthys"]
    },
    {
        name: "Uranus",
        colorClass: "uranus",
        moons: ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]
    },
    {
        name: "Neptune",
        colorClass: "neptune",
        moons: ["Triton", "Néréide"]
    }
];

const style = document.createElement('style');
style.textContent = `
    .mercury { background: gray; }
    .venus { background: #e1c699; }
    .earth { background: #2a5cdd; }
    .mars { background: #c1440e; }
    .jupiter { background: #e3c07b; }
    .saturn { background: #e7d3a1; }
    .uranus { background: #b5e3e3; }
    .neptune { background: #4062bb; }
`;
document.head.appendChild(style);

const section = document.querySelector('.listPlanets');

planets.forEach((planet, idx) => {
    const planetDiv = document.createElement('div');
    planetDiv.classList.add('planet', planet.colorClass);
    planetDiv.textContent = planet.name;

    planet.moons.forEach((moon, moonIdx) => {
        const moonDiv = document.createElement('div');
        moonDiv.classList.add('moon');
        const angle = (moonIdx / planet.moons.length) * 2 * Math.PI;
        const radius = 60;
        moonDiv.style.left = 50 + radius * Math.cos(angle) + 'px';
        moonDiv.style.top = 50 + radius * Math.sin(angle) + 'px';
        moonDiv.title = moon;
        planetDiv.appendChild(moonDiv);
    });

    section.appendChild(planetDiv);
});