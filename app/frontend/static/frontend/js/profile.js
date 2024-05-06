window.onload = function() {
  let pathArray = window.location.pathname.split('/');
  let userId = pathArray[pathArray.length - 2];
  console.log(pathArray)
  fetch(`/api/profile/${userId}/`)
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


  fetch(`/api/task_profile/${userId}/`)
  .then(response => response.json())
  .then(data => {
    
      const createOrderCard = (title, id) => {
          const order = document.createElement('div');
          order.className = 'order';

          const orderTitle = document.createElement('h3');
          orderTitle.className = 'order-title';
          orderTitle.textContent = title;
          order.appendChild(orderTitle);

          const orderAction = document.createElement('div');
          orderAction.className = 'action';
          const actionLink = document.createElement('a');
          actionLink.className = 'look-btn';
          actionLink.href = `/task/${id}`;
          actionLink.textContent = 'Посмотреть заказ';
          orderAction.appendChild(actionLink);
          order.appendChild(orderAction);

          return order;
      }
       
      const appendOrders = (orders, sectionTitle) => {
          const ordersHeading = document.createElement('h2');
          ordersHeading.className = 'orders-heading';
          ordersHeading.textContent = sectionTitle;
          ordersSection.appendChild(ordersHeading);

          for (let { title, id } of orders) {
              ordersSection.appendChild(createOrderCard(title, id));
          }
      }

      const ordersSection = document.querySelector('.orders-section');
      ordersSection.innerHTML = '';

      const { assigned_tasks, created_tasks } = data;

      appendOrders(assigned_tasks, 'Взятые заказы');
      appendOrders(created_tasks, 'Созданные заказы');
  })
  .catch((error) => {
      console.error('Error:', error);
  });



};
