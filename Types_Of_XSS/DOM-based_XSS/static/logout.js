document.getElementById('LogOutButton').addEventListener('click', function(){
    function logout() {
        window.localStorage.removeItem('token');
        window.location.href= './redirect?url=./../index.php';
    }
    logout();
});
if (!window.localStorage.getItem('token')) {
    window.location.href= './signin.html';
}