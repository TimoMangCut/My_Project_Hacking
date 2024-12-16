document.getElementById('loginform').addEventListener('submit', function(event){
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (username === '' || password === '') {
        alert('both fields username and password are required !');
        return;
    }
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "./control/control.php",true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    const data = JSON.stringify({
        "username": username,
        "password": password
    });
    xhr.onload = function(){
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            console.log(xhr.responseText);
            if (response.status === 'success') {
                alert('Login Successful');
                window.localStorage.setItem('token', response.token);
                window.location.href = './welcome.html';
            }
            else {
                alert ('Login Faild:' + response.message);
            }
        }
    }
    xhr.send(data);
})