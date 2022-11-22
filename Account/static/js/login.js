
if ( localStorage.getItem("Token") )
{
    window.location='/home';
}   
function loginByEnter()
{
   if(event.keyCode==13)
   {
       login();
   }
}
function login()
{
   function getCookie(name) 
   {
       var cookieValue = null;
       if (document.cookie && document.cookie !== '') 
       {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++) 
           {
               var cookie = cookies[i].trim();
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) === (name + '=')) 
               {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }

   var csrfToken = getCookie('csrftoken');
   const xhttp = new XMLHttpRequest();
   xhttp.onload = function() 
   {
       var tokenResponseJson=xhttp.responseText
       var tokenResponse= JSON.parse(tokenResponseJson)
       if(xhttp.status==200)
       {
           localStorage.setItem("Token", tokenResponse['access']);
           window.location='/home'
           
       }
       else
       {
           document.getElementById("error").innerText=tokenResponse['message']
           document.getElementById("form__content__text__error").style="display:block"
       }
   }         
   const userInfo={
        username:document.getElementById("Username").value,
       password:document.getElementById("Password").value
   }
   postData=JSON.stringify(userInfo)
   xhttp.open("POST", "http://127.0.0.1:8000/Account/api/Token",false);
   xhttp.setRequestHeader("Content-type","application/json")
   xhttp.setRequestHeader("X-CSRFToken", csrfToken);
   xhttp.send(postData)
}
