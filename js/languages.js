function changeToSpanish() {

    document.querySelectorAll(".english").forEach(element => {
        element.style.display = "none";
    });
    document.querySelectorAll(".spanish").forEach(element => {
        element.style.display = "block";
    });
}

function changeToEnglish() {
    document.querySelectorAll(".english").forEach(element => {
        element.style.display = "block";
    });
    document.querySelectorAll(".spanish").forEach(element => {
        element.style.display = "none";
    });
}
