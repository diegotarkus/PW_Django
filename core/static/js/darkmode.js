$(document).ready(function () {
    $('#modo').click(function () {
        var element = document.body;
        element.classList.toggle("dark");
        localStorage.setItem("dark", dark);
        console.log("Modo oscuro activado");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem('dark')) {
        element.classList.toggle('dark');
    }
})
