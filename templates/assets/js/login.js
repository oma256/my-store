const loginBtn = document.getElementById('login-btn');
const phoneNumberValue = document.getElementById('form3Example1c');
const passwordValue = document.getElementById('form3Example4c');


loginBtn.onclick = () => {
    const requestData = {
        phoneNumber: phoneNumberValue.value,
        password: passwordValue.value,
    }

    fetch(loginUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
            body: JSON.stringify(requestData),
        })
        .then(handleErrors)
        .then(responseJSON => {
            console.log(responseJSON);
            location.href = '/'
        })
        .catch(error => console.log(error));
};
