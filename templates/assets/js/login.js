const loginBtn = document.getElementById('login-btn');
const phoneNumberValue = document.getElementById('form3Example1c');
const passwordValue = document.getElementById('form3Example4c');
const passErrMsg = document.getElementById('pass-err-msg-id');
const userNotFoundErrMsg = document.getElementById('user-not-found-msg-id');


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
            if (responseJSON['detail']['password']) {
                passErrMsg.style.display = 'block';
                userNotFoundErrMsg.style.display = 'none';
            } else if (responseJSON['detail']['user']) {
                userNotFoundErrMsg.style.display = 'block';
                passErrMsg.style.display = 'none';
            } else {
                location.href = '/';
            }
        })
        .catch(error => console.log(error));
};
