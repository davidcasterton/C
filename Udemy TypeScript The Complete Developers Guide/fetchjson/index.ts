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
    // console.log(response.data);

    const todo = response.data as Todo;

    const id = todo.id;
    const title = todo.title;
    const completed = todo.completed;

    console.log(`
    ID: ${id}
    Title: ${title}
    Completed? ${completed}
    `);
});