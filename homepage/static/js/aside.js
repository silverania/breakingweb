$(document).ready(function(){
  height_footer=window.innerHeight/6;
//document.getElementById('div_main_footer').setAttribute("style","height:"+height_footer+"px");
  var object=$('#progress');
  var topNav=$('#nav_top');
  var WINDOW_WIDTH=window.innerWidth;
  var horizontalHeaderMenuPosition=(window.innerWidth/2).toString();
  var table_tutorial=$('#d_tutorial_section');
  var navleft=$('#section_left_navbar');
  mydiv=document.getElementById('d_divaside');
  headWeb=$('#a-Web');
  headLinux=$('#a-Linux');
  headDjango=$('#a-Django');
  var s = $("a[id^='a_html']");
  var off;
  var toHCenter=$(document).innerWidth()/2;
  var toBegin="0px";
  var divaside=document.getElementById('d_divaside');
  var table_tutorial_WIDTH=table_tutorial.css('width');
  var table_tutorial_WIDTH_initial_position=(parseInt(table_tutorial_WIDTH))+15;
  table_tutorial.css('margin-left', -table_tutorial_WIDTH_initial_position );

  function showTutorial() {
    table_tutorial.css('display','block');
    table_tutorial_width=(parseInt(table_tutorial.css('width'),10));
    off=table_tutorial_width;
    $('#d_tutorial_section').animate({'margin-left': '-18px'},200);
    $('#asidebar').animate({ "margin-left" : '0px','opacity' : '0.9',},100);
    $('#asidebar').animate({ "margin-left" : '15px','opacity' : '0.1',},100);
    $('#asidebar').css('color','green');
}
// Animazione destra-sinistra dell elemento Angle-Right
  $('#asidebar').hover(function(){
    showTutorial()
  },
  /* quando il mouse si allontenerà dalla freccia quest' ultima tornerà nella posizione iniziale e l' opacita tornerà a 1*/
  function(){
    $('#asidebar').animate({ "margin-left" : '0px','opacity' : '1',},100);
      $('#asidebar').css('color','black');
  }
);
  // END

/* Imposto la base del menu in base alla base dello schermo */

/*Se la table tutorial è in posizione left=0 vuol dire che è visibile , quindi l 'evento click su angle , la nascondera
di nuovo ponendola in posizione margin-left= -510px' .......e viceversa
*/
$('#asidebar').click(function(event){
  $("li[id^='option_autori']").style.fontSize("2rem")
  //$("li[id^='tutorial_id_']").style.minWidth="1000px!important"
  table_tutorial.css('display','block');
  table_tutorial_width=(parseInt(table_tutorial.css('width'),10));
  off=table_tutorial_width+18;
  $target = $(event.target);
  let x=$('#d_tutorial_section').offset().left;

    // l 'elemento table_tutorial deve ritornare a 0px anche quando clicco sulla freecia , oltre che nell hover della freccia !'
      if ( table_tutorial.offset().left<0) {
        $('#d_tutorial_section').animate({'margin-left': '-18px'},200);
      }
    // FINE COMMENTO

  /* se left  è > 0 : vuol dire che l elelemento table_tutorial è visibile quindi lo mando a fan culo nuovamente nei meandri del monitor
 pronto a ritornare davanti ai coglioni al momento giusto .......o sbagliato , a secondo del punto di vista
  */
    if ( table_tutorial.offset().left > -18) {
      //hideTutorial();
      //deleteTutorial();
      exist=0
    }
}
);






// funzioni per visulizzare menu clickati
function showHtmlMenu(){
  $('#d_Web_menu').css('display','block'); // mostro il menu che mi interessa
  $('#d_Django_menu').css('display','none');// nascondo questo menù nel caso sia visibile
  $('#d_Linux_menu').css('display','none');// nascondo questo menù nel caso sia visibile
}
function showLinuxMenu(){
  $('#d_Linux_menu').css('display','block'); // mostro il menu che mi interessa
  //  $('#a_tutorial_pdf_converter').css('display','block');// mostro il menu che mi interessa
  $('#d_Django_menu').css('display','none');// nascondo questo menù nel caso sia visibile
  $('#d_Web_menu').css('display','none');// nascondo questo menù nel caso sia visibile
}
function showDjangoMenu(){
  $('#d_Django_menu').css('display','block'); // mostro il menu che mi interessa
  //$('#a_tutorial_django_urls').css('display','block'); // mostro il menu che mi interessa
  $('#d_Linux_menu').css('display','none');// nascondo questo menù nel caso sia visibile
  $('#d_Web_menu').css('display','none');// nascondo questo menù nel caso sia visibile
}
// END #####################################

//gestione  click sui pulsanti sull header
$("li[id^='a-']").click(function(){
  text=(this.id);
  var topOffset=mydiv.offsetTop;
  var leftOffset=mydiv.offsetLeft;
  if(leftOffset>0){
    $('.d_divaside').animate({ "left" : -(horizontalHeaderMenuPosition),"margin-top" : "-30%"},200);
      $('.d_divaside').animate({ "left" : -(horizontalHeaderMenuPosition),"margin-top" : "90%"},200);
      $('.d_divaside').animate({ "left" : horizontalHeaderMenuPosition,"margin-top" : "0" },200);
    showHeader(text);
  }
  else{
    showHeader(text);
    $('.d_divaside').css('display', 'block');
    //$('.d_divaside').css('position', 'absolute');
    $('.d_divaside').animate({ "left" : horizontalHeaderMenuPosition,"top" : "0px" },200);
  }
  function showHeader(text){
  switch (text){
    case "a-Web":
    showHtmlMenu();
    break;
    case "a-Linux":
    $('#d_Linux_menu').css('display','block');
    $('#d_Web_menu').css('display','none');// nascondo questo menù nel caso sia visibile
    $('#d_Django_menu').css('display','none');// nascondo questo menù nel caso sia visibile
    break;
    case "a-Django":
    $('#d_Linux_menu').css('display','none');
    $('#d_Web_menu').css('display','none');// nascondo questo menù nel caso sia visibile
    $('#d_Django_menu').css('display','block');// nascondo questo menù nel caso sia visibile
    break;
    default :
  }
}
});
/*  THE END */

/*nascondo tutto se clicco al di fuori del elemento*/
$(document).click(function(event) {

  let x=$('#d_divaside').offset().left;
  $target = $(event.target);
  if(!$target.closest('.d_divaside').length && !$target.closest('.fa-angle-right').length && !$target.closest('#header_menu').length && !$target.closest('.fa-angle-right').length && !$target.closest('#d_tutorial_section').length && ($('#d_tutorial_section').css("margin-left")=="-18px" || x>=0) && !$target.closest('#ul_in_selecFormAutori').length) {
    if(x>=0) {
      $('#d_divaside').css( 'left' , '-700px');
    }
      hideTutorial();
  }
  /* intercetto il click nell elemento li che contiene i nomi autore dei tutorial*/
  if($target.closest('#d_tutorial_section').length)
  {
    shift=$('#d_inside_tutorial_section').css('left')
    shift=shift.replace("px","")
      if(shift>0){
    if (deleteTutorial()==0)  {
      console.log("deletetutorial=0")
    }
  }
}
});
function animateTutorial()  {
  $('#d_inside_tutorial_section').animate({'left':'-700px'},200);
  return 0
}

function hideTutorial() {
  $('#d_tutorial_section').animate({'margin-left': -off },300);
    $('#d_tutorial_section').css('display','none');
    $('#d_inside_tutorial_section').css('display','none');
}

function deleteTutorial() {
  if (animateTutorial()==0){
    try {
      $('.li_tutorials').remove();
      exist=0
  }
  catch(typeError){
    console.log("l elemento element è nullo")
    exist=1
  }
}
  return exist
}
});

/* CREO LA PROGRESSBAR IN SEGUITO A EVENTO SCROLL IN HTML*/
function getPosition() {

      docBodyScrollHeight=document.body.scrollHeight;
      docDocElementScrollHeight=document.documentElement.scrollHeight;
      docBodyOffsetHeight=document.body.offsetHeight;
      docDocElementOffsetHeight=  document.documentElement.offsetHeight;
      docBodyClientHeight=document.body.clientHeight;
      docDocElementClientHeight=document.documentElement.clientHeight;
      let totalHeight = Math.max(
      document.body.scrollHeight, document.documentElement.scrollHeight,
      document.body.offsetHeight, document.documentElement.offsetHeight,
      document.body.clientHeight, document.documentElement.clientHeight
    );
     val=docDocElementOffsetHeight-docDocElementClientHeight;
  let tagElmnt = document.getElementById("page");
  var actualHeight = document.documentElement.scrollTop;
  /*alert(actualHeight+"val_"+docBodyScrollHeight+"_"+docDocElementOffsetHeight+"_docbodyoffsetheight"+docBodyOffsetHeight
  +"docDocElementOffsetHeight"+docDocElementOffsetHeight+"docBodyClientHeight"+docBodyClientHeight+"docDocElementClientHeight"+docDocElementClientHeight);*/
  let rapport=parseInt((actualHeight/val)*100);

  createProgressBar(rapport);
}

function createProgressBar(actualValue){
  var object=document.getElementById('progressbar');
  object.value=parseInt(actualValue,10);
}
