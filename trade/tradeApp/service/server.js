<<<<<<< HEAD
var spawn = require('child_process').spawn;
var app   = spawn('python', ['main.py']);
app.stdout.on('data', function(data) {{
  console.log('stdout: ' + data);
}});

app.stderr.on('data', function(data) {{
  console.log('stderr: ' + data);
}});

app.on('exit', function(code) {{
  console.log('exit code: ' + code);
}});
=======
var exec = require('child_process').exec;
var child;

child = exec("python trade.py", function (error, stdout, stderr) {
  console.log('stdout: ' + stdout);
  console.log('stderr: ' + stderr);
  if (error !== null) {
    console.log('exec error: ' + error);
  }
});
>>>>>>> 7061189acfda28063f26b59475b7ac6a08fc951d
