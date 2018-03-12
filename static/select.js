    $(document).ready(function () {
        var searchrequest = new Object();
        searchrequest.sheetname = document.getElementById("p1").innerText;

        var data = JSON.stringify(searchrequest.sheetname)
        console.log(data)

        jQuery.post('/select/'+ searchrequest.sheetname,data,function(dat){
            console.log(dat);},"json");})
