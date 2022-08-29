

function setActiveHeaderMenu(element){
  category=element;
  django=$("#a-Django");
  web=  $("#a-Web");
  linux=  $("#a-Linux");
  switch (category){
    case "Django":
    django.addClass('active');
    django.css('background-color','#6fffd9');
    break;
    case "Web":
    web.addClass('active');
    web.css('background-color','#6fffd9');
    break;
    case "Linux":
    linux.addClass('active');
    linux.css('background-color','#6fffd9');
    break;
    default :
    return -1;
  }
}
/*function headerliclick(link){
alert(link);
window.open(link);
}
function headerliactive(active){
alert("menu attivo"+active);
liweb=$('#a-web');
lilinux=$('#a-linux');
lidjango=$('#a-django');
if (active.search(liweb)>0){
liweb.addClass('active');
lilinux.removeClass('active');
lidjango.removeClass('active');
}
else if(active.search(lilinux)>0){
lilinux.addClass('active');
liweb.removeClass('active');
lidjango.removeClass('active');
}
}*/
