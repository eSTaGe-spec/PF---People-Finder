
document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();
    var errorMessage = document.getElementById('error-message');
    errorMessage.textContent = ""; 

    const username = document.querySelector('#login').value
    const password = document.querySelector('#password').value

    if (!username) {
        errorMessage.textContent = "Поле 'Логин' не может быть пустым";
        return;
    }
    if (!password) {
        errorMessage.textContent = "Поле 'Пароль' не может быть пустым";
        return;
    }

    const response = await postData('/api/login/', {username, password})

    if (response.status === 200) {
        window.location.href = "/"
    } else {
        const data = await response.json();
        
        if (data.error) {
            errorMessage.textContent = data.error;
        } else {
            errorMessage.textContent = "Ошибка при авторизации";
        }
    }
})

async function postData(url, data) {
    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(data)
    });
    return response;
}
