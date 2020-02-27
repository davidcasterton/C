import axios from 'axios';

const url = 'http://jsonplaceholder.typicode.com/todos/1';

interface Todo {
    id: number;
    title: string;
    completed: boolean;
}

// axios.get return a promise
// chaining .then that will be called with response once we get a response from API
axios.get(url).then(response => {
    const todo = response.data as Todo;
    logTodo(todo);
});

const logTodo = (todo : Todo) => {
    console.log(`
        ID: ${todo.id}
        Title: ${todo.title}
        Completed? ${todo.completed}
        `);
}