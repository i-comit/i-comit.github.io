function blurElement(element, size) {
    var filterVal = 'blur(' + 50 + 'px)';
    $(element).css({
        'filter':filterVal,
        'webkitFilter':filterVal,
        'mozFilter':filterVal,
        'oFilter':filterVal,
        'msFilter':filterVal,
        'transition':'all 0.5s ease-out',
        '-webkit-transition':'all 0.5s ease-out',
        '-moz-transition':'all 0.5s ease-out',
        '-o-transition':'all 0.5s ease-out'
    });
}

$("#logo").click(function(event) {
    blurElement($("body"))
    event.preventDefault();
    delay("./index.html")
});

$("#test").click(function(event) {
    blurElement($("body"))
    event.preventDefault();
    delay("./tests.html")
});

$("#biocompatibility").click(function(event) {
blurElement($("body"))
event.preventDefault();
delay("./biocompatibility.html")
});

$("#certificates").click(function(event) {
    blurElement($("body"))
    event.preventDefault();
    delay("./certificates.html")
});

$("#contact").click(function(event) {
    blurElement($("body"))
    event.preventDefault();
    delay("./contact.html")
});
function delay (URL) {
    setTimeout( function() { window.location = URL }, 180 );
}