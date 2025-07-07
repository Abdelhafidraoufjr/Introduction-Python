function calculateTip() {
    var billAmount = document.getElementById("billamt").value;
    var serviceQuality = document.getElementById("serviceQual").value;
    var numberOfPeople = document.getElementById("peopleamt").value;

    if (billAmount === "" || serviceQuality == 0) {
        alert("Please enter bill amount and select service quality.");
        return;
    }

    if (numberOfPeople === "" || numberOfPeople < 1) {
        numberOfPeople = 1;
        document.getElementById("each").style.display = "none";
    } else {
        document.getElementById("each").style.display = "inline";
    }

    var total = (billAmount * serviceQuality) / numberOfPeople;
    total = total.toFixed(2);

    document.getElementById("totalTip").style.display = "block";
    document.getElementById("tip").innerText = total;
}

document.getElementById("totalTip").style.display = "none";
document.getElementById("each").style.display = "none";

document.getElementById("calculate").addEventListener("click", calculateTip);
document.getElementById("totalTip").style.display = "none";
document.getElementById("calculate").onclick = calculateTip;
