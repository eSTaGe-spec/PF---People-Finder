window.onload = async function() {
    const contentDiv = document.querySelector('#content');

    const response = await fetch("/api/users_info/");
    if (!response.ok) {
        console.error("Не удалось получить информацию пользователей", response);
        return;
    }

    const usersData = await response.json();

    for(let user of usersData) {
        const profileSection = document.createElement('div');
        profileSection.className = "profile-section";

        const avatar = user.avatar || DEFAULT_AVATAR_URL;

        profileSection.innerHTML = `
        <div class="profile-info">
            <div class="avatar">
                <img src="${avatar}" alt="Аватар">
            </div>
            <a href="/profile/${user.id}" class="user-link">${user.name}</a>
            <ul class="user-details">
                <li><strong>Возраст:</strong> <span>${user.age} лет</span></li>
                <li><strong>Стаж работы:</strong> <span>${user.work_experience} лет</span></li>
                <li><strong>Навыки:</strong> <span>${user.skills.join(', ')}</span></li>
            </ul>        
        </div>`;

        contentDiv.appendChild(profileSection);
    }
}
