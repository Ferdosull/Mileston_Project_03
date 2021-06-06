$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $("#select").formSelect();
    $("#select1").formSelect();
    $("#select2").formSelect();
    $("#select3").formSelect();
    // $("#step2div").hide();
    // $("#step3div").hide();
    // $("#step4div").hide();
    // $("#step5div").hide();
    // $("#step6div").hide();
    // $("#step7div").hide();
    // $("#step8div").hide();
    // $("#step9div").hide();
    // $("#step10div").hide();
});

$("#toTop").click(function () {
    //1 second of animation time
    //html works for FFX but not Chrome
    //body works for Chrome but not FFX
    //This strange selector seems to work universally
    $("html, body").animate({scrollTop: 0}, 1000);
});

$("#copyright").text(new Date().getFullYear());

// https://codepen.io/diegoleme/pen/surIK //

var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Both Passwords Fields Do Not Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

//password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

// Password Validation //

function initStep(a, b, c) { // using button clicks and respective key values to update the function from the object //
    var inputField = document.getElementById(a); // getting the header by id //
    inputField.classList.remove('hide-at-pg-load'); // removing the show yourself class //
    var hideButton = document.getElementById(b); // getting the header by id //
    hideButton.classList.add('hide-at-pg-load'); // removing the show yourself class //
    var showButton = document.getElementById(c); // getting the header by id //
    showButton.classList.remove('hide-at-pg-load'); // removing the show yourself class //
    // transition.classList.add('hide'); // hiding the header element with opacity transition //
}