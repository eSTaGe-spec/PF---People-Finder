window.onload = async function() {
    const contentDiv = document.querySelector('.main');

    const response = await fetch("api/all_task/");
    if (!response.ok) {
        console.error("Не удалось получить данные", response);
        return;
    }

    const taskData = await response.json();

    for(let task of taskData) {
        const taskSection = document.createElement('div');
        taskSection.className = "card";

        const isQuickly = task.is_quickly ? "<span class='urgent-marker'>СРОЧНО</span>" : "";
        
        taskSection.innerHTML = `
        <div class="header">
            <h2><a href="task/${task.id}/" class="title">${task.title}${isQuickly}</a></h2>
            <h2 class="user">${task.created_by_profile}</h2>
        </div>
        <p class="description">${task.description}</p>
               
        <div class="card-footer">
            <div class="card-price">
                <h2 class="price">Цена задания: ${task.price} руб</h2>
            </div>
            <div class="action">
                <a href="task/${task.id}/" class="look-btn">Посмотреть задание</a>
            </div>
        </div>`;

        contentDiv.appendChild(taskSection);
    }
}
