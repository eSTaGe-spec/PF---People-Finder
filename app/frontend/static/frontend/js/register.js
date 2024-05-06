document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();
    var errorMessage = document.getElementById('error-message');
    errorMessage.textContent = ""; 

    const name = document.querySelector('#name').value;
    const username = document.querySelector('#login').value;
    const password1 = document.querySelector('#password1').value;
    const password2 = document.querySelector('#password2').value;

    if (!name) {
        errorMessage.textContent = "Поле 'Имя' не может быть пустым";
        return;
    }

    if (!username) {
        errorMessage.textContent = "Поле 'Логин' не может быть пустым";
        return;
    }

    if (!password1) {
        errorMessage.textContent = "Поле 'Пароль' не может быть пустым";
        return;
    }

    if (!password2) {
        errorMessage.textContent = "Поле 'Повтор пароля' не может быть пустым";
        return;
    }

    if (password1 !== password2) {
        errorMessage.textContent = "Пароли не совпадают";
        return;
    }

    const response = await postData('/api/register/', {name, username, password: password1})

    if (response.status === 201) {
        window.location.href = "/"
    } else {
        const data = await response.json();
        
        if (data.error) {
            errorMessage.textContent = data.error;
        } else {
            errorMessage.textContent = "Ошибка при регистрации";
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
