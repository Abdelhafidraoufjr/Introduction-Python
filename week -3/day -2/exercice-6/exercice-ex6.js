const navBar = document.getElementById('navBar');
navBar.setAttribute('id', 'socialNetworkNavigation');

const ul = navBar.querySelector('ul');
const newLi = document.createElement('li');
const textNode = document.createTextNode('Déconnexion');
newLi.appendChild(textNode);
ul.appendChild(newLi);

const firstLi = ul.firstElementChild;
const lastLi = ul.lastElementChild;
console.log('Premier lien :', firstLi.textContent);
console.log('Dernier lien :', lastLi.textContent);