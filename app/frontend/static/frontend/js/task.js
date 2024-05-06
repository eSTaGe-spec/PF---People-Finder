window.onload = async function() {
    const taskId = window.location.pathname.split('/').filter(Boolean).pop();
    const contentDiv = document.querySelector('.main .card');

    const response = await fetch(`/api/task/${taskId}/`);
    if (!response.ok) {
        console.error("Не удалось получить данные", response);
        return;
    }

    const task = await response.json();

    const isQuickly = task.is_quickly ? "<span class='urgent-marker'>СРОЧНО</span>" : "";

    document.querySelector('.titleh1').textContent = `Заказ: ${task.title}`;
    contentDiv.querySelector('.header .title').textContent = task.title;

    const userTakenTask = task.assigned_by_profile ? `Взял задание: ${task.assigned_by_profile}` : "Задание свободно";
    contentDiv.querySelector('.header .user-taken-task').textContent = userTakenTask;

    contentDiv.querySelector('.header .user').textContent = `Опубликовано: ${task.created_by_profile}`;
    contentDiv.querySelector('.description').textContent = task.description;

    const tagsContainer = contentDiv.querySelector('.tag-container');
    tagsContainer.innerHTML = '';
    for(let tag of task.tags) {
        let tagLink = document.createElement('a');
        tagLink.className = 'tag-link';
        tagLink.textContent = tag;
        tagsContainer.appendChild(tagLink);
    }

    contentDiv.querySelector('.card-price .price').textContent = `Цена задания: ${task.price} руб`;

    document.querySelector('#take-task').addEventListener('submit', async function(e) {
        e.preventDefault();
    
        const response = await fetch(`/api/accept_task/${taskId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id: document.cookie.userId })

        });
    
        const responseData = await response.json();
    
        if (!responseData.error) {
            alert('Задание успешно взято!')
        } else {
            alert('Произошла ошибка. Пожалуйста, попробуйте еще раз.')
        }
    
        // Обновляем страницу, чтобы отобразить обновленный статус задачи
        window.location.reload();
    });
    
}
