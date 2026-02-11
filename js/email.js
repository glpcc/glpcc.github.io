function sendEmail() {
    var subject = document.getElementById("subject").value;
    var body = document.getElementById("message").value;
  
    var mailtoLink = "mailto:gonzalolopecc@gmail.com";
    mailtoLink += "?subject=" + encodeURIComponent(subject);
    mailtoLink += "&body=" + encodeURIComponent(body);
  
    window.location.href = mailtoLink;
}