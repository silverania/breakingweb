BASE_URL="http://127.0.0.1:8000"
URL_NEW_POST="/post/sendpost"
const MAX_TEXTAREA_NUMBER=21
const BASE_PHOTO_DIR="media/"
var borderPost="none";
var borderResponse="1px solid grey";
var paPostOrResp;
var postarea=Object()
var el
var mess;
var padre
var user
var loginis
var lastUpdate
var userLogged
var butcloned
var isChanged=false
var bbutton=document.createElement("Button");
var resps
var tagTitle
//var bUserImg=document.createElement("IMG");
var divFormChild=document.createElement("DIV");
var bdiv=document.createElement("DIV");
var divUserBlog=document.createElement("DIV");
var divCommentIcon=document.createElement("DIV");
var firstDivHead=document.createElement("DIV");
var divRespTitle=document.createElement("DIV");
var divExitLogin=document.createElement("DIV");
var divEmpty=document.createElement("DIV");
var divBlogReg=document.createElement("DIV");
var ulBlogReg=document.createElement("UL");
var liBlogReg=document.createElement("LI");
var aBlogReg=document.createElement("A");
var spanBlogReg=document.createElement("SPAN");
var liBlogEntra=document.createElement("LI");
var aBlogEntra=document.createElement("A");
var spanBlogEntra=document.createElement("SPAN");
var liBlogEsci=document.createElement("LI");
var aBlogEsci=document.createElement("A");
var spanBlogEsci=document.createElement("SPAN");
var post,post2=new Object()
var isOpen=false
var bSection=document.createElement("SECTION")
//var bSpan=document.createElement("SPAN");
//var bSpanChild=document.createElement("SPAN");
var bIcon = document.createElement("H1")
    var t = document.createTextNode("Messages")
    bIcon.appendChild(t)
var bForm=document.createElement("FORM");
var title=document.getElementsByTagName('title')[0].innerText
var wait=true
var postTitle
var tutorial
var bbutton2=new Object();
var exist=new Boolean(false)
var newPostId=0
var elementToAppendPostArea
var json_resps
var re

function createSectionDivSpan(){
  bForm.setAttribute("action","post/getpost");
  bForm.setAttribute("class","form_comment")
  //divUserBlog.setAttribute("style","width:45%;display:inline-block;")
  firstDivHead.setAttribute("style","width:45%;display:inline;")
  firstDivHead.setAttribute("id","firstDivHead")
  divExitLogin.setAttribute("style","width:45%;display:inline;")
  divCommentIcon.setAttribute("id","div_comment_icon")
  divCommentIcon.setAttribute("style","margin:0 auto")
  divRespTitle.setAttribute("class","div_resp")
  //divEmpty.setAttribute("style","width:20%;display:inline-block;")
  divFormChild.setAttribute("id","multiarea");
  //divFormChild.setAttribute("class","form-group");
  divExitLogin.setAttribute("id","d_blog_reg")
  divExitLogin.setAttribute("style","width:45%;display:inline-block;")
  bdiv.setAttribute("id","bdiv")
  //bIcon.setAttribute('src',"../../../static/images/blog_comment.gif")
  //bIcon.setAttribute("WIDTH","50px")
  bIcon.setAttribute("style","text-align:center;font-weight:bold;")
  bIcon.setAttribute("id","blog_icon")
  bSection.setAttribute("id","blog");
  bSection.setAttribute("style","width:100%");
  //bSpan.setAttribute("id","s_blog_icon")
  aBlogEntra.setAttribute("style","display:block;width:auto;text-align:right;")
  aBlogReg.setAttribute("style","display:block;width:auto;text-align:right;z-index:200")
  aBlogReg.setAttribute("href","/user/register")
    aBlogReg.setAttribute("href","/user/register")
  aBlogEntra.setAttribute("href","/user/login")
aBlogEntra.setAttribute("class","nav-link")
  aBlogEsci.setAttribute("href","/user/logout")
  liBlogEntra.setAttribute("style","display:inline;width:auto;margin-right:0px;")
liBlogEntra.setAttribute("class" , "nav-item")
  //bSpanChild.setAttribute("id","s_blog_text")
  bbutton.setAttribute("id","button_post")
  //bH5.setAttribute("id","span_blog_entra")
  bbutton.setAttribute("type","button")
  bbutton.setAttribute("class","mybut mybut-outline-info ")
  spanBlogEntra.setAttribute("id","span_entra")
  spanBlogReg.setAttribute("id","span_reg")
  divBlogReg.setAttribute("id","div_blog_reg")
  bbutton.textContent="Commenta"
  spanBlogReg.textContent="Registrati"
  spanBlogEntra.textContent="Entra"

  spanBlogEsci.textContent="Esci"
  ulBlogReg.setAttribute("id","ul_blog")
  ulBlogReg.setAttribute("style","list-style: none;padding: 0;margin: 0;")
  parent=document.body.insertBefore(bSection,document.getElementsByTagName("footer")[0]);
  if(loginis=="anonimo"){
    console.log(loginis)
    aBlogReg.appendChild(spanBlogReg)
    liBlogReg.appendChild(aBlogReg)
    aBlogEntra.appendChild(spanBlogEntra)
    liBlogEntra.appendChild(aBlogEntra)
    ulBlogReg.appendChild(liBlogReg)
    ulBlogReg.appendChild(liBlogEntra)
    divExitLogin.appendChild(ulBlogReg)
    //bSection.appendChild(divExitLogin)
  }
  else {
    aBlogEsci.appendChild(spanBlogEsci)
    aBlogEsci.setAttribute("style","display:block;width:auto;text-align:right")
    liBlogEsci.appendChild(aBlogEsci)
    ulBlogReg.appendChild(liBlogEsci)
    divExitLogin.appendChild(ulBlogReg)
    bSection.appendChild(divBlogReg)
  }
  //bH5.appendChild(spanUserName)
  bSection.appendChild(bdiv)
  bdiv.appendChild(firstDivHead)
  bdiv.appendChild(divCommentIcon)
  bdiv.appendChild(divExitLogin)
  divCommentIcon.appendChild(bIcon)
  //divUserBlog.appendChild(bSpan)
  //bSpan.appendChild(bSpanChild)
  bSection.appendChild(bForm)
  bForm.appendChild(divFormChild)
  $(parent).prepend(divCommentIcon)
  divFormChild.appendChild(bbutton)

}

class Resp{
  constructor(author,body="",publish,post,photo,titolo,pk,resptype){
    this.sent = false
    this.author = author
    this.post = post
    this.body = body
    this.type = resptype
    this.publish = publish
    this.photo = photo
    //this.titled=titolo

    if (resptype=="newresp") {
      this.pk = parseInt(pk,"10")
      this.pk=pk+1
    }
    else {
      this.pk=pk
    }
    this.thisTutorialTitle=tutorial
  }
}

class Profile{
  constructor(author="anonimo",photo=""){
    this.photo=photo
  }
}

class Post{
  constructor(type="none",author="anonimo",title1,comment,date,photo,pk){
    this.sent=false
    this.type=type
    this.author=author
    this.risposte=new Array()
    this.body=comment
    //this.titled=title1
    this.photo=photo
    this.publish=date
    this.pk=pk
    this.thisTutorialTitle=tutorial
  }
}


class postArea {
  constructor(post){
    this.post=post
    this.postarea=document.createElement("TEXTAREA");
    this.isActive=false
    this.isChanged=isChanged

    this.postarea.onkeyup = function(){
      // textarea resize in base al testo inserito

      //$("textarea").each(function () {
        //this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
      //})
    //    this.on("input",
      //  function () {
        this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
    //  }
  //  )
    //  })

      isChanged=true
      this.isChanged=true
      var callcount = 0;
      var action = function(){

      }
      var delayAction = function(action, time){
        var expectcallcount = callcount;
        var delay = function(){
          if(callcount == expectcallcount){
            action();
          }
        }
        setTimeout(delay, time);
      }
      return function(eventtrigger){
        ++callcount;
        delayAction(action, 200);
      }
    }
    //var mess=""
    switch (post.type){
      case "newpost":
      this.postarea.removeAttribute("disabled","")
      break
      case "newresp":
      this.postarea.removeAttribute("disabled","")
      break
      case "post":
      this.postarea.value=post.body
      this.postarea.setAttribute("disabled","")
      break
      case "resp":
      this.postarea.value=post.body
      this.postarea.setAttribute("disabled","")
      break
    }
  }

  appendPostArea(mess,divuserblog){
    if(mess.type=="newpost"){
      var elToAppend=document.getElementById('button_post')
      $ ( divuserblog ).insertAfter(elToAppend)
    }
    else if (mess.type=="newresp") {
      $ ( divuserblog ).insertAfter( elementToAppendPostArea )
    }
    else{
      bdiv.appendChild(divuserblog)
    }
    //postarea.postarea.setAttribute("id","postarea_"+postarea.pk)
  }

  makeHeadBlog(mess,postarea,elementToAppendPostArea){
    if(!(isOpen==true)) {
      var id
      mess.type == "resp" || mess.type == "newresp" ? id = mess.post.pk + "_" + mess.pk : id = mess.pk
      //if (!(id=="undefined")) mess.pk = id
      //var divPostTitle=document.createElement("DIV");
      //var spanInDivPostTitle=document.createElement("SPAN")
      divUserBlog = document.createElement( "DIV" )
      var spanUserName=document.createElement("SPAN")
      var spanInUserName=document.createElement("SPAN")
      var bH5=document.createElement("span")
      var divContainerHead=document.createElement("DIV")
      var tagUserImg=document.createElement("IMG")
      divContainerHead.setAttribute("id","d_head_blog_"+id)
      divContainerHead.setAttribute("style","width:100%")
      //divContainerHead.setAttribute("style","height:auto")
      tagUserImg.setAttribute("style","border-radius:50%")
      tagUserImg.setAttribute("src",mess.photo)
      divUserBlog.appendChild(divContainerHead)
      divContainerHead.appendChild(tagUserImg)
      //bH5.textContent="il "+mess.publish
      spanUserName.setAttribute("style","color:grey;display:inline;")
      spanInUserName.setAttribute("style","color:black;display:inline;")
      //spanInDivPostTitle.setAttribute("id","post_title_"+id)
      //divPostTitle.setAttribute("id","d_post_title_"+id)
      //divPostTitle.appendChild(spanInDivPostTitle)
      bH5.setAttribute("style","margin-left:3%;color:blue;")
      bH5.setAttribute("id","bh5_span_"+id)
      bH5.appendChild(spanInUserName)
      bH5.appendChild(spanUserName)
      divContainerHead.appendChild(bH5)
      //divUserBlog.appendChild(divPostTitle)
      this.appendPostArea(mess,divUserBlog)
      tagUserImg.setAttribute("id","img_user_"+id)
      spanUserName.setAttribute("id","span_user_"+id)
      spanInUserName.setAttribute("id","span_inuser_"+id)
      postarea.postarea.setAttribute("id",mess.type+loginis+"_"+id)
      switch (mess.type){
        case "newpost":
        divUserBlog.setAttribute("id","divuserblog_"+id)
        divUserBlog.setAttribute("class","new_post_"+id)
        $(document).on('click', function(e){
          if ($(e.target).closest("#divuserblog_"+id).length === 0 && $(e.target).closest("#button_post").length === 0 && $(e.target).closest(".form_comment").length === 0 ) {
            if (isChanged==false) {
              $("#divuserblog_"+id).remove()
              isOpen=false
            }
          }
          //  $('#button_risposta_post').click()
        })
        break
        case "resp":
        //divUserBlog.setAttribute("class","resp_"+id)
        divUserBlog.setAttribute("id","divuserblog_"+id)
        spanInUserName.textContent=mess.author[0].toUpperCase() +mess.author.slice("1")
        spanUserName.textContent=" | " +mess.publish
        divUserBlog.setAttribute("style","margin-left:20%")
        console.log("is resp ")
        break
        case "post":
        divUserBlog.setAttribute("id","divuserblog_"+id)
        divUserBlog.setAttribute("class","post_"+id)
        break
        case "newresp" :
        var id_newresp = id.toString()
        id_newresp="_new_"+id_newresp
        postarea.isActive=true
        divUserBlog.setAttribute("id","divuserblog_"+id_newresp)
        divUserBlog.setAttribute("style","margin-left:20%")
        spanInUserName.textContent=mess.author[0].toUpperCase() +mess.author.slice("1")
        spanUserName.textContent=" | " +mess.publish
        elementToAppendPostArea=elementToAppendPostArea
        postarea.postarea.setAttribute("id",mess.type+loginis+"_"+id_newresp)
        $(document).on('click', function(e){
          //if ($(e.target).closest("#divuserblog_"+id_newresp).length === 0) {
        if ($(e.target).closest('*[id^="divuserblog"]').length===0){
            if (isChanged==false) {
              $("#divuserblog_"+id_newresp).remove()
              isOpen=false
            }
          }
          //  $('#button_risposta_post').click()
        })
        default:
        console.log("def")
      }
      this.mess=mess
      if(mess.type=="post" || mess.type=="newpost" ) {
        if(!(postarea.disabled==true)){
          spanUserName.textContent=mess.publish
          spanInUserName.textContent=mess.author[0].toUpperCase() +mess.author.slice("1")+" , "
          //spanInDivPostTitle.textContent=mess.titled[0].toUpperCase()+mess.titled.slice("1")
          console.log("thispost.disabled")
          $('#post_response').css("border", "1px solid grey")
          bbutton.textContent="Nuovo Post"
          var idWherePutElement="button_post"
          console.log(idWherePutElement)
        }
      }
      divUserBlog.appendChild(postarea.create())
      if(mess.type=="newpost") {
        postarea.isActive=true
        if(postarea.isActive==true){
          $("#"+postarea.postarea.id).css("border","4px solid blue")
        }
      }
      return $(divUserBlog)
    }
  }

  createButtonRispostaPost(mess,postarea){
    var r
    var id
    mess.type == "resp" || mess.type == "newresp" ? id = mess.post.pk + "_" + mess.pk : id = mess.pk
    var button_risposta_post=document.createElement("BUTTON")
    var form_risposta_post=document.createElement("FORM")
    var objectToAppendChild=divUserBlog.id
    button_risposta_post.setAttribute('style','display:block')
    form_risposta_post.appendChild(button_risposta_post)
    var url;
    $(button_risposta_post).click(function(e){
      e.stopPropagation()
      if (mess.type=="resp" || mess.type=="post") {
        if(isOpen==false) {
          elementToAppendPostArea = document.getElementById("divuserblog_"+id)
          if(mess instanceof Resp) {
            var post=mess.post
          }
          else if (mess instanceof Post) {
            var post=mess
          }
          var ids = (resps.length)
          ids = ids + 1
          createPostArea
          ( r=new Resp(loginis,"", new Date().toLocaleString(),post,BASE_PHOTO_DIR+userLogged[0].fields.photo," risponde a "+mess.author,ids,"newresp"),elementToAppendPostArea)
          resps.push(r)
        }
        else if ( button_risposta_post.textContent=="Rispondi" && isOpen==true ){
          msgIsTexareaOpen()
        }
      }
    }
  )
  $(button_risposta_post).hover(function(){
    $(button_risposta_post).animate({'width':'33%'},200);
    $(button_risposta_post).animate({'left':'33%'},200);
    $(button_risposta_post).css('box-shadow', '0 0 0 white' );//#719ECE"
  },
  function(){
    $(button_risposta_post).animate({'width':'100%'},200);
    $(button_risposta_post).css('box-shadow', '10px 10px 10px #719ECE' );
  }
)
switch (mess.type){
  case "newpost" : case "newresp" :
  postarea.isActive=true
  button_risposta_post.textContent="Invia"
  $(button_risposta_post).click(function(){
    //autorizzo la creazione del nuovo post solo se è valido: contiene testo ecc..
    let ids='#'+postarea.postarea.id
    let txts=$(ids).val()
    try{
      if (txts==""){
        throw  "Post Vuoto ! ";
      }
    }
    catch (err){
      console.log("area di testo vuota . Exit code -1 !")
      return -1
    }
    console.log("comparazione del tipo e valore = vera in:"+txts)
    //form_risposta_post.setAttribute("action",url)
    url=BASE_URL+URL_NEW_POST
    mess.body=txts
    if (sendToServer(mess,url)==0){
      isOpen=false
    }
    //button_risposta_post.setAttribute('action','url')
    $(postarea.postarea).css("box-shadow","0 0 0 0")
    mess.type=="newpost" ? button_risposta_post.textContent="Post Inserito" : button_risposta_post.textContent="Risposta Inserita"

    button_risposta_post.setAttribute("disabled","")
    postarea.postarea.setAttribute("disabled","")
    $(postarea.postarea).css("color" ,"rgba(0, 0, 0, 0.5)");
    $(postarea.postarea).css("border" ,"2px solid grey");
    $(button_risposta_post).css("color" ,"black");
  }
);
break
case "post":
var objectToAppendChild=divUserBlog.id
button_risposta_post.textContent="Rispondi"
break
case "resp" :
var objectToAppendChild="divuserblog_"+id
button_risposta_post.textContent="Rispondi"
break
}
var elementToAppendButton=document.getElementById(objectToAppendChild)
elementToAppendButton.appendChild(form_risposta_post)
setButtonAndFormAttribute(id)

function setButtonAndFormAttribute(type){
  let buttonID="but_"+mess.type+"_"+type
  button_risposta_post.setAttribute("type","button")
  button_risposta_post.setAttribute("id",buttonID)
  form_risposta_post.setAttribute("id","form_"+mess.type+"_"+id)
  form_risposta_post.setAttribute("class","form_"+mess.type+"_"+id)
}
}

disableButton(button){
  button.setAttribute("disabled","")
}

create(){
  $(this.postarea).animate({'width':'100%'},1200);// nu second e dui 1,2sec
  this.postarea.setAttribute("rows","2");
  this.postarea.setAttribute("name","messaggio")
  $(this.postarea).css("border", borderPost)
  this.postarea.setAttribute("title","Autenticarsi NON è Obbligatorio !")
  return this.postarea;
}

}


function initBlogSGang(login,parTagTitle,id){
  if(login=="False"||login=="false"||login=="none"||login=="AnonymousUser"){
    loginis="anonimo"
  }
  else{
    loginis=login
  }
  idis=id;
  //tutorial=tut
  tagTitle=parTagTitle
  createSectionDivSpan(idis);
}

/* Primo funzione eseguita nel flusso di codice , ...... l' entrypoint.... */
$(bbutton).click(function() {
if(userLogged[0].fields.user!="anonimo"){
  if(isOpen==false) {
    buttonCommentClick()
  }
  else {
    msgIsTexareaOpen()
  }
}
else{
  window.open("/user/login")
  }
}
)


function buttonCommentClick(){
  let modal
  let textAreaInDivInMain
  let result
  var divModalMain
  var divInMain
  var modalConfirmButton
  // caso del primo click su comment , in cui la textarea non è visibile e quindi anche = empty
  function instancePost(){
    let mess=Object()
    //var titleNewPost=makeModalWindow(this.post=instancePostarea())
    if(!(mess instanceof Post)){
      exist=false
      mess= new Post("newpost",loginis)
      if(exist==false){
      createNewComment(mess)
      location.href="#blog"
    }
    }
    exist=true
    Boolean(exist)
  }

  if (!(post instanceof postArea ))
  {
    //post=instancePostarea()
    post=instancePost()
  }
}

//function makeModalWindow(mess){
  //newPostId=newPostId+1
  //if(exist==false){
    //divModalMain=document.createElement("DIV");
    //divInMain=document.createElement("DIV");
    //textAreaInDivInMain=document.createElement("TEXTAREA");
    //modalConfirmButton=document.createElement("Button");
    //var checkValidity=false
    //modalConfirmButton.setAttribute('id','but_confirm_title')
    //modalConfirmButton.setAttribute('type','button')
    //divModalMain.setAttribute('class','modal')
    //divModalMain.setAttribute('id','myModal')
    //divInMain.setAttribute('class','modal-content')
    //textAreaInDivInMain.setAttribute("id","p_text")
    //textAreaInDivInMain.setAttribute("rows","1")
    //textAreaInDivInMain.value="Titolo Post ?"
    //divInMain.appendChild(textAreaInDivInMain)
    //divInMain.appendChild(modalConfirmButton)
    //divModalMain.appendChild(divInMain)
    //body.appendChild(divModalMain)
    //modal = document.getElementById("myModal");
    //modal.style.display = "block";
    //exist=true
  //}
  //else{
    //modal.style.display = "block";
  //}
function createNewComment(mess){
  //  try{
      //let txt=$("#p_text").val()
      //if (!(txt=="Titolo Post ?")){
        mess.titled="nuovo"
        newPostId=newPostId+1
        mess.type="newpost"
        mess.publish=getDateFromDjangoDate()
        mess.author=loginis
        userLogged[0].fields.photo == "undefined" ? alert  ("non ho la photo dell user !") :  mess.photo=userLogged[0].fields.photo
        mess.pk=newPostId
      //  if(mess.titled){
        //  $('#myModal').remove()
        //  createPostArea(mess)
        //  exist=false
        //}
        createPostArea(mess)
        if(exist==false){
          Boolean(exist)
        return mess
      }
    }
      //else{
        //alert("Devi inserire un titolo Valido")
      //}

    //catch(Error){
      //console.log("qualcosa è andato storto nel recupero del titolo")




// se la variabile data non viene passata come parametro si presuppone che il client abbia creato un nuovo post , quindi //la data è now
function getDateFromDjangoDate(data=""){
  var dateNow = new Date()
  //var dataDjango=new Date(data)
  var dataDjango
  var data1
  var data2
  isNow = function() {
    data1 =dataDjango.getDate()
    data2 = dateNow.getDate()
    return data1==data2
  }
  var newDate
  var day,month,year,hour
  if (  data==""){
    var dataDjango=new Date()
    var today = new Date();
    day = String(today.getDate()).padStart(2, '0');
    day=isNow()
    month = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    month = getMonth(month)
    year = today.getFullYear();
    hour=today.getHours().toString()+":"+today.getMinutes().toString()
    data=getMsg()
    var dataDjango=new Date(data)
  }
  else {
      var dataDjango=new Date(data)
    day=data.slice("8","10")
      month=data.slice("5","7")
      month=getMonth(month)
    year=data.slice("0","4")
    hour=data.slice("11","16")
    data=getMsg()
  }
  function getMonth(month){
    var res
    switch (month) {
    case "01" : res="gennaio"
    break
    case "02" : res="febbraio"
    break
    case "03" : res="marzo"
    break
    case "04" : res="aprile"
    break
    case "05" : res="maggio"
    break
    case "06" : res="giugno"
    break
    case "07" : res="luglio"
    break
    case "08" : res="agosto"
    break
    case "09" : res="settembre"
    break
    case "10" : res="ottobre"
    break
    case "11" : res="novembre"
    break
    case "12" : res="dicembre"
    break
    }
    return res
  }
  function getMsg(){
    if (isNow()){
      data="Oggi alle"+" "+hour
    }
    else{
      day=day.replace("0","")
      data=day+" "+month+" "+year+" alle "+hour
    }
    return data
  }
  newDate=data
  return newDate
}

function cleanJson(json){
  this.data=json.toString()
  s = this.data.replace(/\\n/g, "\\n")
  .replace(/\\'/g, "\\'")
  .replace(/\\"/g, '\\"')
  .replace(/\\&/g, "\\&")
  .replace(/\\r/g, "\\r")
  .replace(/\\t/g, "\\t")
  .replace(/\\b/g, "\\b")
  .replace(/\\f/g, "\\f")
  return s
}

$(document).on("load" ,function(){
  //var itm = document.getElementsByClassName("form_comment")[0];
  //var cln = itm.cloneNode(true);
  //bdiv.appendChild(cln)[2];
})


$(document).ready(function(){
  var obj
  var indexX=0
  var initial_y
  var y=0,s
  mess=new Array()
  resps=new Array()
  var post = new Array()
  let profiles=new Array()
  let z=0
  var q=0
  let comments_json;
  var itm = document.getElementsByClassName("form_comment")[0];
  //var cln = itm.cloneNode(true);
  //cln.getElementsByClassName('mybut')[0].setAttribute("id","clone_button")
  //bdiv.appendChild(cln)[2];
  butcloned = document.getElementById('button_post')
  /*$(butcloned).click(function(){
    if(userLogged[0].fields.user!="anonimo"){
    if(isOpen==false) {
      buttonCommentClick()
    }
    else {
      msgIsTexareaOpen()

    }
  }
  }
  )*/
  $('.mybut').hover(function(e){
    $('.mybut').css("box-shadow","0 0 0 white")
  },
  function(){
    $('.mybut').css("box-shadow","10px 10px 10px #719ECE")
  })
  $.ajax({
    url: '/post/showposts',
    data: {
      'loginis': loginis,'tagTitle' : tagTitle ,
    },


    dataType: 'json',
    success: function (data) {
      s = cleanJson(data)
      try {
        obj = JSON.parse(s);
        comments_json = JSON.parse(obj.data_comm);// blog.comment
        resps_json = JSON.parse(obj.resps);
        profiles_json = JSON.parse(obj.profiles);
        userLogged=JSON.parse(obj.userLogged);
      }
      catch(SyntaxError){
        console.log("Dati inconsistenti ricevuti dal server , i commenti potrebbero non esistere !")
        profiles_json = JSON.parse(obj.profiles);
        userLogged=JSON.parse(obj.userLogged);
      }
      var photoResp
      var i=0




      //initial_y=(parseInt(obj3.length))-1
      for (i=0;i<=comments_json.length-1;i=i+1){
        for (z=0;z<=profiles_json.length-1;z=z+1){
          // if(obj5_photo[z].fields.user==obj2[i].fields.author){
          if(profiles_json[z].pk==comments_json[i].fields.author){
            profiles.push(new Profile(profiles_json[z].fields.first_name,profiles_json[z].fields.photo))
            mess.push(new Post("post",profiles_json[z].fields.first_name,comments_json[i].fields.title,comments_json[i].fields.body,getDateFromDjangoDate(comments_json[i].fields.publish),BASE_PHOTO_DIR+profiles_json[z].fields.photo,comments_json[i].pk))
            createPostArea(mess[indexX])
            break;
          }
        }
        // creo la textarea per il post e con l head .
        z=0
        // NUOVO PUNTO DINSERIMENTO CICLO FOR PER RISPOSTE
        for (y=resps_json.length-1; y>=0; y=y-1){
          if(comments_json[i].pk==resps_json[y].fields.commento){
            for (var z2=0;z2<=profiles_json.length-1;z2=z2+1){
              if(profiles_json[z2].pk==resps_json[y].fields.author){
                if (resps_json[y].fields.author=="anonimo"){
                  photoResp=obj5_photo
                }
                else{
                  photoResp=BASE_PHOTO_DIR+profiles_json[z2].fields.photo
                }
                resps.push(new Resp(profiles_json[z2].fields.first_name,resps_json[y].fields.body,getDateFromDjangoDate(resps_json[y].fields.publish),mess[indexX],photoResp," risponde a "+mess[indexX].author,resps_json[y].pk,"resp"))
                mess[indexX].risposte.push(resps[q])
                createPostArea(resps[q])
                q=q+1
              }
            }
          }
        }
        y=0
        indexX=indexX+1
      }
    }
  }
);

}
);

// Metodo chiamato da post , resp e nuovo Post//
function createPostArea(messOrResp,elementToAppendArea){
  if(!(isOpen==true)) {
    paPostOrResp=new postArea(messOrResp)
    paPostOrResp.makeHeadBlog(messOrResp,paPostOrResp,elementToAppendArea)
    paPostOrResp.postarea.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
    paPostOrResp.postarea.style.height = "auto";
    paPostOrResp.postarea.style.height = (paPostOrResp.postarea.scrollHeight) + "px";
    paPostOrResp.createButtonRispostaPost(messOrResp,paPostOrResp)
  }
  else{
    msgIsTexareaOpen()

  }
  if(messOrResp.type == "newresp" || messOrResp.type=="newpost") {
    isOpen=true
  }
  else {
    if(messOrResp.type == "post" || messOrResp.type == "resp") {
      isOpen=false
    }
  }
  return 0
}

function msgIsTexareaOpen(){
  alert("Hai un post già aperto !")
}

function sendToServer(post=Object(),url){
  if (post.type=="newresp"){
    data={
      'commento':post.post.pk,'type':post.type,'tutorial':post.thisTutorialTitle,'username':loginis,'body':post.body,
    }
  }
  else if (post.type=="newpost"){
    data={
      'tagTitle':tagTitle,'type':post.type,'tutorial':post.thisTutorialTitle,'username':loginis ,'body':post.body,
    }
  }
  if(post.type=="newpost" || post.type=="newresp"){
    let content=tutorial;
    $.ajax({
      url: url,
      data: data,
      dataType: 'json',
      success: function (data) {
        var userPhoto=data.photo
        if( post.type=="newpost" || post.type=="newresp") {
          isOpen=false
          makeHeadBlog(data.type,data.photo,this,data.aggiornato)
        }
      }
    }
  );
  console.log("ajax call finished");
}
return 0
}
