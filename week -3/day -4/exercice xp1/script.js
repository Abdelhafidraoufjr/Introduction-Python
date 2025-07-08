const input = document.getElementById('new-todo');
const todoList = document.getElementById('todo-list');
const removeAllBtn = document.getElementById('remove-all');
let currentFilter = 'all';

input.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    addTodo();
  }
});

function addTodo() {
  const todoText = input.value.trim();
  if (todoText) {
    const li = document.createElement('li');
    li.innerHTML = `
                    <span class="todo-text">${todoText}</span>
                    <button class="remove-todo" onclick="removeTodo(this)">Remove</button>
                `;
    li.addEventListener('click', function (e) {
      if (e.target !== this && e.target.tagName !== 'SPAN') return;
      toggleComplete(this);
    });
    todoList.appendChild(li);
    input.value = '';
    updateRemoveAllButton();
    applyFilter();
  }
}

function toggleComplete(element) {
  element.classList.toggle('completed');
  applyFilter();
}

function removeTodo(button) {
  button.parentElement.remove();
  updateRemoveAllButton();
  applyFilter();
}

function removeAllTodos() {
  if (confirm('Are you sure you want to remove all todos?')) {
    todoList.innerHTML = '';
    updateRemoveAllButton();
    applyFilter();
  }
}

function updateRemoveAllButton() {
  removeAllBtn.disabled = todoList.children.length === 0;
}

function setFilter(filter) {
  currentFilter = filter;
  document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelector(`.filter-btn[onclick="setFilter('${filter}')"]`).classList.add('active');
  applyFilter();
}

function applyFilter() {
  const todos = todoList.children;
  for (let todo of todos) {
    switch (currentFilter) {
      case 'all':
        todo.style.display = '';
        break;
      case 'active':
        todo.style.display = todo.classList.contains('completed') ? 'none' : '';
        break;
      case 'completed':
        todo.style.display = todo.classList.contains('completed') ? '' : 'none';
        break;
    }
  }
}

updateRemoveAllButton();