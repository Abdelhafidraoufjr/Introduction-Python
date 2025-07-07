const tasks = [];
let taskIdCounter = 0;

const form = document.querySelector('form');
const input = document.querySelector('input[type="text"]');
const listTasksDiv = document.querySelector('.listTasks');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    addTask();
});

function addTask() {
    const taskText = input.value.trim();
    if (taskText === '') return;

    const task = {
        task_id: taskIdCounter++,
        text: taskText,
        done: false
    };
    tasks.push(task);

    const taskDiv = document.createElement('div');
    taskDiv.className = 'task-item';
    taskDiv.setAttribute('data-task-id', task.task_id);

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', doneTask);

    const label = document.createElement('label');
    label.textContent = task.text;
    label.style.margin = '0 10px';

    const deleteBtn = document.createElement('button');
    deleteBtn.innerHTML = '<i class="fa fa-times"></i>';
    deleteBtn.className = 'delete-btn';
    deleteBtn.addEventListener('click', deleteTask);

    taskDiv.appendChild(checkbox);
    taskDiv.appendChild(label);
    taskDiv.appendChild(deleteBtn);

    listTasksDiv.appendChild(taskDiv);

    input.value = '';
}

function doneTask(e) {
    const taskDiv = e.target.closest('.task-item');
    const taskId = Number(taskDiv.getAttribute('data-task-id'));
    const task = tasks.find(t => t.task_id === taskId);
    if (!task) return;
    task.done = e.target.checked;

    const label = taskDiv.querySelector('label');
    if (task.done) {
        label.style.textDecoration = 'line-through';
        label.style.color = 'red';
    } else {
        label.style.textDecoration = 'none';
        label.style.color = 'black';
    }
}

function deleteTask(e) {
    const taskDiv = e.target.closest('.task-item');
    const taskId = Number(taskDiv.getAttribute('data-task-id'));
    const idx = tasks.findIndex(t => t.task_id === taskId);
    if (idx > -1) tasks.splice(idx, 1);
    taskDiv.remove();
}