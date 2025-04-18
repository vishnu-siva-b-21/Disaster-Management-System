const form = document.getElementById('registrationForm');
form.addEventListener('submit', function (event) {
  event.preventDefault();
  if (validateForm()) {
    form.submit();
    
  }
});

function validateForm() {
  let isValid = true;

  const name = document.getElementById('name').value.trim();
  const age = document.getElementById('age').value.trim();
  const phoneNumber = document.getElementById('phoneNumber').value.trim();
  const area = document.getElementById('area').value.trim();
  const selectedSkill = document.getElementById('dropdown').value; // Add this line for selected skill
  const pinCode = document.getElementById('pinCode').value.trim();
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;


  // Validation for Name
  if (name === '') {
    isValid = false;
    document.getElementById('nameError').innerText = 'Name is required';
    document.getElementById('name').style.borderColor = 'red';
  } else if (!/^[a-zA-Z ]+$/.test(name)) {
    isValid = false;
    document.getElementById('nameError').innerText = 'Invalid Name Format';
    document.getElementById('name').style.borderColor = 'red';
  } else {
    document.getElementById('nameError').innerText = '';
    document.getElementById('name').style.borderColor = '';
  }

  // Validation for Age
  if (age === '') {
    isValid = false;
    document.getElementById('ageError').innerText = 'Age is required';
    document.getElementById('age').style.borderColor = 'red';
  } else if (isNaN(age) || age < 1 || age > 100) {
    isValid = false;
    document.getElementById('ageError').innerText = 'Invalid age';
    document.getElementById('age').style.borderColor = 'red';
  } else {
    document.getElementById('ageError').innerText = '';
    document.getElementById('age').style.borderColor = '';
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

  // Validation for Area
  if (area === '') {
    isValid = false;
    document.getElementById('areaError').innerText = 'Area is required';
    document.getElementById('area').style.borderColor = 'red';
  } else if (!/^[a-zA-Z ]+$/.test(area)) {
    isValid = false;
    document.getElementById('areaError').innerText = 'Invalid Area Name';
    document.getElementById('area').style.borderColor = 'red';
  } else {
    document.getElementById('areaError').innerText = '';
    document.getElementById('area').style.borderColor = '';
  }

  // Validation for Skills dropdown
  if (selectedSkill === '') {
    isValid = false;
    document.getElementById('careerError').innerText = 'Please select your skills';
    document.getElementById('dropdown').style.borderColor = 'red';
  } else {
    document.getElementById('careerError').innerText = '';
    document.getElementById('dropdown').style.borderColor = '';
  }

   // Validation for PinCode
   if (pinCode === '') {
    isValid = false;
    document.getElementById('pinCodeError').innerText = 'PinCode is required';
    document.getElementById('pinCode').style.borderColor = 'red';
} else if (isNaN(pinCode) || pinCode.length !== 6) {
    isValid = false;
    document.getElementById('pinCodeError').innerText = 'Invalid PinCode';
    document.getElementById('pinCode').style.borderColor = 'red';
} else {
    document.getElementById('pinCodeError').innerText = '';
    document.getElementById('pinCode').style.borderColor = '';
}
// Validation for Password
if (password === '') {
  isValid = false;
  document.getElementById('passwordError').innerText = 'Password is required';
  document.getElementById('password').style.borderColor = 'red';
} else if (!/(?=.*[A-Z])/.test(password)) {
  isValid = false;
  document.getElementById('passwordError').innerText = 'Password must contain at least one uppercase letter';
  document.getElementById('password').style.borderColor = 'red';
} else if (!/(?=.*[a-z])/.test(password)) {
  isValid = false;
  document.getElementById('passwordError').innerText = 'Password must contain at least one lowercase letter';
  document.getElementById('password').style.borderColor = 'red';
} else if (!/(?=.*\d)/.test(password)) {
  isValid = false;
  document.getElementById('passwordError').innerText = 'Password must contain at least one digit';
  document.getElementById('password').style.borderColor = 'red';
} else if (!/(?=.*[\W_])/.test(password)) {
  isValid = false;
  document.getElementById('passwordError').innerText = 'Password must contain at least one symbol';
  document.getElementById('password').style.borderColor = 'red';
} else if (password.length < 8) {
  isValid = false;
  document.getElementById('passwordError').innerText = 'Password must be at least 8 characters long';
  document.getElementById('password').style.borderColor = 'red';
} else {
  document.getElementById('passwordError').innerText = '';
  document.getElementById('password').style.borderColor = '';
}


// Validation for Confirm Password
if (confirmPassword === '') {
    isValid = false;
    document.getElementById('confirmPasswordError').innerText = 'Confirm Password is required';
    document.getElementById('confirmPassword').style.borderColor = 'red';
} else if (confirmPassword !== password) {
    isValid = false;
    document.getElementById('confirmPasswordError').innerText = 'Passwords do not match';
    document.getElementById('confirmPassword').style.borderColor = 'red';
} else {
    document.getElementById('confirmPasswordError').innerText = '';
    document.getElementById('confirmPassword').style.borderColor = '';
}

  return isValid;
}



// Gender selection validation
document.getElementById("registrationForm").addEventListener("submit", function(event) {
  var genderInputs = document.getElementsByName("gender");
  var genderSelected = false;

  for (var i = 0; i < genderInputs.length; i++) {
    if (genderInputs[i].checked) {
      genderSelected = true;
      break;
    }
  }

  if (!genderSelected) {
    document.getElementById("genderError").textContent = "Please select a gender.";
    event.preventDefault(); // Prevent form submission
  } else {
    document.getElementById("genderError").textContent = ""; // Clear error message if gender is selected
  }
});


document.getElementById("registrationForm").addEventListener("submit", function(event) {
  var genderInputs = document.getElementsByName("gender");
  var genderSelected = false;

  for (var i = 0; i < genderInputs.length; i++) {
    if (genderInputs[i].checked) {
      genderSelected = true;
      break;
    }
  }

  if (!genderSelected) {
    document.getElementById("genderError").textContent = "Please select a gender.";
    event.preventDefault(); // Prevent form submission
  } else {
    document.getElementById("genderError").textContent = ""; // Clear error message if gender is selected
  }
});