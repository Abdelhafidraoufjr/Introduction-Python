    const div = document.getElementById('container');
    console.log(div);

    const ulLists = document.querySelectorAll('ul.list');
    ulLists[0].children[1].textContent = 'Richard';

    ulLists[1].children[1].remove();

    ulLists.forEach(ul => {
        ul.children[0].textContent = 'VotreNom';
    });

    ulLists.forEach(ul => {
        ul.classList.add('student_list');
    });

    ulLists[0].classList.add('university', 'attendance');

    div.style.backgroundColor = 'lightblue';
    div.style.padding = '15px';

    Array.from(ulLists[1].children).forEach(li => {
        if (li.textContent.trim() === 'Dan') {
            li.style.display = 'none';
        }
    });

    Array.from(ulLists[0].children).forEach(li => {
        if (li.textContent.trim() === 'Richard') {
            li.classList.add('highlight');
        }
    });

    document.body.style.fontSize = '18px';