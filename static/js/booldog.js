let f = function () {
    var height = "";
    var width = "";
    window.addEventListener("message", function (event) {
        if (!(event.origin.includes('https://localbooldog:8000'))) {
            console.log("messaggio ignorato");
            return -1;
            ("mancata autorizzazione!")
        }
        else {
            height = event.data.height;
            width = event.data.base;
            iframe.setAttribute('height', height);
            iframe.setAttribute('width', width);
            //iframe.style.height = iframe.contentWindow.document.body.scrollHeight + "px";
        }
    });

    if (height == "") {
        var iframe = document.createElement("IFRAME");
        let mainurl = location.href.toString();
        iframe.setAttribute("id", "booldogFrame");
        iframe.setAttribute("scrolling", "no");
        iframe.setAttribute("style", "display:block;margin:100px auto;width:100%;");
        iframe.setAttribute('src', 'https://localbooldog:8000/booldog?url=' + mainurl);
        const body = document.getElementsByTagName("body")[0];
        body.appendChild(iframe);
    }
}();