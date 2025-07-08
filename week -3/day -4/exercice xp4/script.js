        const gameBoard = document.getElementById('game-board');
        const scoreDisplay = document.getElementById('score');
        const timeDisplay = document.getElementById('time');
        const highScoreList = document.getElementById('high-score-list');
        let score = 0;
        let timeLeft = 30;
        let moleInterval;
        let countdownInterval;
        let highScores = [
            { name: "Alice", score: 10 },
            { name: "Bob", score: 8 },
            { name: "Charlie", score: 5 }
        ];

        function createHoles() {
            gameBoard.innerHTML = ''; // Clear existing holes
            for (let i = 0; i < 9; i++) {
                const hole = document.createElement('div');
                hole.classList.add('hole');
                hole.dataset.index = i;
                hole.addEventListener('click', whackMole);
                gameBoard.appendChild(hole);
            }
        }

        function showMole() {
            const holes = document.querySelectorAll('.hole');
            holes.forEach(hole => hole.innerHTML = ''); // Clear all holes
            const randomHole = holes[Math.floor(Math.random() * holes.length)];
            randomHole.innerHTML = '<span class="mole">🐹</span>';
        }

        function whackMole(event) {
            if (event.target.classList.contains('mole')) {
                score++;
                scoreDisplay.textContent = score;
                event.target.parentElement.innerHTML = '';
            }
        }

        function startGame() {
            score = 0;
            timeLeft = 30;
            scoreDisplay.textContent = score;
            timeDisplay.textContent = timeLeft;
            createHoles();
            clearInterval(moleInterval);
            clearInterval(countdownInterval);
            moleInterval = setInterval(showMole, 1000);
            countdownInterval = setInterval(countdown, 1000);
        }

        function countdown() {
            timeLeft--;
            timeDisplay.textContent = timeLeft;
            if (timeLeft === 0) {
                endGame();
            }
        }

        function endGame() {
            clearInterval(moleInterval);
            clearInterval(countdownInterval);
            gameBoard.innerHTML = '';
            updateHighScores();
            displayHighScores();
            const playAgain = confirm(`Game over! Your score is ${score}. Play again?`);
            if (playAgain) {
                startGame();
            }
        }

        function updateHighScores() {
            if (score > highScores[highScores.length - 1].score) {
                const playerName = prompt("You got a high score! Enter your name:");
                if (playerName) {
                    highScores.push({ name: playerName, score: score });
                    highScores.sort((a, b) => b.score - a.score);
                    highScores = highScores.slice(0, 5); // Keep only top 5 scores
                }
            }
        }

        function displayHighScores() {
            highScoreList.innerHTML = '';
            highScores.forEach(entry => {
                const li = document.createElement('li');
                li.textContent = `${entry.name}: ${entry.score}`;
                highScoreList.appendChild(li);
            });
        }

        displayHighScores();
        startGame();