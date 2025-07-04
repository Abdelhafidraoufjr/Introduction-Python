const famille = {
    pere: "Jean",
    mere: "Marie",
    fils: "Paul",
    fille: "Sophie"
};

for (const key in famille) {
    console.log(key, ":" + " " + famille[key]);
}
