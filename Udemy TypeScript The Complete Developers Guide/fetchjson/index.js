"use strict";
exports.__esModule = true;
var axios_1 = require("axios");
var url = 'http://jsonplaceholder.typicode.com/todos/1';
// axios.get return a promise
// chaining .then that will be called with response once we get a response from API
axios_1["default"].get(url).then(function (response) {
    var todo = response.data;
    logTodo(todo);
});
var logTodo = function (todo) {
    console.log("\n        ID: " + todo.id + "\n        Title: " + todo.title + "\n        Completed? " + todo.completed + "\n        ");
};
