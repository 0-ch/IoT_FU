$(document).ready(function(){
  var list = []; // 將 list 定義在更高的範圍
  
  $("#progressbarTWInput").change(function(){
    $("#preview_progressbarTW_imgs").html(""); // 清除預覽
    readURL(this);
  });
  
  function readURL(input){
    var i = 0;
    var flag=1;
    if (input.files && input.files.length > 0) {
      if(i==0){
        $("#preview_progressbarTW_imgs").html("");
        $("#notify").html("<p>目前沒有圖片</p>");
      }
      var name = document.getElementById("name").value
      var num = document.getElementById("num").value
      
      for(var i = 0; i < input.files.length; i++){
        var reader = new FileReader();
        
        reader.onload = function (e) {
          var img = $("<img width='300' height='200'>").attr('src', e.target.result);
          // console.log(e.target.result);
          list.push(e.target.result);
          var data = {
            "name":name,
            "num":num,
            "base64String": e.target.result.split(',')[1] // 取得 base64 字串部分
          };
          
          if (data.base64String != null) {
            $.ajax({
              url: 'http://127.0.0.1:5000/upload',
              method: 'POST',
              data: JSON.stringify(data),
              contentType: "application/json",
              dataType: 'JSON',
              success: function(result) {
                console.log(JSON.stringify(data));
                
                if (result != null) {
                  console.log("新增成功！");
                }
              },
              error: function(data) {
                console.log("發生錯誤");
                flag=0;
              }
            });
          }
          $("#preview_progressbarTW_imgs").append(img);
          $("#notify").html("");
        };
        
        reader.readAsDataURL(input.files[i]);
      }
     
    } else {
      var noPictures = $("<p>目前沒有圖片</p>");
      $("#preview_progressbarTW_imgs").append(noPictures);
    }
    if(flag==1){
      alert("success upload");
    }
  }
  
  $("#imgInp").change(function() {
    console.log(123);
    readURL(this);
  });
});
