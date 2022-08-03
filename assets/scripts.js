$(window).scroll(function() {
  var top = $(window).scrollTop();
    if(top>=700){
      $(".up").addClass('.none');
    }
    else if($(".up").hasClass('none')){
      $(".up").removeClass('none');
    }
});

$(".mapa").on("click", function() {
  $(".bttn").toggleClass("bttnb");
  $(this).html() == "Skrýt mapu" ? $(this).html('Ukázat mapu') : $(this).html('Skrýt mapu');

  $(".visible").toggleClass("invisible");

});

  let scrollDiv1 = document.querySelector(".ss-container");
  SimpleScrollbar.initEl(scrollDiv1);


/*
var dropdown = document.getElementsByClassName("sidenav-item-a");
var i;
var x = 0;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;

    var x = 30;
    x.toString();   // returns 123 from expression 100 + 23
    x += "px";

    dropdownContent.style.paddingLeft = x;

    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

*/
