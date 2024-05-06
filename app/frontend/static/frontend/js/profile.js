window.onload = function() {
    fetch('/api/profile/')
    .then(response => response.json())
    .then(data => {
  
      // Подстановка данных профиля
      document.querySelector('.avatar img').src = data.avatar;
      document.querySelector('.user-name').innerText = data.name;
      document.querySelector('.user-details li:nth-child(1) span').innerText = data.age + " лет";
      document.querySelector('.user-details li:nth-child(2) span').innerText = data.work_experience + " лет";
      document.querySelector('.user-details li:nth-child(3) span').innerText = data.phone_number;
      document.querySelector('.user-details li:nth-child(4) span').innerText = data.email;
      document.querySelector('.user-details li:nth-child(5) span').innerText = data.skills.join(", ");
      
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  };
  