let correctColor;
let difficulty = 'easy';
let countdownInterval;

function generateRandomColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}

function setDifficulty(level) {
    difficulty = level;
    clearInterval(countdownInterval);
    startGame();
}

function startGame() {
    correctColor = generateRandomColor();
    const colorDisplay = document.getElementById('color-display');
    const options = document.getElementById('options');
    const result = document.getElementById('result');
    const nextColorText = document.getElementById('next-color');
    const rgbInput = document.getElementById('rgb-input');

    colorDisplay.style.backgroundColor = correctColor;
    options.innerHTML = '';
    result.textContent = '';
    nextColorText.style.display = 'none';

    if (difficulty === 'hard') {
        options.style.display = 'none';
        rgbInput.style.display = 'block';
    } else {
        options.style.display = 'block';
        rgbInput.style.display = 'none';
        const numOptions = difficulty === 'easy' ? 3 : 6;
        const colors = [correctColor];
        for (let i = 1; i < numOptions; i++) {
            colors.push(generateRandomColor());
        }
        colors.sort(() => Math.random() - 0.5);

        colors.forEach(color => {
            const button = document.createElement('button');
            button.className = 'color-option';
            if (difficulty === 'easy') {
                button.style.backgroundColor = color;
            } else {
                button.textContent = color;
            }
            button.onclick = () => checkGuess(color);
            options.appendChild(button);
        });
    }
}

function checkGuess(guessedColor) {
    const result = document.getElementById('result');
    const options = document.getElementById('options');
    const nextColorText = document.getElementById('next-color');
    if (guessedColor === correctColor) {
        result.textContent = 'Correct! Well done!';
        options.innerHTML = '';
        nextColorText.style.display = 'block';
        startCountdown();
    } else {
        result.textContent = 'Wrong! Try again.';
    }
}

function startCountdown() {
    clearInterval(countdownInterval);
    let countdown = 5;
    document.getElementById('countdown').textContent = countdown;
    countdownInterval = setInterval(() => {
        countdown--;
        document.getElementById('countdown').textContent = countdown;
        if (countdown === 0) {
            clearInterval(countdownInterval);
            startGame();
        }
    }, 1000);
}

function checkRgbGuess() {
    const r = document.getElementById('r').value;
    const g = document.getElementById('g').value;
    const b = document.getElementById('b').value;
    const guessedColor = `rgb(${r}, ${g}, ${b})`;
    checkGuess(guessedColor);
}

startGame();