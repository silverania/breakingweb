$(document).ready(function(){
$('.kpx_loginForm').click(function(){
  var input_username =document.getElementById('inputUsername')
  var username = input_username.text


alert("autenticato : "+login)

  setTimeout(function(){alert("Ciao, sono passati 5 secondi");},5000);



$.ajax({
  url: 'login/',
  data: {
    'username': username,
  },
  dataType: 'json',
  success: function (data) {
  s = cleanJson(data)
}
});
});
})
