#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);

    // Filter completed tasks
    const completedTasks = tasks.filter(task => task.completed);

    // Compute the number of completed tasks per user
    const completedTasksPerUser = completedTasks.reduce((result, task) => {
      result[task.userId] = (result[task.userId] || 0) + 1;
      return result;
    }, {});

    console.log(completedTasksPerUser);
  }
});
