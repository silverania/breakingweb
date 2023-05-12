var iframe;
let f = function () {
    var height = "";
    var width = "";
    window.addEventListener("message", function (event) {
        if (!(event.origin.includes('https://localbooldog:8000'))) {
            console.log("messaggio ignorato");
            ("mancata autorizzazione!");
        }
        else {
            height = event.data.height;
            width = event.data.base;
            iframe.setAttribute('height', height);
            iframe.setAttribute('width', width);
            if (event.data.reload === true) {
                document.getElementById('booldogFrame').src = "https://localbooldog:8000/booldog?mainurl=" + this.location.href.toString() + "&user=" + user + "&password=" + password;
                console.log("iframe reload !");
            }
            //iframe.style.height = iframe.contentWindow.document.body.scrollHeight + "px";
        }
    });

    if (height == "") {
        iframe = document.createElement("IFRAME");
        let mainurl = location.href.toString();
        iframe.setAttribute("id", "booldogFrame");
        iframe.setAttribute("scrolling", "no");
        iframe.setAttribute("data-user", user);
        iframe.setAttribute("data-pd", password);
        iframe.setAttribute("style", "display:block;margin:100px auto;width:100%;");
        iframe.setAttribute('src', 'https://localbooldog:8000/booldog?mainurl=' + mainurl + "&user=" + user + "&password=" + password);
        const body = document.getElementsByTagName("body")[0];
        body.appendChild(iframe);
    }
}();