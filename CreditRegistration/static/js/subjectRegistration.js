if (localStorage.getItem("Token") )
{
    GetSubjectByTermNow();
    GetTermSubjectStudentNow();
}
else
{
    localStorage.removeItem('Token');
    window.location='/Account/Login';
}
function LogOut()
{
    window.location="/Account/Login";
    localStorage.removeItem('Token');
}
/* Liệt Kê danh sách các môn mặc định trong kì */ 
function GetSubjectByTermNow()
{
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() 
    {
        if(xhttp.status==403)
        {
            localStorage.removeItem('Token');
            window.location='/Account/Login';
        }
        var subjectsJsons=xhttp.responseText;
        var subjects= JSON.parse(subjectsJsons);
        if(xhttp.status==200)
        {
            selecSubjectHtml = '';
                 
            for (var i in subjects)
            {
                selecSubjectHtml+='<option value="'+subjects[i]['SubjectCode']+'">'+subjects[i]['SubjectCode']+' - '+subjects[i]['SubjectName']+'</option>';
            }
            document.getElementById("selecSubject").innerHTML=selecSubjectHtml;
        }
    }            
    xhttp.open("GET", "/Subject/api/GetSubjectByTermNow",false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}
/*Liệt kê danh sách các môn học đã đăng kí với User và Term Hiện Tại*/ 
function GetTermSubjectStudentNow(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() 
    {
        if(xhttp.status==403)
        {
            localStorage.removeItem('Token');
            window.location='/Account/Login';
        }
        else if(xhttp.status==404)
        {
            document.getElementById("erornotfound").style.display = "block";
            GetTermSubjectStudentNear();
        }
        var subjectsJsons=xhttp.responseText;
        var subjects= JSON.parse(subjectsJsons);
        if(xhttp.status==200)
        {
            var selecSubjectHtmls = '<thead><tr><th>Lưu Đăng kí</th><th>Mã Môn Học</th><th>Tên Môn Học</th></tr></thead><tbody>';
                 
            for (var i in subjects)
            {
                selecSubjectHtmls+='<tr><td id="checkbox" ><input type="checkbox" onclick="DeleteTermSubjectStudentBysubjectCode(this)" checked'+' value="'+subjects[i]['SubjectCode']+'"></td><td id="'+subjects[i]['SubjectCode']+'">'+subjects[i]['SubjectCode']+'</td><td >'+subjects[i]['SubjectName']+'</td></tr>';
            }
            document.getElementById("table__Subjectlist").innerHTML=selecSubjectHtmls+"</tbody>";
        }
    }            
    xhttp.open("GET", "/TermSubjectStudent/api/GetTermSubjectStudentNow",false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}

/* Liệt kê danh sách các môn đã đăng kí trong kì gần nhất*/
function GetTermSubjectStudentNear(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() 
    {
        if(xhttp.status==403)
        {
            localStorage.removeItem('Token');
            window.location='/Account/Login';
        }
        else if(xhttp.status==404)
        {
            document.getElementById("erornotfound").style.display = "block";
        }
        var subjectsJsons=xhttp.responseText;
        var subjects= JSON.parse(subjectsJsons);
        if(xhttp.status==200)
        {
            var selecSubjectHtmls = '<thead><tr><th>Mã Môn Học</th><th>Tên Môn Học</th></tr></thead><tbody>';
                 
            for (var i in subjects)
            {
                selecSubjectHtmls+='<tr><td id="'+subjects[i]['SubjectCode']+'">'+subjects[i]['SubjectCode']+'</td><td >'+subjects[i]['SubjectName']+'</td></tr>';
            }
            document.getElementById("table__Subjectlist").innerHTML=selecSubjectHtmls+"</tbody>";
        }
    }            
    xhttp.open("GET", "/TermSubjectStudent/api/GetTermSubjectStudentNear",false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}
// hàm Tìm kiếm môn học bằng mã môn học
function GetMonHoc_changed(){
    var selecSubject=document.getElementById("selecSubject");
    var choosenOption= selecSubject.options[selecSubject.selectedIndex];
    if(choosenOption.value){
        PostTermSubjectStudentNow(choosenOption.value);
    }
}



function GetSubjectBySubjectCodeInput(){
    PostTermSubjectStudentNow(document.getElementById('subjecttext').value);
}

function PostTermSubjectStudentNow(subjectCode)
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
        if(xhttp.status==201)
        {
            
            GetTermSubjectStudentNow();
        }
        else if(xhttp.status==404)
        {
            alert("bạn không có quyền sửa");
        }
    }         
    const userInfo={
        subjectCode:subjectCode
    }
    postData=JSON.stringify(userInfo)
    xhttp.open("POST", "/TermSubjectStudent/api/GetTermSubjectStudentNow",false);
    xhttp.setRequestHeader("Content-type","application/json");
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token;
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.setRequestHeader("X-CSRFToken", csrfToken);
    xhttp.send(postData)
    }
function DeleteTermSubjectStudentBysubjectCode(oke){
    subjectCode=oke.value;
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
        if(xhttp.status==204)
        {
            GetTermSubjectStudentNow();
        }
        else if(xhttp.status==404)
        {
            alert("bạn không có quyền sửa");
        }
    }         

    xhttp.open("DELETE", "/TermSubjectStudent/api/TermSubjectStudentBysubjectCode/"+subjectCode,false);
    xhttp.setRequestHeader("Content-type","application/json")
    xhttp.setRequestHeader("X-CSRFToken", csrfToken);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}
