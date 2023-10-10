document.addEventListener("DOMContentLoaded", function (){

  var selectAll = document.getElementById("selectAll")
  var allCheckboxes = document.querySelectorAll(".item-checkbox")
  var deleteMultiple = document.getElementById("deleteMultiple");	
  var deleteIds = document.getElementById("delete-ids");
  var allusers = document.getElementById("all-users");

  var toBeDeleted = [];		

  selectAll.addEventListener("click", function(item){


    var isChecked = selectAll.checked;
    allCheckboxes.forEach(function (item){

      if(isChecked){
        item.checked = true;								
      }
      else{
        item.checked = false;				
      }	

    })  
  })	

  deleteMultiple.addEventListener("click", function(){

    toBeDeleted = []
    allusers.innerHTML = " er valgt";
    deleteIds.value = "";

    allCheckboxes.forEach(function (item){

      if(item.checked == true){

        toBeDeleted.push(item.dataset.id);

      }
    })

    toBeDeleted.forEach(function (item){

      deleteIds.value += item + ","

    })

    allusers.innerHTML = toBeDeleted.length + allusers.innerHTML;

  })

//Sets id of what to edit
var editUsers = document.querySelectorAll(".edit")
var deleteUsers = document.querySelectorAll(".delete")

var editId = document.getElementById("edit-id");
var deleteId = document.getElementById("delete-id");


function SetEditText(userId){

  emails = document.querySelectorAll(".user-email").forEach(function (item){


    if(item.dataset.id == userId){
      document.getElementById("edit-mail").value = item.innerHTML
    }



  })

  names = document.querySelectorAll(".user-name").forEach(function (item){
  

    if(item.dataset.id == userId){
      document.getElementById("edit-name").value = item.innerHTML
    }

  })

}

editUsers.forEach(function (item){

  item.addEventListener("click", function(){

    editId.value = item.dataset.id;
    SetEditText(item.dataset.id);

  })
})


deleteUsers.forEach(function (item){

  item.addEventListener("click", function (){

    deleteId.value = item.dataset.id;

  })
})	
})
