const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");

const optionsList = document.querySelectorAll(".option");

selected.addEventListener("click", () => {
    optionsContainer.classList.toggle("active");
});

optionsList.forEach(o => {
    o.addEventListener("click", () => {
        selected.innerHTML = o.querySelector("label").innerHTML;
        optionsContainer.classList.remove("active");
    });
});


(function ($) {

    $("#id_birthday").datepicker({
        dateFormat: "dd.mm.yy",
        yearRange: "1900:2018",
        changeMonth: true,
        changeYear: true,
        showOn: "both",
        buttonText: '<i class="zmdi zmdi-calendar-alt"></i>',
    });

    $('.add-info-link ').on('click', function () {
        $('.add_info').toggle("slow");
    });

})(jQuery);