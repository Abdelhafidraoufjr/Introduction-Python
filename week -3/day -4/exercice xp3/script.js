        let memory = 0;
        let lastOperation = '';
        let startNew = false;

        function appendToDisplay(value) {
            const display = document.getElementById('display');
            if (value === '±') {
                if (display.value !== '' && display.value !== '0') {
                    display.value = parseFloat(display.value) * -1;
                }
                return;
            }
            if (startNew) {
                if ('+-*/'.includes(value)) {
                    display.value += value;
                } else {
                    display.value = value;
                }
                startNew = false;
            } else {
                display.value += value;
            }
            lastOperation = '';
        }

        function clearEntry() {
            document.getElementById('display').value = '';
            lastOperation = '';
            startNew = false;
        }

        function allClear() {
            clearEntry();
            memory = 0;
        }

        function calculate() {
            try {
                const display = document.getElementById('display');
                const result = eval(display.value);
                display.value = result;
                lastOperation = '=';
                startNew = true;
            } catch (error) {
                document.getElementById('display').value = 'Error';
                startNew = true;
            }
        }

        function memoryAdd() {
            calculate();
            memory += parseFloat(document.getElementById('display').value) || 0;
            startNew = true;
        }

        function memorySubtract() {
            calculate();
            memory -= parseFloat(document.getElementById('display').value) || 0;
            startNew = true;
        }

        function memoryRecall() {
            const display = document.getElementById('display');
            if (display.value === '' || '+-*/'.includes(display.value[display.value.length - 1])) {
                display.value += memory;
            } else {
                display.value = memory;
            }
            startNew = false;
        }

        function memoryClear() {
            memory = 0;
        }