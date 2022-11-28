const listcredit=[];
var subjectselect=0;
if (localStorage.getItem("Token") )
{
   
    GetSubjectByTermNow();
    GetSectionClassStudentNow();
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
            
        }
        var creditsJsons=xhttp.responseText;
        var credits= JSON.parse(creditsJsons);
        if(xhttp.status==200)
        {
            subjectselect=id;
            var seleccreditsHtmls = '<thead><tr><th>Trạng Thái</th><th>Mã Môn Học</th><th>Tên Môn Học</th><th>Sĩ số</th><th>Tối Đa</th><th>Thứ</th><th>Tiết Bắt Đầu</th><th>Số Tiết</th><th>Giảng Viên</th><th style="width:300px">Danh Sách Ngày Học</th></tr></thead>';
            for (var i in credits)
            {
                
                var dayDefault=credits[i]["dayDefault"].split(",");
                var dem= dayDefault.length;
                var seachtbd =dayDefault[0].search("T");
                var thu= dayDefault[0].slice(0,1);
                var tietdb=dayDefault[0].slice(dayDefault[0].search("T")+1,dayDefault[0].search("S"));
                var sotiet =dayDefault[0].slice(dayDefault[0].search("S")+1,dayDefault[0].search("S")+2);
                seleccreditsHtmls+='<tbody class="creditcontent"><tr><td id="checkbox" rowspan="'+String(dem)+'"><input type="checkbox" value="'+credits[i]["id"]+'" onclick="PostCredit(this)"';
                if(listcredit.includes(credits[i]["id"]))
                {
                    seleccreditsHtmls+=' checked ';
                }
                seleccreditsHtmls+='> </td><td rowspan="'+String(dem)+'">'+'>'+credits[i]["subjectCode"]+'</td><td rowspan="'+String(dem)+'">'+credits[i]["subjectName"]+'</td><td rowspan="'+String(dem)+'">'+String(credits[i]["quanlityReal"])+'</td><td rowspan="'+String(dem)+'">'+String(credits[i]["quanlity"]-credits[i]["quanlityReal"])+'</td><td >'+thu+'</td><td>'+tietdb+'</td><td>'+sotiet+'</td> <td rowspan="'+String(dem)+'">'+credits[i]["Teacher"]+'</td><td rowspan="'+String(dem)+'">'+credits[i]["dayLessonList"]+'</td></tr>';
                for (var j=1;j<dayDefault.length;j++)
                {
                    seleccreditsHtmls+='<tr><td>'+dayDefault[j].slice(0,1)+'</td><td>'+dayDefault[j].slice(dayDefault[j].search("T")+1,dayDefault[j].search("S"))+'</td><td>'+dayDefault[j].slice(dayDefault[j].search("S")+1,dayDefault[j].search("S")+2)+'</td></tr>'
                }
                seleccreditsHtmls+='</tbody>';
            }
            document.getElementById("table__Subjectlist").innerHTML=seleccreditsHtmls+"</tbody>";
        }
    }            
    xhttp.open("GET", "/SectionClass/api/SectionClassApi/"+id,false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}


// Đăng kí tín chỉ của môn học
function GetCredit_changed(){

    var selectCredits=document.querySelectorAll(".creditcontent input");
    for(var i=0;i<selectCredits.length;i++){

        selectCredits[i].checked= false;
    }

}
// Liệt Kê các tín chỉ đã đăng kí
function GetSectionClassStudentNow(){
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
            // GetTermSubjectStudentNear();
        }
        var subjectsJsons=xhttp.responseText;
        var subjects= JSON.parse(subjectsJsons);
        if(xhttp.status==200)
        {
            var selecSubjectHtmls = '<thead><tr><th>Lưu Đăng kí</th><th>Mã Môn Học</th><th>Tên Môn Học</th></tr></thead><tbody>';
                 
            for (var i in subjects)
            {
                listcredit.push(subjects[i]['classSection']);
                selecSubjectHtmls+='<tr><td id="checkbox" ><input type="checkbox" onclick="DeleteCredit(this)" checked'+' value="'+subjects[i]['classSection']+'"></td><td id="'+subjects[i]['SubjectCode']+'">'+subjects[i]['SubjectCode']+'</td><td >'+subjects[i]['SubjectName']+'</td></tr>';
            }
            document.getElementById("table__CheckSubjectlist").innerHTML=selecSubjectHtmls+"</tbody>";
        }
    }            
    xhttp.open("GET", "/SectionClassStudent/api/SectionClassStudentNow",false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}
// Đăng kí tín chỉ
function PostCredit(credit){
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
            GetCredit_changed();
            credit.checked=true;
            GetSectionClassStudentNow();
        }
        else if(xhttp.status==404)
        {
            if(tokenResponse["message"]!="Môn đã được đăng kí")
            {
                credit.checked=false;
                alert(tokenResponse["message"]);
            }
            else{
                DeleteCredit(credit);
            }
            
        }
    }         
    const CreInfo={
        id:credit.value
    }
    postData=JSON.stringify(CreInfo)
    xhttp.open("POST", "/SectionClassStudent/api/SectionClassStudentNow",false);
    xhttp.setRequestHeader("Content-type","application/json");
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token;
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.setRequestHeader("X-CSRFToken", csrfToken);
    xhttp.send(postData)

}
function DeleteCredit(credit){
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
            listcredit.pop(credit.value);
            if(subjectselect!=0)
            {

                GetCreditByID(subjectselect);
            }
            GetSectionClassStudentNow()
        }
        else if(xhttp.status==404)
        {
            alert("bạn không có quyền sửa");
        }
    }         

    xhttp.open("DELETE", "/SectionClassStudent/api/SectionClassStudentByID/"+credit.value,false);
    xhttp.setRequestHeader("Content-type","application/json")
    xhttp.setRequestHeader("X-CSRFToken", csrfToken);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}