if (localStorage.getItem("Token") )
{
    GetTermUserSign();
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

function inNgay(date){
    var month =(date.getMonth()+1).toString();
    if(month.length==1){
        month='0'+month;
    }
    var day=date.getDate().toString();
    if(day.length==1){
        day='0'+day;
    }
    return date.getFullYear()+"/"+month+"/"+day;
}
function ChuanHoaNgay(date){
    function search(str,a){
        for(var i=0;i<str.length;i++){
            if(a==str[i]){
                return i
            }
        }
        return -1
    }
    while(search(date,"/")!=-1){
        date.repalce("/","-")
    }
    return date
}
//Lấy ra tuần học theo đki
function GetTermUserSign(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() 
    {
        if(xhttp.status==403)
        {
            localStorage.removeItem('Token');
            window.location='/Account/Login';
        }

        var termsJsons=xhttp.responseText;
        var terms= JSON.parse(termsJsons);
        if(xhttp.status==200)
        {
            selecTermHtml = '';
            var check=0;
            for(var i =0;i<terms.length;i++){
                var now=new Date();
                var dayStart=new Date(ChuanHoaNgay(terms[i]["dayStart"]));
                var dayEnd =new Date(ChuanHoaNgay(terms[i]["dayEnd"]));
                if(now>dayStart && now<dayEnd){
                    terms[i]["checked"]=true;
                    check=1;
                    break;
                }
            }
            if(check==0){
                terms[0]["checked"]=true;
            }
            for (var i in terms)
            {
                selecTermHtml+='<option value="'+terms[i]['id']+'" ';
                if(terms[i]['checked']){
                    selecTermHtml+="selected ";
                    var checkDay =new Date(dayStart.toString());
                    var selectedTime='';
                    var nows='';
                    while(checkDay<=dayEnd)
                    {
                        var checkedDay= new Date(checkDay.toString());
                        checkDay.setDate(checkDay.getDate()+7);
                        
                        selectedTime+='<option value="'+terms[i]['id']+'-' +inNgay(checkedDay)+'-'+inNgay(checkDay)+'" ';
                        if(now<=checkDay && now>=checkedDay){
                            nows=terms[i]['id']+'-'+inNgay(checkedDay)+'-'+inNgay(checkDay);
                            selectedTime+=" selected ";
                        }
                        selectedTime+='>'+inNgay(checkedDay)+'-'+inNgay(checkDay)+'</option>';
                 
                    }
                    document.getElementById("schoolweek").innerHTML=selectedTime;

                    GetTkb(nows);
                }
                selecTermHtml+='>'+terms[i]['termName']+'</option>';
            }
            document.getElementById("selectterm").innerHTML=selecTermHtml;
        }
    }            
    xhttp.open("GET", "/TermSubjectStudent/api/TermStudentSign",false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}
function GetMonHoc_changed(){
    var selecSubject=document.getElementById("selectterm");
    var choosenOption= selecSubject.options[selecSubject.selectedIndex];
    if(choosenOption.value){
        GetTimeByTermID(choosenOption.value);  
    }
}
function GetTimeByTermID(id){
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
            alert("Học Kì Không tồn tại");
        }
        var termJson=xhttp.responseText;
        var term= JSON.parse(termJson);
        if(xhttp.status==200)
        {
            var now=new Date();
            var dayStart=new Date(ChuanHoaNgay(term["dayStart"]));
            var dayEnd =new Date(ChuanHoaNgay(term["dayEnd"]));
            var checkDay =new Date(dayStart.toString());

            var selectedTime='';

            while(checkDay<=dayEnd)
            {
                var checkedDay= new Date(checkDay.toString());
                checkDay.setDate(checkDay.getDate()+7);
                
                selectedTime+='<option value="'+term['id']+'" ';
                if(now<=checkDay && now>=checkedDay){
                    selectedTime+=" selected ";
                }
                selectedTime+='>'+inNgay(checkedDay)+'-'+inNgay(checkDay)+'</option>';
            
            }
            document.getElementById("schoolweek").innerHTML=selectedTime;
        }

    }
            
    xhttp.open("GET", "/TermSubjectStudent/api/TimeByTermID/"+id,false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}
//Lấy ra thời khóa biểu theo tuần
function Getschedule_changed(){
    var selecSubject=document.getElementById("schoolweek");
    var choosenOption= selecSubject.options[selecSubject.selectedIndex];
    if(choosenOption.value){
        GetTkb(choosenOption.value);
    }
}
function GetTkb(Terms){
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
        var scheduleJson=xhttp.responseText
        var schedule= JSON.parse(scheduleJson)
        if(xhttp.status==200)
        {
            console.log(schedule)
            var scheduleHtml='<thead><tr><th>...</th><th>Thứ 2</th><th>Thứ 3</th><th>Thứ 4</th><th>Thứ 5</th><th>Thứ 6</th><th>Thứ 7</th><th>Chủ Nhật</th><th>...</th></tr></thead><tbody>';
            for (var tiet=1;tiet<=12;tiet++)
            {
                scheduleHtml+='<tr><td>Tiết '+tiet.toString()+'</td>';
                for(var thu=2;thu<=8;thu++){
                    ok=0;
                    for(var z=0;z<schedule.length;z++){
                        if(thu.toString()+"T"+tiet.toString()==schedule[z].dayLesson){
                            checkdaylesson=schedule[z].Subject;
                            ok=1;
                            break;
                        }
                    }
                    if(ok!=0){

                        scheduleHtml+='<td class="subjectlesson" >'+checkdaylesson+'</td>';
                    }
                    else{

                        scheduleHtml+='<td></td>'
                    }
                }
                scheduleHtml+='<td>Tiết '+tiet.toString()+'</td></tr>';
            }
            scheduleHtml+='</tbody><tfoot><tr><th>...</th><th>Thứ 2</th><th>Thứ 3</th><th>Thứ 4</th><th>Thứ 5</th><th>Thứ 6</th><th>Thứ 7</th><th>Chủ Nhật</th><th>...</th></tr></tfoot>'
            document.getElementById("scheduletable").innerHTML=scheduleHtml;
        }
        else if(xhttp.status==404)
        {

            
        }
    }         
    var term=Terms.split("-");
    const Time={
        dayStart:term[1],
        dayEnd:term[2]
    }
    postData=JSON.stringify(Time)
    xhttp.open("POST", "/SectionClassStudent/api/GetScheduleByTime/"+term[0],false);
    xhttp.setRequestHeader("Content-type","application/json");
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token;
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.setRequestHeader("X-CSRFToken", csrfToken);
    xhttp.send(postData)

}