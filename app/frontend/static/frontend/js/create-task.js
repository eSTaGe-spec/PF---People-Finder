function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfToken = getCookie('csrftoken');


window.onload = async function () {
    const response = await fetch('/api/create_task/');
    const data = await response.json();

    const selectElement = document.getElementById('order-tags')

    data.forEach(function(tag) {
        const optionElement = document.createElement('option');
        optionElement.innerHTML = tag.title;
        selectElement.appendChild(optionElement);
    });

    document.getElementById('create-order-form').addEventListener('submit', async function(e) {
        e.preventDefault();
    
        const title = document.getElementById('order-title').value;
        const description = document.getElementById('order-description').value;
        const price = document.getElementById('order-price').value;
        const quickly = document.getElementById('urgent-order').checked;
        const selectedTags = Array.from(document.getElementById('order-tags').options)
                                    .filter(option => option.selected)
                                    .map(option => option.value);
    
        const data = {
            title: title,
            description: description,
            price: price,
            is_quickly: quickly,
            tags: selectedTags
        };
    
        const response = await fetch('/api/create_task/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        });
        
    
        if (response.ok) {
            // Действие после удачного создания заказа. Редирект или сообщение об успехе.
            window.location.href = '/';
        } else {
            // Действие при ошибке создания заказа. Вывод ошибки.
            alert('Произошла ошибка при создании заказа');
        }
    })
    

}
