// functions carried out once the page has loaded and the document is ready.
$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $("#select").formSelect();
    $("#select1").formSelect();
    $("#select2").formSelect();
    $("#select3").formSelect();
    $('.modal').modal();
});


// function to return the user to the top of the page triggered by link in the footer.
$("#toTop").click(function () {
    $("html, body").animate({scrollTop: 0}, 1000);
});


// function to pull the current year and place it in the footer.
$("#copyright").text(new Date().getFullYear());


// The following JS function example was found while searching for double password confirmation. 
// https://codepen.io/diegoleme/pen/surIK
var password = document.getElementById("password");
var confirm_password = document.getElementById("confirm_password");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Both Passwords Fields Do Not Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

confirm_password.onkeyup = validatePassword;


// hiding and showing "Add Steps" and step input fields as required by the user.
function initStep(a, b, c) { // using button clicks and id variables passed from the HTML.
    var inputField = document.getElementById(a); // getting the Input Field by id.
    inputField.classList.remove('hide-at-pg-load'); // removing the hide-at-pg-load class.
    var hideButton = document.getElementById(b); // getting the clicked button by id.
    hideButton.classList.add('hide-at-pg-load'); // adding the hide-at-pg-load class.
    var showButton = document.getElementById(c); // getting the next button to show by id.
    showButton.classList.remove('hide-at-pg-load'); // removing the hide-at-pg-load class.
}


// function to hide the flash messages generated from user actions.
function flashHide(){
    var flashDiv = document.getElementById("flash"); // getting the Flash DIV by id.
    flashDiv.classList.add('hide-at-pg-load'); // adding the hide-at-pg-load class.
}


// function to add a default value to the URL input based upon the users input.
// the function also hides the inputted URL so that the user cannot make changes to it anymore.
function noUrl(a, b){
    document.getElementById(a).value = "https://none"; // getting an element by id and assigning it a value.
    var hideUrl = document.getElementById(b) // getting the URL DIV by id.
    hideUrl.classList.add('hide-at-pg-load'); // adding the hide-at-pg-load class.
}

// fixing the issue on mobile where the tooltip is still present after clicking the button.
function hideTooltip(a){
    var toolTip = document.getElementById(a); // getting the tool tipped button by id.
    toolTip.classList.remove('tooltipped'); // adding the hide-at-pg-load class.
}
