/* Load modal Window privacy */
$(document).ready(function() {
    $('body').bsgdprcookies();
});

// Example with custom settings
var settings = {
    message: '(...)',
    messageMaxHeightPercent: 30,
    delay: 1000,
    OnAccept : function() {
        console.log('Yay! User accepted your cookies window!');
    }
}

$(document).ready(function() {
    $('body').bsgdprcookies(settings);
});
