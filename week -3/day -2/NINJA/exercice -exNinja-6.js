function createCalendar(year, month) {
    const days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU'];

    const table = document.createElement('table');
    table.style.borderCollapse = 'collapse';

    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    days.forEach(day => {
        const th = document.createElement('th');
        th.textContent = day;
        th.style.border = '1px solid #000';
        th.style.padding = '4px';
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement('tbody');

    let date = new Date(year, month - 1, 1);
    let firstDay = date.getDay(); 
    firstDay = (firstDay + 6) % 7;

    let currentRow = document.createElement('tr');
    for (let i = 0; i < firstDay; i++) {
        const td = document.createElement('td');
        td.textContent = '.';
        td.style.border = '1px solid #000';
        td.style.padding = '4px';
        currentRow.appendChild(td);
    }

    while (date.getMonth() === month - 1) {
        const td = document.createElement('td');
        td.textContent = date.getDate();
        td.style.border = '1px solid #000';
        td.style.padding = '4px';
        currentRow.appendChild(td);

        if ((firstDay + date.getDate() - 1) % 7 === 6) {
            tbody.appendChild(currentRow);
            currentRow = document.createElement('tr');
        }
        date.setDate(date.getDate() + 1);
    }

    let lastDay = (firstDay + date.getDate() - 2) % 7;
    if (lastDay !== 6) {
        for (let i = lastDay + 1; i <= 6; i++) {
            const td = document.createElement('td');
            td.textContent = '.';
            td.style.border = '1px solid #000';
            td.style.padding = '4px';
            currentRow.appendChild(td);
        }
        tbody.appendChild(currentRow);
    } else if (currentRow.children.length) {
        tbody.appendChild(currentRow);
    }

    table.appendChild(tbody);

    document.body.appendChild(table);
}

createCalendar(2012, 9);