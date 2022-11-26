if (localStorage.getItem("Token") )
{
   
    GetSubjectByTermNow();
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

/*Liệt kê danh sách các môn học đã đăng kí với User và Term Hiện Tại*/ 
function GetSubjectByTermNow(){
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
            GetSubjectByTermNear();
        }
        var subjectsJsons=xhttp.responseText;
        var subjects= JSON.parse(subjectsJsons);
        if(xhttp.status==200)
        {
            selecSubjectHtml = '';
                 
            for (var i in subjects)
            {
                selecSubjectHtml+='<option value="'+subjects[i]['MajorSubjectID']+'">'+subjects[i]['SubjectCode']+' - '+subjects[i]['SubjectName']+'</option>';
            }
            document.getElementById("selecSubject").innerHTML=selecSubjectHtml;
        }
    }            
    xhttp.open("GET", "/TermSubjectStudent/api/SubjectByTermNow",false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}

/* Liệt kê danh sách các môn đã đăng kí trong kì gần nhất*/
function GetSubjectByTermNear(){
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
            selecSubjectHtml = '';
                 
            for (var i in subjects)
            {
                selecSubjectHtml+='<option value="'+subjects[i]['MajorSubjectID']+'">'+subjects[i]['SubjectCode']+' - '+subjects[i]['SubjectName']+'</option>';
            }
            document.getElementById("selecSubject").innerHTML=selecSubjectHtml;
        }
    }            
    xhttp.open("GET", "/TermSubjectStudent/api/SubjectByTermNear",false);
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
        GetCreditByID(choosenOption.value);
    }
}



function GetSubjectBySubjectCodeInput(){
    alert(document.getElementById('subjecttext').value);
}
function GetCreditByID(id){
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
            alert('opp')
        }
        var subjectsJsons=xhttp.responseText;
        var subjects= JSON.parse(subjectsJsons);
        if(xhttp.status==200)
        {

        }
    }            
    xhttp.open("GET", "/SectionClass/api/SectionClassApi/"+id,false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}