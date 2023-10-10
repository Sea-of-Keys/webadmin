document.addEventListener("DOMContentLoaded", function (){

  var selectAll = document.getElementById("selectAll")
  var allCheckboxes = document.querySelectorAll(".item-checkbox")
  var deleteMultiple = document.getElementById("deleteMultiple");	
  var deleteIds = document.getElementById("delete-ids");
  var allusers = document.getElementById("all-users");

  var toBeDeleted = [];		


  var url = "https://api.seaofkeys.com"

	function getvals(id, endpoint){
		return fetch(url +  endpoint + id ,
		{
			method: "GET",
		  headers: {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
		  },
		})
		.then((response) => response.json())
		.then((responseData) => {		  
		  return responseData["team"]["users"];
		})
		.catch(error => console.warn(error));
	  }


	  function setResponse(response){		




     

      var edit_list =  document.getElementById("mySelectOptions");



      response.forEach(function (item){

        const node = document.createElement("li");    
        const textnode = document.createTextNode(item.name);

        node.dataset.id = item.id;       
        
        node.appendChild(textnode);
        edit_list.appendChild(node);
  
      })    




      console.log(response[0])
		

	  }	  
	  




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

    getvals(item.dataset.id, "/team/").then(response => setResponse(response));   

  })
})


deleteUsers.forEach(function (item){

  item.addEventListener("click", function (){

    deleteId.value = item.dataset.id;

  })
})	
})
