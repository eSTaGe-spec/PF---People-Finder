function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


window.onload = async function() {
    const userId = document.cookie.userId;
    console.log(userId)
    await loadUserData();
    await loadSkills();
    document.getElementById('settings-form').addEventListener('submit', function(event) {
        event.preventDefault();
        changeProfile(event);
    });
}

async function loadUserData() {
    const response = await fetch("/api/user_settings/");
    if (!response.ok) {
        console.error("Не удалось получить данные профиля", response);
        return;
    }

    const profileData = await response.json();

    document.querySelector('#avatar-img').src = profileData.avatar;
    document.querySelector('#age').value = profileData.age;
    document.querySelector('#experience').value = profileData.work_experience;
    document.querySelector('#phone-number').value = profileData.phone_number;
    document.querySelector('#Email').value = profileData.email;
}

async function loadSkills() {
    const response = await fetch("/api/skills/");
    if (!response.ok) {
        console.error("Не удалось загрузить данные о навыках", response);
        return;
    }

    const skillsList = await response.json();
    const skillsSelect = document.querySelector('#skills');

    for(let skill of skillsList) {
       let option = document.createElement('option');
       option.text = skill.title;
       skillsSelect.add(option);
    }
}

async function changeProfile(event) {
    const form = event.target;

    const formData = new FormData();

    if (form['avatar'].files.length > 0) {
        formData.append('avatar', form['avatar'].files[0]);
    }
    
    formData.append('age', form['age'].value);
    formData.append('work_experience', form['experience'].value);
    formData.append('phone_number', form['phone-number'].value);
    formData.append('email', form['Email'].value);
    
    const selectedSkills = Array.from(form['skills'].selectedOptions).map(option => option.value);
    selectedSkills.forEach(skill => formData.append('skills', skill));


    try {
        const response = await fetch('/api/user_settings/', {
            method: 'POST',
            body: formData,
            headers: {
               'X-CSRFToken': getCookie('csrftoken'),
            },
        });

        if (!response.ok) {
            console.error('Не удалось обновить профиль', response);
            return;
        }

        const data = await response.json();
        console.log('Профиль обновлен', data);
        window.location.href = `/`;
        
    } catch (error) {
        console.error('Произошла ошибка при отправке формы', error);
    }
}
