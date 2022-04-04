function bindCaptchButton(){

$("#btn-captcha").on('click',function(event){
var email =$("input[name='email']").val();
    if (!email){
    alert('请输入邮箱');
    }
});
}

$(function(){bindCaptchButton();});