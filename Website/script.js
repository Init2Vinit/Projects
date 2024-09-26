// using links to change HTML pages on click on the nav bar on header
function changePage(page) {
    var mainContent = document.getElementById("page"); // getting each HTML page and storing it in a variable

    // Fetching and loading the content of the selected page
    fetch(page + '.html') //using fetch API
        .then(response => response.text()) //convert to text
        .then(data => {
            mainContent.innerHTML = data; //replaces the current page with new page clicked
        })
        // error catching if page is not available 
        .catch(error => {
            console.error('Error fetching page content:', error);
        });
}

// form validation when submit button pressed for the registration form
function submitForm() {
    // getting all the elements in the form using their ids
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confPass = document.getElementById("confPass").value;

    // trimming each field and checking for presence
    if (name.trim() === '' || email.trim() === '' || password.trim() === '' || confPass.trim() === '') {
        alert("Please fill in all fields.");
        return;
    }
    // checking if email is valid using another function
    if (!isValidEmail(email)) {
        alert("Please enter a valid email address.");
        return;
    }
    // checking password length to be 8 characters
    if (password.length < 8) {
        alert("Password must be at least 8 characters long.");
        return;
    }  
    // checking if confirm password input matches the password input
    if (password !== confPass) {
        alert("Passwords do not match.");
        return;
    }
    // when everything is validated then the alert returns their name and email
    alert("Registration successful!\nName: " + name + "\nEmail: " + email);
    // clearing the inputs after they submit
    document.getElementById("registrationForm").reset();
}

// email validation using another function that returns back to the main function above
function isValidEmail(email) {
    // checking for correct email format
    var emailRight = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRight.test(email);
}

// form validation when submit button pressed for the contacts form
function submitForm2() {
    // getting all the elements in the form using their ids
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var comment = document.getElementById("comment").value;

    // trimming each field to check for presence
    if (name.trim() === '' || email.trim() === '' || comment.trim() === '') {
        alert("Please fill in all fields.");
        return;
    }
    // checking if email is valid again using the other email function
    if (!isValidEmail(email)) {
        alert("Please enter a valid email address.");
        return;
    }
    // when everything is validated then the alert returns their name and email
    alert("Form successful!\nName: " + name + "\nEmail: " + email);
    document.getElementById("contactForm").reset();
}

// filtering schedule by date
function filterByDate() {
    // defining variables
    var input, filter, table, tr, td, i, txtValue;
    // getting dateFilter element which uses HTML inbuilt date format
    input = document.getElementById("dateFilter");
    filter = input.value;
    // assigning table to the schedule table on schedule page which will be filtered
    table = document.getElementById("scheduleTable");
    // setting tr to the table row element on the schedule table
    tr = table.getElementsByTagName("tr"); 

    // for loop looping through all the rows
    for (i = 0; i < tr.length; i++) {
        // setting td to the first element in the row which is date
        td = tr[i].getElementsByTagName("td")[0];
        // checking for a value in the field, is not null
        if (td) {
            // setting txtValue to the value from the table cell
            txtValue = td.textContent || td.innerText;
            // checks if there is a date in line with the user input
            if (txtValue.indexOf(filter) > -1) {
                tr[i].style.display = ""; // returns the row if yes
            } else {
                tr[i].style.display = "none"; // returns nothing if no
            }
        }
    }
}