const form = document.getElementById('registrationForm');
form.addEventListener('submit', function (event) {
  event.preventDefault();
  if (validateForm()) {
    form.submit();
  }
});

function validateForm() {
  let isValid = true;

  const Orgname = document.getElementById('Orgname').value.trim();
  const InChargeName = document.getElementById('In_Charge_name').value.trim(); 
  const phoneNumber = document.getElementById('phoneNumber').value.trim();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();
  const confirmPassword = document.getElementById('confirmPassword').value.trim();

  // Validation for Orgname
  if (Orgname === '') {
    isValid = false;
    document.getElementById('OrgnameError').innerText = 'Orgnization Name is required';
    document.getElementById('Orgname').style.borderColor = 'red';
  } else if (!/^[a-zA-Z ]+$/.test(Orgname)) {
    isValid = false;
    document.getElementById('OrgnameError').innerText = 'Invalid Orgnization Name Format';
    document.getElementById('Orgname').style.borderColor = 'red';
  } else {
    document.getElementById('OrgnameError').innerText = '';
    document.getElementById('Orgname').style.borderColor = '';
  }

  // Validation for In_charge name
  if (InChargeName === '') {
    isValid = false;
    document.getElementById('In_Charge_nameError').innerText = 'In_Charge_name Name is required';
    document.getElementById('In_Charge_name').style.borderColor = 'red';
  } else if (!/^[a-zA-Z ]+$/.test(InChargeName)) {
    isValid = false;
    document.getElementById('In_Charge_nameError').innerText = 'Invalid In_Charge_name Name Format';
    document.getElementById('In_Charge_name').style.borderColor = 'red';
  } else {
    document.getElementById('In_Charge_nameError').innerText = '';
    document.getElementById('In_Charge_name').style.borderColor = '';
  }


  // Validation for Phone Number
  if (phoneNumber === '') {
    isValid = false;
    document.getElementById('phoneNumberError').innerText = 'Phone Number is required';
    document.getElementById('phoneNumber').style.borderColor = 'red';
  } else if (!/^\d{10}$/.test(phoneNumber)) {
    isValid = false;
    document.getElementById('phoneNumberError').innerText = 'Phone Number must be 10 digits';
    document.getElementById('phoneNumber').style.borderColor = 'red';
  } else {
    document.getElementById('phoneNumberError').innerText = '';
    document.getElementById('phoneNumber').style.borderColor = '';
  }

  // Validation for email
  if (email.trim() === '') {
    isValid = false;
    document.getElementById('emailError').innerText = 'Email is required';
    document.getElementById('email').style.borderColor = 'red';
  } else if (!/^\S+@\S+\.\S+$/.test(email)) {
    isValid = false;
    document.getElementById('emailError').innerText = 'Invalid email format';
    document.getElementById('email').style.borderColor = 'red';
  } else {
    document.getElementById('emailError').innerText = '';
    document.getElementById('email').style.borderColor = '';
  }

  // Validation for Password
  if (password === '') {
    isValid = false;
    document.getElementById('passwordError').innerText = 'Password is required';
    document.getElementById('password').style.borderColor = 'red';
  } else {
    document.getElementById('passwordError').innerText = '';
    document.getElementById('password').style.borderColor = '';
  }

  // Validation for Confirm Password
  if (confirmPassword === '') {
    isValid = false;
    document.getElementById('confirmPasswordError').innerText = 'Please confirm your password';
    document.getElementById('confirmPassword').style.borderColor = 'red';
  } else if (password !== confirmPassword) {
    isValid = false;
    document.getElementById('confirmPasswordError').innerText = 'Passwords do not match';
    document.getElementById('confirmPassword').style.borderColor = 'red';
  } else {
    document.getElementById('confirmPasswordError').innerText = '';
    document.getElementById('confirmPassword').style.borderColor = '';
  }

  return isValid;
}


