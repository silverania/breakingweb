function getParam(){
    const params = new URLSearchParams(window.location.search);
    var valuenext=params.get('next');
    //var login="{{ request.user.is_authenticated }}"
    $('[data-toggle="tooltip"]').tooltip()
    var r=document.getElementById("a_reg");
    var pf=document.getElementById("a_passwordforget");
    var pc=document.getElementById("a_changepassword");
    r.href="/user/register/blog?next="+params.get('next');
    pc.href="{% url 'change_password' %}?next="+params.get('next');
    pf.href="{% url 'password_reset' %}?next="+params.get('next');
    //var fs= document.getElementById("formlogin");
    if (valuenext){
        localStorage.setItem("next",valuenext);
        next=localStorage.getItem("next")
        console.log("valuenext not empty : "+next)
    }
    else{
        next=localStorage.getItem("next")
        window.location.href=window.location.href+"?next="+next
        console.log(next)
    }
    return next;
}
