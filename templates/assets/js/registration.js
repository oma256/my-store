const registerBtn = document.getElementById('register-btn');
const phoneNumberInput = document.getElementById('phone_number_id');
const firstNameInput = document.getElementById('first_name_id');
const lastNameInput = document.getElementById('last_name_id');
const passwordInput = document.getElementById('pass_id');
const repeatPasswordInput = document.getElementById('repeat_pass_id');

registerBtn.onclick = () => {
    const requestData = {
        phoneNumber: phoneNumberInput.value,
        firstName: firstNameInput.value,
        lastName: lastNameInput.value,
        password: passwordInput.value,
        repeatPassword: repeatPasswordInput.value
    }

    fetch(registerUrl, {
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
}