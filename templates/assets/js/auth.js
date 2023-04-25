const loginBtn = document.getElementById('login-btn');
const phoneNumberValue = document.getElementById('form3Example1c');
const passwordValue = document.getElementById('form3Example4c');

const getCookie = (name) => {
    return document.cookie.split(';').reduce((prev, c) => {
        let arr = c.split('=');
        return (arr[0].trim() === name) ? arr[1] : prev;
    }, undefined);
};

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
            window.location.reload(true);
        })
        .catch(error => console.log(error))
}
