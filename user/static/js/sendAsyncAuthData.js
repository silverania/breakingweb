$('.kpx_loginForm').click(function(){
  var input_username =document.getElementById('inputUsername')
  var username = input_username.text
  
})
$.ajax({
  url: 'login/',
  data: {
    'username': ,
  },
  dataType: 'json',
  success: function (data) {
  s = cleanJson(data)
}
});
