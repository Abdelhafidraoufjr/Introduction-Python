let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
};
const name_user = prompt("Veuillez saisir votre nom:");
if (name_user in guestList) {
    console.log("Hi! I'm " + name_user + ", and I'm from " + guestList[name_user]);
} else {
    console.log("Hi! I'm a guest.");
}
