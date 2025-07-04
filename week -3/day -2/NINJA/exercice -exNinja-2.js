function calculateAverage(gradesList) {
    if (!Array.isArray(gradesList) || gradesList.length === 0) {
        console.log("Veuillez fournir un tableau de notes non vide.");
        return null;
    }
    const sum = gradesList.reduce((acc, grade) => acc + grade, 0);
    return sum / gradesList.length;
}

function findAvg(gradesList) {
    const average = calculateAverage(gradesList);
    if (average === null) return;
    console.log("La moyenne est :", average);

    if (average > 65) {
        console.log("Félicitations, vous avez réussi !");
    } else {
        console.log("Vous avez échoué. Vous devez recommencer le cours.");
    }
}
findAvg([70, 80, 60, 90]);