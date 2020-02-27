"use strict";
exports.__esModule = true;
var axios_1 = require("axios");
var url = 'http://jsonplaceholder.typicode.com/todos/1';
// axios.get return a promise
// chaining .then that will be called with response once we get a response from API
axios_1["default"].get(url).then(function (response) {
    // console.log(response.data);
    var todo = response.data;
    var ID = todo.ID;
    var title = todo.Title;
    var finished = todo.finished;
    console.log("\n    The Todo with ID: " + ID + "\n    HAS a title of: " + title + "\n    Is it finished? " + finished + "\n    ");
});
