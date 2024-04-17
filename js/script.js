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

function ShowMoreProjects() {
    document.querySelectorAll(".less_important").forEach(element => {
        element.style.display = "block";
    });
    document.getElementById("btn-projects-more").style.display = "none";
};

function ShowLessProjects() {
    document.querySelectorAll(".less_important").forEach(element => {
        element.style.display = "none";
    });
    document.getElementById("btn-projects-more").style.display = "block";
}